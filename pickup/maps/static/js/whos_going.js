$("#map").on("click", ".whos_going", function(event) {
    var eventId = event.target.id.slice(-1);
    document.getElementById("sidebar").innerHTML = "\
    <div style='overflow = auto;'> \
    <div class='container'> \
        <div class='card'> \
            <div class = 'card-body' \
                <p>First Last</p> \
            </div> \
        </div> \
        <div class='card'> \
            <div class = 'card-body' \
                <p>First Last</p> \
            </div> \
        </div> \
        <div class='card'> \
            <div class = 'card-body' \
                <p>First Last</p> \
            </div> \
        </div> \
        <div class='card'> \
            <div class = 'card-body' \
                <p>First Last</p> \
            </div> \
        </div> \
        <div class='card'> \
            <div class = 'card-body' \
                <p>First Last</p> \
            </div> \
        </div> \
        <div class='card'> \
            <div class = 'card-body' \
                <p>First Last</p> \
            </div> \
        </div> \
        <div class='card'> \
            <div class = 'card-body' \
                <p>First Last</p> \
            </div> \
        </div> \
        <div class='card'> \
            <div class = 'card-body' \
                <p>First Last</p> \
            </div> \
        </div> \
        <div class='card'> \
            <div class = 'card-body' \
                <p>First Last</p> \
            </div> \
        </div> \
        <div class='card'> \
            <div class = 'card-body' \
                <p>First Last</p> \
            </div> \
        </div> \
    </div>\
    </div>";
})