var lp_css = "liars-poker-css";
if (!document.getElementById(lp_css)){
    var head = document.getElementsByTagName('head')[0];
    var link = document.createElement('link');
    link.id = lp_css;
    link.rel = 'stylesheet';
    link.type = 'text/css';
    link.href = 'games/liars_poker/liars_poker.css';
    head.appendChild(link);
}


function LiarsPoker(gameId, playerId){
    this.gameId = gameId;
    this.playerId = playerId;
}


LiarsPoker.prototype.refreshState = function(responseData){
    if (responseData['new_round']){
        $("#poker-table").remove();
        this.setTable(responseData);
        this.updateInfo("START!!!");
    }
    else{
        this.updateInfo(responseData['last_combo'].join());
    }

}

LiarsPoker.prototype.setTable = function(tableState) {

    var table = document.getElementById('poker-table');
    if (table == null) {
        var canv = '\
        <div id="poker-table"> \
            <div id="toolbar"> \
                <div id="help-button"> \
                </div> \
                <div id="call-button"> \
                </div> \
            </div> \
        </div>';
        $("#game-container").html(canv);
        table = document.getElementById('poker-table');
        $("#help-button").click(this.requestHelp);

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
        }

        // Display your hand
        hand = tableState['hand'];
        var handHTML = '<div id="hand">';

        for(card in hand){
            // TODO: display real cards
            handHTML = handHTML + '<div class="card-front">  \
                                    <p>' + hand[card] +'</p></div>';
        }
        handHTML = handHTML + '</div>';
        $("#poker-table").append(handHTML);

    }
    
}

LiarsPoker.prototype.requestHelp = function(e){
    console.log("it's happening");
    helpHTML = '<div id="help-page"> \
                <p>Nothing here yet</p> \
                </div>';
    $("#poker-table").append(helpHTML);

}

LiarsPoker.prototype.updateInfo = function(message){
    var infoBox = document.getElementById('info-box');
    if (infoBox == null) {
        var infoBoxHTML = '<div id="info-box"></div>'
        $("#poker-table").append(infoBoxHTML);       
    }
    $("#info-box").html('<p>' + message + '</p>');

}
/*
LiarsPoker.prototype.makeClaim = function(){

    var comboForm = $("#claim-form").serializeArray();
    var comboData = [];
    for(i in comboForm){
        if(comboForm[i].name == "combo"){
            combo[0] = comboForm[i].value;
        }
        else{
            combo.append(comboForm[i].value);
        }
    }

    var postData = {
        game_id: this.gameId,
        player_id: this.playerId, 
        update_json: JSON.stringify({
            move: "claim"
            combo: comboData
        })
    };

    $.post('api/update', postData, function(data) {
        refreshState(gameId, playerId, false);
    })

}

LiarsPoker.prototype.challenge = function(){
    var postData = {
        game_id: this.gameId,
        player_id: this.playerId, 
        update_json: JSON.stringify({
            move: "challenge"
        })
    };

    $.post('api/update', postData, function(data) {
        refreshState(gameId, playerId, false);
    })

}
*/
/*
LiarsPoker.prototype.challengeResult = function(){

}

*/