/* Underline 'Add an event' on hover */
function toggleUnderline() { 
    $(this).toggleClass('underline');
}
$("#add_event_link").hover(toggleUnderline, toggleUnderline);
