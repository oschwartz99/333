$("#sidebar").on("click", "#search_events", function(event) {
    $.ajax({
        url: '/ajax/load_event_search/',
        success: function(data) {
            document.getElementById("sidebar").innerHTML = data['page'];
        },
    });
});