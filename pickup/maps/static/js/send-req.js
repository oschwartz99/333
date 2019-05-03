$("#sidebar").on("click", ".send", function(event) {
	console.log(event.target);
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