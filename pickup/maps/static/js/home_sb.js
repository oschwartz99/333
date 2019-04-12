$("#sidebar").on('click', ".home_sb_link", function() {
    $.ajax({
        url: '/ajax/home_sb/', 
        success: function(data) {
            // replace content in page with event form
            document.getElementById("sidebar").innerHTML = data["page"];
            marker.remove(); // remove marker if it's on map
        }
    });
});

   