/* LISTENER: Going to/Cancelling an event */
$("#map").on('click', ".event-action", function(event) {
    var button = event.target;
    
    // User clicked cancel
    if (button.classList.contains("btn-danger")) {
        $.ajax({
            url: '/ajax/user_cancelled/',
            data: {"event_id": button.id},
            success: function() {
                button.className="btn btn-success active event-action list-group-item";
                button.innerHTML="You're not going. RSVP?";
                $.ajax({ // update number going
                    url: 'ajax/get_number_going/',
                    data: {"event_id": button.id},
                    success: function(data) {
                        document.getElementById("number-going-" + button.id).innerHTML = data.number_going + " have RSVP'd.";
                    }
                });
            }
        });
    }
    
    // User clicked going
    else if (button.classList.contains("btn-success")) {
        $.ajax({
            url: '/ajax/user_going/',
            data: {"event_id": button.id},
            success: function() {
                button.className="btn btn-danger active event-action list-group-item";
                button.innerHTML="You're going. Cancel RSVP?";
                $.ajax({ // update number going
                    url: 'ajax/get_number_going/',
                    data: {"event_id": button.id},
                    success: function(data) {
                        document.getElementById("number-going-" + button.id).innerHTML = data.number_going + " have RSVP'd.";
                    }
                });
            }
        });
    }
});