$("#map").on("click", ".whos_going", function(event) {
    var id = "hidden-" + event.target.id.slice(-1);
    (document).getElementById(id).style.display = "block";    
})