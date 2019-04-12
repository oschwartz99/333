$("#map").on("click", ".whos_going", function(event) {
    var eventId = event.target.id.slice(-1);

    /* Create AJAX route which says to the database:
    here is the event id, return a rendered string
    of all the people going to an event in the sidebar.
    Then, use JS to display this in the sidebar */
    $.ajax({
        url: '/ajax/whos_going/',
        data: {"event_id": eventId},
        success: function(data) {
            document.getElementById("sidebar").innerHTML = data['page'];
        },
    });

    // var text = "";
    // console.log(going_users[eventId]);
    // for (var i = 0; i < going_users[eventId].length; i++)
        // text += going_users[eventId][i];   
    // console.log("text: " + text); 
    // document.getElementById("sidebar").innerHTML = text;
})