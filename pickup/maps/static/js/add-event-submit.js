function isNotEmpty(string) {
    return string !== "";
}

// Change behaviour of form
var form = $("#event_form");
form.onsubmit = function(e) {
    e.preventDefault();
}

$("#sidebar").on('click', "#add-event-submit", function() {
    var name  = $("#id_event_name")[0].value;
    var descr = $("#id_event_descr")[0].value;
    var dt    = $("#id_datetime")[0].value;
    var loc   = $("#id_location")[0].value;
    if (isNotEmpty(name) && isNotEmpty(descr) && isNotEmpty(dt) && isNotEmpty(loc)) {
        console.log("oi");
    }
});
