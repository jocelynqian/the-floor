var lp_css = "liars-poker-css";
if (!document.getElementById(lp_css)){
    var head = document.getElementsByTagName('head')[0];
    var link = document.createElement('link');
    link.id = lp_css;
    link.rel = 'stylesheet';
    link.type = 'text/css';
    link.href = 'liars_poker.css';
    head.appendChild(link);
}


function LiarsPoker(){
}


LiarsPoker.prototype.setTable = function(tableState) {

    var table = document.getElementById('poker-table');
    if (table == null) {
        var canv = '\
        <div id="poker-table"> \
            <div id="toolbar"> \
                <div id="help-button"></div> \
            </div> \
        </div>';
        $("#game-container").html(canv);
        table = document.getElementById('poker-table');

        // TODO: Add the round number

        // Add the players to the table
        cardCounts = tableState['counts'];
        for (player in cardCounts){
            var playerHTML = '\
            <div class="player-seat"> \
                <div class="name-placard"> \
                    <p class="player-name">' + player + '</p> \
                </div> \
                <div class="player-hand">';
            
           for(i = 0; i < cardCounts[player]; i++){
                playerHTML = playerHTML + '<div class=card-back></div>';
            }

            playerHTML = playerHTML + '</div></div>';

            $("#poker-table").append(playerHTML);

            console.log(cardCounts[player]);
        }

        // Display your hand
    }
    
}
