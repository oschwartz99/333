$("#sidebar").on('click', "#profile_sb_link", function() {
    $.ajax({
        data: {},
        url: '/ajax/profile_sb/', 
        success: function(data) {
            // replace content in page with event form
            var sidebar = document.getElementById("sidebar");
            sidebar.innerHTML = data["page"]
        }
    });
});

$("#sidebar").on('click', ".edit-profile-link", function(event) {
    $(document).ready(function() {
        if (event.target.id != 'profile-email') {
            $.ajax({
                data: {"field": event.target.id},
                url: '/ajax/edit_profile/', 
                success: function(data) {
                    // replace content in page with event form
                    var sidebar = document.getElementById("sidebar");
                    sidebar.innerHTML = data["page"]
                }
            }); 
        }
        else alert("We're sorry: you can't change your email just yet!");
    })
});


