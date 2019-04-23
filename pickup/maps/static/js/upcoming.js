$("#sidebar").on('click', "#upcoming", function() {
	$.ajax({
        data: {},
        url: '/ajax/upcoming/', 
        success: function(data) {
            // replace content in page with event form
            var sidebar = document.getElementById("sidebar");
            sidebar.innerHTML = data["page"];

            $.ajax({
            	data: {},
            	url: 'ajax/upcoming_events/',
            	success: function(data) {
            		$("#upcoming-events").html(data)
            	}
            })
        },
    });
});