$(document).ready(function() {
    var lng = document.getElementById("id_lng");
    var lat = document.getElementById("id_lat");
    if (!(localStorage.getItem("lat") === null)) {
        lng.value = localStorage.getItem("lng");
        lat.value = localStorage.getItem("lat");
    }
});