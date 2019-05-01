/* ------------------------------------------------------------------------------------------------------------------------------- */
// SETUP OF VARIABLES
mapboxgl.accessToken = 'pk.eyJ1IjoiY29zMzMzIiwiYSI6ImNqdDYzY3A0ZDBkMGc0YXF4azczdXRheWMifQ.3VeYeV_c-231Lab62H2XtQ';

/* Dict containing all markers.
   Stored as key:value pairs, with the key being 
   the event_id, and the value being the JS object. */
markers = {};
var coors = {};

/* Create a marker, and a popup associated with that marker.
    These will be displayed if an event is created. (The popup
    is for deleting the marker).
    These are only displayed if the listener below runs. */
var popup = new mapboxgl.Popup().setHTML("<button class='btn btn-sm btn-danger' id='delete_add_event'>Remove</button>");
var marker = new mapboxgl.Marker({
    draggable: true
})
    .setPopup(popup);

/* ------------------------------------------------------------------------------------------------------------------------------- */

/* Initialize map object */
const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v9',
    center: [0,0], // doesn't matter what these are
    zoom: 1,
});

/* Modify map with icons & other settings */
map.on('load', function () {
    console.log("map load triggered");

    // Add compass, zoom, and geolocate
    const geolocate = new mapboxgl.GeolocateControl({
        positionOptions: {
            enableHighAccuracy: true
        },
        trackUserLocation: true
    });
    
    /* Trigger geolocate (i.e. zoom in to user's position) */
    map.addControl(geolocate, 'top-left');
    map.addControl(new mapboxgl.NavigationControl(), 'bottom-right');
    setTimeout(function() {
        geolocate.trigger();
    }, 10);

    /* Save lat and lng of current position (for geocode.js) */
    setTimeout(function() {
        try {
        coors['lat'] = geolocate._lastKnownPosition.coords.latitude;
        coors['lng'] = geolocate._lastKnownPosition.coords.longitude;
        }
        catch {
            console.log("waiting for geolocation to be tracked...")
        }
    }, 1000);

    /* Create a call back function. First, it queries the database with an 
       AJAX request. Following this, it calls the callback function argument
       (see next code block). */
    events = [];
    eventNumber = 0;
    function displayEvents(callback) {
        $.ajax({
            url: '/ajax/fetch_from_db/',
            data: {}, // empty query - just fetch all events
            dataType: 'json',
            success: function (data) {
                for (var key in data.events) {
                    event = {};
                    if (data.events.hasOwnProperty(key)) {
                        event["type"] = "Feature";
                        event["geometry"] = {
                            type: "Point",
                            coordinates: [data.events[key].lng, data.events[key].lat],
                        };
                        event["properties"] = {
                            "should_display": data.events[key].should_display,
                            "number_going": data.events[key].number_going,
                            "user_going": data.events[key].user_going,
                            "event_id": data.events[key].event_id,
                            "date": data.events[key].date,
                            "start_time": data.events[key].start_time,
                            "end_time": data.events[key].end_time,
                            "created_by": data.events[key].created_by,
                            "event_name": key.toString(),
                            "event_descr": data.events[key].event_descr,
                            "event_type": data.events[key].event_type,
                            "location": data.events[key].location,
                        };
                    }
                    
                    // only display event if user should be able to see it
                    if (data.events[key].should_display) {
                        events.push(event);
                        eventNumber++;
                    }
                }
            }
        });

        setTimeout(callback, 1000);
    }

    /* Executes an instance of the above function, complete with a callback. 
       Here the callback function adds all of the features to the map (i.e. 
        annotated markers). */
    displayEvents(function() {
        imageURLs = {
            "Party": "https://cdn4.iconfinder.com/data/icons/valentine-event-flat-circle/96/Drinks-512.png",
            "Concert": "https://cdn3.iconfinder.com/data/icons/education-vol-1-20/512/16-512.png",
            "Study": "https://image.flaticon.com/icons/png/512/562/562132.png",
            "Speech": "https://www.pngrepo.com/download/228157/lecture-lectern.png",
            "Meal": "https://cdn3.iconfinder.com/data/icons/ios-web-user-interface-flat-circle-shadow-vol-6/512/Food_fork_kitchen_knife_meanns_restaurant-512.png",
            "Movie": "http://icons.iconarchive.com/icons/graphicloads/100-flat/256/movie-icon.png",
            "Sports": "https://cdn2.iconfinder.com/data/icons/colored-simple-circle-volume-04/128/circle-flat-general-545202225-512.png",
        }

        console.log("displayEvents called");

        var geojson = {
            type: "FeatureCollection",
            features: [],
        };
        

        var numberPushed = 0;
        for (i = 0; i < eventNumber; i++) {
            geojson["features"].push(events[i]);
            numberPushed++;
        }

        

        var count = 0;
        var maxTries = 10;
        while (true) {
            try {
                console.log("trying...");
                console.log("number pushed: " + numberPushed);
                console.log("event number:  " + eventNumber);
                // add markers to map
                if (numberPushed != eventNumber) {
                    console.log("error!");
                    throw "events haven't been pushed yet"
                }
                
                else {
                    geojson.features.forEach(function(marker) {
                        console.log("in foreach function");

                        // create a HTML element for each feature
                        var el = document.createElement('div');
                        el.className = 'marker';
                        el.style.backgroundImage = "url('" + imageURLs[marker.properties.event_type] + "')";
                        // el.style.backgroundImage = "url('../Party.png')"

                        
                        // Set the HTML in the popup
                        html = "<div class='list-group' style='margin-bottom: 20px;' id='popup-" + marker.properties.event_id + "'><h3 style='cursor:default;' class=' btn btn-primary active list-group-item'>" 
                               + marker.properties.event_name + "</h3>"
                               + "<p style='cursor:default;' class='btn btn-primary active list-group-item'>" + marker.properties.event_descr + "</p>"
                               + "<p style='cursor:default;' class='btn btn-primary active list-group-item' id='number-going-" + marker.properties.event_id + "'>Number Attending: " + marker.properties.number_going + "</p>"
                               + "<p style='cursor:default;' class='btn btn-primary active list-group-item'>Date: " + marker.properties.date + "</p>"
                               + "<p style='cursor:default;' class='btn btn-primary active list-group-item'>From: " + marker.properties.start_time + "</p>"
                               + "<p style='cursor:default;' class='btn btn-primary active list-group-item'>To: " + marker.properties.end_time + "</p>";




                        html += "<p class='btn btn-warning text-dark active whos_going list-group-item' id='whos_going_" + marker.properties.event_id + "'>See who's going</p></div>";
                        html += "<p class='btn btn-warning text-dark active friends_going list-group-item' id='friends_going" + marker.properties.event_id + "'>See friends going</p></div>";

                        // html += "<div style='display: none;' id='hidden-" + marker.properties.event_id +"'>"
                        // // iterate over users_going and display on popup
                        // for (var i = 0; i < marker.properties.users_going.length; i++)
                        //     html += "<p>" + marker.properties.users_going[i] + "</p>";
                        // html += "</div>"

                        // "Going" or "Cancel" button, depending on if user is attending
                        if (marker.properties.user_going) 
                            html += "<div class='container'><button class='btn btn-danger event-action'" + 
                                    "id='" + marker.properties.event_id + "'" + ">Not Going</button></div>";
                        else 
                            html += "<button class='btn btn-success event-action'" + 
                                    "id='" + marker.properties.event_id + "'" + ">Going</button>";
                        
                        // If logged-in user created the event, add a 'delete' button
                        if (marker.properties.created_by)
                            html += "<button style='margin-top:10px;'"
                                    + "class='btn btn-danger delete_event'"
                                    + "id='delete-" + marker.properties.event_id + "'>Delete Event</button>";
                    
                        // make a marker for each feature and add to the map
                        var new_marker = new mapboxgl.Marker(el)
                            .setLngLat(marker.geometry.coordinates)
                            .setPopup(new mapboxgl.Popup()
                                .setHTML(html)
                            )
                            .addTo(map);

                        // append marker to markers dict
                        markers[marker.properties.event_id] = new_marker;
                    });
                    console.log("breaking");
                    break;
                }    
                
            } 
            catch {
                count++;
                if (count == maxTries) throw "ran out of tries";
            }
        }
    });    
});

/* ------------------------------------------------------------------------------------------------------------------------------- */

/* LISTENER: Removing the newly added event (created here 
    because the popup is a dynamically created element so we 
    have to make sure JQuery is listening to interactions 
    with it). */
$("#map").on('click', "#delete_add_event", function(){
    marker.remove();
    var eventInfo = document.getElementById("add_event");
    eventInfo.innerHTML = "";      // remove prompt
    eventInfo.style.display = '';
});