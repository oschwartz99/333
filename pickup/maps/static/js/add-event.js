$(document).ready(function() {
    // Get form elements to fill in 
    var lng = document.getElementById("id_lng");
    var lat = document.getElementById("id_lat");
    
    // If we have the coordinates of a marker saved,
    // fill in the form with these coordinates.
    // Otherwise, do nothing. 
    if (typeof localStorage !== undefined && lng != null && lat != null) {
        if (localStorage.getItem("lng") !== null) {
            lng.value = localStorage.getItem("lng");
            lat.value = localStorage.getItem("lat");
        }
    }
});