mapboxgl.accessToken = 'pk.eyJ1IjoiY29zMzMzIiwiYSI6ImNqdDYzY3A0ZDBkMGc0YXF4azczdXRheWMifQ.3VeYeV_c-231Lab62H2XtQ';

/* Initialize map object */
const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v9',
    center: [151.21, -33.86],
    zoom: 8,
});

/* Perform once map is loaded */
map.on('load', function () {
    // Add compass and zoom control
    map.addControl(new mapboxgl.NavigationControl());

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
                                "description": "<form><input></input></form>",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [151, -33]
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


    // Change the cursor to a pointer when the mouse is over the places layer.
    map.on('mouseenter', 'points', function () {
        map.getCanvas().style.cursor = 'pointer';
    });

    // Change it back to a pointer when it leaves.
    map.on('mouseleave', 'points', function () {
        map.getCanvas().style.cursor = '';
    });
    
});