$("#sidebar").on('click', "#add_event_link", function() {

    $.ajax({
        url: '/ajax/add_event/',
        success: function(data) {
            // replace content in page with event form
            var sidebar = document.getElementById("sidebar");
            sidebar.innerHTML = data["page"]

            // add draggable marker and update lng/lat fields if it moves
            marker.setLngLat(map.getCenter()).addTo(map);
            var lng = document.getElementById("id_lng")
            lng.value = marker.getLngLat()['lng']
            var lat = document.getElementById("id_lat")
            lat.value = marker.getLngLat()['lat']
            marker.on('drag', function() {
                document.getElementById("id_lng").value = marker.getLngLat()['lng']
                document.getElementById("id_lat").value = marker.getLngLat()['lat']
            });

            // if user changes the lng/lat manually, move marker
            lng.addEventListener('change', function() {
                if (marker != undefined) {
                    if (lng.value == "")
                        lng.value = marker.getLngLat()['lng'];
                    else 
                        marker.setLngLat([lng.value, marker.getLngLat()['lat']]);
                }
            });
            lat.addEventListener('change', function() {
                if (marker != undefined) {
                    if (lat.value == "")
                        lat.value = marker.getLngLat()['lat'];
                    else
                        marker.setLngLat([marker.getLngLat()['lng'], lat.value]);
                }
            });

            $("#id_date").datepicker({
                minDate: 0,
            });
            $("#id_date").datepicker("show");
        }
    });
});
