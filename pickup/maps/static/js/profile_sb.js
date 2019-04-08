$("#sidebar").on('click', "#profile_sb_link", function() {
    console.log("clicked view prof");
    $.ajax({
        data: {"which": "orig"},
        url: '/ajax/profile_sb/', 
        success: function(data) {
            // replace content in page with event form
            var sidebar = document.getElementById("sidebar");
            sidebar.innerHTML = data["page"]
        }
    });
});

$("#sidebar").on('click', "#profile_edit_link", function() {
    console.log("clicked edit prof");
    $.ajax({
        data: {"which": "edit"},
        url: '/ajax/profile_sb/', 
        success: function(data) {
            // replace content in page with event form
            var sidebar = document.getElementById("sidebar");
            sidebar.innerHTML = data["page"]
        }
    });
});


