mapboxgl.accessToken = 'pk.eyJ1IjoiY29zMzMzIiwiYSI6ImNqdDYzY3A0ZDBkMGc0YXF4azczdXRheWMifQ.3VeYeV_c-231Lab62H2XtQ';

/* Initialize map object */
const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v9',
    center: [0,0], // doesn't matter what these are
    zoom: 1,
});

/* Modify map with icons & other settings */
map.on('load', function () {
    // Add compass, zoom, and geolocate
    const geolocate = new mapboxgl.GeolocateControl({
        positionOptions: {
            enableHighAccuracy: true
        },
        trackUserLocation: true
    });
    map.addControl(geolocate);
    map.addControl(new mapboxgl.NavigationControl());
    setTimeout(function() {geolocate.trigger();}, 10);

    /* Create a call back function. First, it queries the database with an 
       AJAX request. Following this, it calls the callback function argument
       (see next code block). */
    features = [];
    featureNumber = 0;
    function displayEvents(callback) {
        $.ajax({
            url: '/ajax/fetch_from_db/',
            data: {}, // empty query - just fetch all events
            dataType: 'json',
            success: function (data) {
                for (var key in data.events) {
                    feature = {};
                    if (data.events.hasOwnProperty(key)) {
                        feature["geometry"] = {
                            "type": "Point", 
                            "coordinates": [data.events[key].lng, data.events[key].lat],
                        };
                        feature["type"] = "feature";
                        feature["properties"] = {
                            "created_by": data.events[key].created_by,
                            "event_name": key.toString(),
                            "event_descr": data.events[key].event_descr,
                            "event_type": data.events[key].event_key,
                            "number_going": data.events[key].number_going,
                            "location": data.events[key].location,
                        }
                    }
                    features.push(feature);
                    featureNumber++;
                }
            }
        });

        /* Give the AJAX enough time to complete before loading images */
        setTimeout(function() {
            callback();
        }, 50);
    }

    /* Executes an instance of the above function, complete with a callback. 
       Here the callback function adds all of the features to the map (i.e. 
        annotated markers). */
    displayEvents(function() {
        imageURLs = {
            "Party": "http://icons.iconarchive.com/icons/iconsmind/outline/256/Wine-Glass-icon.png",
            "Concert": "https://cdn3.iconfinder.com/data/icons/simple-transparent-guitars/100/Acoustic_Guitar-512.png",
        }

        for (i = 0; i < featureNumber; i++) {
            map.loadImage("https://image.flaticon.com/icons/png/512/45/45637.png", 
            function(error, image) {
                if (error) throw error;
                map.addImage('bottle', image);
                map.addLayer({
                    "id": "points",
                    "type": "symbol",
                    "source" : {
                        "type": "geojson",
                        "data": {
                            "type": "FeatureCollection",
                            "features": features[i],
                        }
                    },
                    "layout": {
                        "icon-image": 'bottle',
                        "icon-size": 0.1
                    }
                });
            });

        }


            
    });

    

    // Handle clicks on icons
    map.on('click', 'points', function (e) {
        var coors = e.features[0].geometry.coordinates.slice();
        var created_by   = e.features[0].properties.created_by;
        var event_descr  = e.features[0].properties.event_descr;
        var event_name   = e.features[0].properties.event_name;
        var number_going = e.features[0].properties.number_going;
        var location     = e.features[0].properties.location;

        var html = "<div style='text-align:center'><p style='font-weight:bold;'>" + event_name + "</p>" + 
                   "<p>Created by: " + created_by + "</p>" +
                   "<p>" + event_descr + "</p>" +
                   "<p>Number attending: " + number_going + "</p>" +
                   "<p>Location: " + location + "</p></div>";

        while (Math.abs(e.lngLat.lng - coors[0]) > 180) {
            coors[0] += e.lngLat.lng > coors[0] ? 360 : -360;
        }

        new mapboxgl.Popup()
            .setLngLat(coors)
            .setHTML(html)
            .addTo(map);
    });


    // Change cursor to pointer when mouse is over 'points' layer
    map.on('mouseenter', 'points', function () {
        map.getCanvas().style.cursor = 'pointer';
    });

    // Change it back when mouse leaves
    map.on('mouseleave', 'points', function () {
        map.getCanvas().style.cursor = '';
    });
    
});

var popup = new mapboxgl.Popup().setHTML("<button class='btn btn-sm btn-danger' id='delete_event'>Remove</button>");
var marker = new mapboxgl.Marker({
    draggable: true
})
    .setPopup(popup);

/* Create an event: create a draggable marker for the 
   user to position */
$(document).ready(function() {
    /* Handler for clicking the "Add an event" */
    $("#add_anchor").click(function() {
        var eventInfo = document.getElementById("add_event");
        marker.setLngLat(map.getCenter()).addTo(map);
        function onDragEnd() {
            eventInfo.style.display = 'block';
            eventInfo.innerHTML = "Click <a id='goto_event' style='color: #00ffff;' href='/testing/'>here</a> to add event details once you've positioned your marker. \
                                <br>To delete the event, click the icon.";
        }
        marker.on('dragend', onDragEnd);

        /* Continually save the coordinates of the marker */
        setInterval(function() {
            localStorage.setItem("lng", marker.getLngLat().lng);
            localStorage.setItem("lat", marker.getLngLat().lat);
        }, 10);
    });

        
});

/* Handler for removing the event */
$("#map").on('click', "#delete_event", function(){
    console.log("hello")
    marker.remove();
    var eventInfo = document.getElementById("add_event");
    eventInfo.innerHTML = "";      // remove prompt
    eventInfo.style.display = '';
});