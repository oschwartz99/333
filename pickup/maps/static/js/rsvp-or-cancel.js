/* LISTENER: Going to/Cancelling an event */
$("#map").on('click', ".event-action", function(event) {
    var button = event.target;
    
    // User clicked cancel
    if (button.classList.contains("btn-danger")) {
        $.ajax({
            url: '/ajax/user_cancelled/',
            data: {"event_id": button.id},
            success: function() {
                button.className="btn btn-success event-action list-group-item";
                button.innerHTML="Going";
                $.ajax({ // update number going
                    url: 'ajax/get_number_going/',
                    data: {"event_id": button.id},
                    success: function(data) {
                        document.getElementById("number-going-" + button.id).innerHTML = "Number Attending: " + data.number_going;
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
                button.className="btn btn-danger event-action list-group-item";
                button.innerHTML="Not Going";
                $.ajax({ // update number going
                    url: 'ajax/get_number_going/',
                    data: {"event_id": button.id},
                    success: function(data) {
                        document.getElementById("number-going-" + button.id).innerHTML = "Number Attending: " + data.number_going;
                    }
                });
            }
        });
    }
});