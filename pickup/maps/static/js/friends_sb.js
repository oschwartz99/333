$("#sidebar").on('click', "#friends_sb_link", function() {
    console.log("clicked friends page");
    $.ajax({
        url: '/ajax/friends_sb/',
        success: function(data) {
            var sidebar = document.getElementById("sidebar");
            sidebar.innerHTML = data["page"]
        }
    });
});

$("#sidebar").on('click', "#friends_view_site", function() {
    $.ajax({
        data: {},
        url: '/ajax/friends_view_site/',
        success: function(data) {
            var sidebar = document.getElementById("sidebar");
            sidebar.innerHTML = data["page"]

            $.ajax({
                data: {},
                url: 'ajax/friends_view/',
                success: function(data) {
                    $("#friends_view").html(data)
                }
            })
        }
    });
});

$("#sidebar").on('click', "#friends_add_link", function() {
    console.log("clicked view friends");
    $.ajax({
        url: '/ajax/friends_add/',
        success: function(data) {
            var sidebar = document.getElementById("sidebar");
            sidebar.innerHTML = data["page"]
        }
    });
});

$("#sidebar").on('click', "#friends_requests_link", function() {
    console.log("clicked view friend requests");
    $.ajax({
        url: '/ajax/friends_requests/',
        success: function(data) {
            var sidebar = document.getElementById("sidebar");
            sidebar.innerHTML = data["page"]
        }
    });
});

$("#sidebar").on('click', "#friends_remove_link", function() {
    console.log("clicked remove friends");
    $.ajax({
        url: '/ajax/friends_remove/',
        success: function(data) {
            var sidebar = document.getElementById("sidebar");
            sidebar.innerHTML = data["page"]
        }
    });
});