$("#sidebar").on("click", ".send", function(event) {
	event.target.classList.remove("btn-primary");
	event.target.classList.add("btn-success");
	event.target.innerText = "Friend request sent"
	event.target.disabled = true;

	$.ajax({
		data: {
			"username": event.target.id.substr(8),
		},
		url: '/ajax/send_req/',
		success: function() {}
	});
});

$("#sidebar").on("click", ".accept", function(event) {
	event.target.classList.remove("btn-primary");
	event.target.classList.add("btn-success");
	event.target.innerText = "You are now friends"
	event.target.disabled = true;

	// hide the corresponding reject button
	id = "reject-" + event.target.id.substr(7);
	document.getElementById(id).style.display = "none";

	$.ajax({
		data: {
	 		"username": event.target.id.substr(7),
	 	},
	 	url: '/ajax/accept_req/',
	 	success: function() {}
	});
});

$("#sidebar").on("click", ".reject", function(event) {
	event.target.classList.remove("btn-primary");
	event.target.classList.add("btn-success");
	event.target.innerText = "Request rejected"
	event.target.disabled = true;

	// hide the corresponding accept button
	id = "accept-" + event.target.id.substr(7);
	document.getElementById(id).style.display = "none";

	$.ajax({
		data: {
	 		"username": event.target.id.substr(7),
	 	},
	 	url: '/ajax/reject_req/',
	 	success: function() {}
	});
});

$("#sidebar").on("click", ".remove", function(event) {
	event.target.classList.remove("btn-primary");
	event.target.classList.add("btn-success");
	event.target.innerText = "Friend removed"
	event.target.disabled = true;

	$.ajax({
		data: {
	 		"username": event.target.id.substr(8),
	 	},
	 	url: '/ajax/remove_friend/',
	 	success: function() {}
	});
});