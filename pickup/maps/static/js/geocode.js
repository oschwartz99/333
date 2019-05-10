/* Initialize Geocoder */
function loadGeocoder() {
    if (coors['lat'] !== undefined) {
        var geocoder = new MapboxGeocoder({
            accessToken: mapboxgl.accessToken,
            placeholder: 'Search for places near you',
            bbox: [coors['lng']-45, coors['lat']-45, coors['lng']+45, coors['lat']+45],
            proximity: {
                longitude: coors['lng'],
                latitude: coors['lat'],
            },
        });
        map.addControl(geocoder, 'top-right');
    }
    else
        setTimeout(loadGeocoder, 10);
}
loadGeocoder();

