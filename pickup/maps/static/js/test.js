$(document).ready(function() {
    $("#test_element").click(function() {
        $.ajax({
            url: '/test_ajax/',
            data: {"info": "you suck"},
            success: function(data) {
                var sidebar = document.getElementById("sidebar");
                sidebar.innerHTML = data["key"]
            }
        });
    });
});