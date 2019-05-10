$("#sidebar").on("click", ".accept", function(event) {
	event.target.classList.remove("btn-primary");
	event.target.classList.add("btn-success");
	event.target.innerText = "You are now friends"
	event.target.disabled = true;

	// $.ajax({
	// 	data: {
	// 		"username": event.target.id.substr(8),
	// 	},
	// 	url: '/ajax/send_req/',
	// 	success: function() {}
	// });
});