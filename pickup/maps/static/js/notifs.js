function updateReqNotifs() {
	$.ajax({
		url: "/ajax/notifs/",
		data: {},
		success: function(data) {
			console.log("updating friend req notifs");
			if ($("#home-notifs").length > 0) {
				if (data["notifs"] == 1)
					document.getElementById("home-notifs").innerHTML = data["notifs"] + " friend request";
				else if (data["notifs"] > 1)
					document.getElementById("home-notifs").innerHTML = data["notifs"] + " friend requests";
			}
			else if ($("#friends-notifs").length > 0)
				document.getElementById("friends-notifs").innerHTML = data["notifs"];
		}
	});
}

function updateUpcomingNotifs() {
	console.log("calling upcoming update");
	$.ajax({
		url: "/ajax/upcoming_events_number/",
		data: {},
		success: function(data) {
			if ($("#upcoming-number").length > 0) {
				if (data["number"] > 0)
					document.getElementById("upcoming-number").innerHTML = data["number"] + " coming up";
				else 
					document.getElementById("upcoming-number").innerHTML = "";
			}
		}
	});
}

$(document).ready(function() {
	updateUpcomingNotifs();
	updateReqNotifs();
});
$("#sidebar").on("click", "#friends_sb_link", updateReqNotifs);
$("#sidebar").on("click", ".home_sb_link", updateReqNotifs);
$("#sidebar").on("click", ".home_sb_link", updateUpcomingNotifs);