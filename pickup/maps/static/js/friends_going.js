$("#map").on("click", ".friends_going", function(event) {
    var eventId = event.target.id.slice(14);

    /* Create AJAX route which says to the database:
    here is the event id, return a rendered string
    of all of the user's friends going to an event in the sidebar.
    Then, use JS to display this in the sidebar */
    $.ajax({
        url: '/ajax/friends_going/',
        data: {"event_id": eventId},
        success: function(data) {
            document.getElementById("sidebar").innerHTML = data['page'];
        },
    });
});