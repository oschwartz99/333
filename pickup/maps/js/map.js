import mapboxgl from 'mapbox-gl/dist/mapbox-gl';
mapboxgl.accessToken = '{{ mapbox_access_token }}';

const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v9'
});