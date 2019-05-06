function updateNotifs(event) {
	$.ajax({
		url: "/ajax/notifs/",
		data: {},
		success: function(data) {
			console.log("success");
			console.log("number of reqs: " + data["notifs"]);
			console.log($("#home-notifs").length);
			if ($("#home-notifs").length > 0)
				document.getElementById("home-notifs").innerHTML = data["notifs"];
			else if ($("#friends-notifs").length > 0)
				document.getElementById("friends-notifs").innerHTML = data["notifs"];
		}
	});
}

$(document).ready(updateNotifs());
$("#sidebar").on("click", "#friends_sb_link", updateNotifs);
$("#sidebar").on("click", ".home_sb_link", updateNotifs);
