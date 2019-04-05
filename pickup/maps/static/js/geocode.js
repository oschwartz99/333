/* Initialize Geocoder */
function loadGeocoder() {
    if (coors['lat'] !== undefined) {
        var geocoder = new MapboxGeocoder({
            accessToken: mapboxgl.accessToken,
            placeholder: 'Search for places near you',
            bbox: [coors['lng']-2, coors['lat']-2, coors['lng']+2, coors['lat']+2],
            proximity: {
                longitude: coors['lng'],
                latitude: coors['lat'],
        });
        map.addControl(geocoder);
    }
    else
        setTimeout(loadGeocoder, 10);
}
loadGeocoder();

