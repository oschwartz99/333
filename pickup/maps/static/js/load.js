mapboxgl.accessToken = 'pk.eyJ1IjoiY29zMzMzIiwiYSI6ImNqdDYzY3A0ZDBkMGc0YXF4azczdXRheWMifQ.3VeYeV_c-231Lab62H2XtQ';

/* Initialize map object */
const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v9',
    center: [0,0], // doesn't matter what these are
    zoom: 8,
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

    events = []

    $.ajax({
        url: '/ajax/fetch_from_db/',
        data: {}, // empty query - just fetch all events
        dataType: 'json',
        success: function (data) {
            events.push(data.events)
        }
    });

    // Display wine bottle icon
    map.loadImage('https://image.flaticon.com/icons/png/512/45/45637.png', 
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
                        "features": [{
                            "type": "Feature",
                            "properties": {
                                "description": events[0],
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-74.6672, 40.3573]
                            }
                        }]
                    }
                },
                "layout": {
                    "icon-image": 'bottle',
                    "icon-size": 0.1
                }
            });
    });

    // Handle clicks on icons
    map.on('click', 'points', function (e) {
        var coors = e.features[0].geometry.coordinates.slice();
        var descr = e.features[0].properties.description;

        while (Math.abs(e.lngLat.lng - coors[0]) > 180) {
            coors[0] += e.lngLat.lng > coors[0] ? 360 : -360;
        }

        new mapboxgl.Popup()
            .setLngLat(coors)
            .setHTML(descr)
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