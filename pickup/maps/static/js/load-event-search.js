$("#sidebar").on("click", "#search_events", function(event) {
    $.ajax({
        url: '/ajax/load_event_search/',
        success: function(data) {
            document.getElementById("sidebar").innerHTML = data['page'];
        },
    });
});

$("#sidebar").on("keyup", "#event-search", function() {
	$.ajax({
		type: "POST",
		url: "/ajax/event_search/",
		data: {
			'search_text': $("#event-search").val(),
			'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
		},
		success: searchSuccess,
		dataType: 'html',
	});
});

$("#sidebar").on("empty", "#event-search", function() {
	alert("empty!");
})

function searchSuccess(data, textStatus, jqXHR) {
	$("#event-search-results").html(data);
}
