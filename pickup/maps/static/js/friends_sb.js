$("#sidebar").on('click', "#friends_sb_link", function() {
    console.log("clicked friends page");
    $.ajax({
        url: '/ajax/friends_sb/',
        success: function(data) {
            var sidebar = document.getElementById("sidebar");
            sidebar.innerHTML = data["page"]
            setTimeout(updateReqNotifs, 200);
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

$("#sidebar").on('click', "#friends_requests_site", function() {
    $.ajax({
        data: {},
        url: '/ajax/friends_requests_site/',
        success: function(data) {
            var sidebar = document.getElementById("sidebar");
            sidebar.innerHTML = data["page"]

            $.ajax({
                data: {},
                url: 'ajax/friends_requests/',
                success: function(data) {
                    $("#friends_requests").html(data)
                }
            })
        }
    });
});

$("#sidebar").on('click', "#search_friends", function() {
    console.log("clicked add friend");
    $.ajax({
        url: '/ajax/load_friends_search/',
        success: function(data) {
            document.getElementById("sidebar").innerHTML = data['page'];
        },
    });
});

$("#sidebar").on("keyup", "#friend_search", function() {
	console.log("typed in search friend box");
    console.log($("#friend_search").val());
    $.ajax({
		type: "POST",
		url: "/ajax/friends_search/",
		data: {
			'search_text': $("#friend_search").val(),
			'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
		},
		success: function(data) {
            $("#friend_search_results").html(data);
        },
		dataType: 'html',
	});
});