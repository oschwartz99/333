$("#sidebar").on('click', "#home_sb_link", function() {
    $.ajax({
        url: '/ajax/home_sb/', 
        success: function(data) {
            // replace content in page with event form
            var sidebar = document.getElementById("sidebar");
            sidebar.innerHTML = data["page"]
        }
    });
});

   