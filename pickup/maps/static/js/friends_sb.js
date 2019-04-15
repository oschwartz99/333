$("#sidebar").on('click', "#friends_sb_link", function() {
    console.log("clicked view friends");
    $.ajax({
        url: '/ajax/friends_sb/',
        success: function(data) {
            var sidebar = document.getElementById("sidebar");
            sidebar.innerHTML = data["page"]
        }
    });
});
