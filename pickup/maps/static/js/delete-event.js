/* LISTENER: an event was deleted by its creator */
$("#map").on('click', ".delete_event", function(event) {
    // Display an alert message, and check if user wants to continue    
    if (confirm("Do you want to delete this event?")) {
        var event_id = event.target.id.slice(7);

        // remove the marker from map and markers dict
        markers[event_id].remove();
        delete markers[event_id];

        // make an ajax request to delete the event from DB
        $.ajax({
            url: '/ajax/delete_event/',
            data: {"event_id": event_id},
            success: function() {}
        })
    }
});