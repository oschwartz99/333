/* Underline 'Add an event' on hover */
function toggleUnderline() { 
    $(this).toggleClass('underline');
}
$(document).on("mouseenter", ".link", toggleUnderline);
$(document).on("mouseleave", ".link", toggleUnderline);
