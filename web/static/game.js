$.getScript("games/tictactoe.js");

var gameName = '';
var gameId = '';
var playerId = '';
var gameInstance = null;

function getGameIdAndJoin(gameName) {
    gameId = window.prompt("Enter the game id:", "");
    joinGame(gameName, gameId);
}

function createGame(gameName) {
    var postData = {
        game_name: gameName,
    };
    $.post('api/create', postData, function(data) {
        data = JSON.parse(data);
        gameId = data['game_id'];
        $('#game-id').html('Game Id: ' + gameId);
        joinGame(gameName, gameId);
    });
}

function joinGame(gameName, gameId) {
    gameInstance = new TicTacToe();

    var postData = {
        game_name: gameName,
        game_id: gameId,
    };
    $.post('api/join', postData, function(data) {
        data = JSON.parse(data);
        playerId = data['player_id'];
        $('#game-container').html(
            '<a class="game-link" onclick="javascript: startGame(\'' + gameName + '\', \'' + gameId + '\', \'' + playerId + '\');">Start Game</a>'
        );
        refreshState(gameName, gameId, playerId, false);
    });
}

function startGame(gameName, gameId, playerId) {
    var postData = {
        game_name: gameName,
        game_id: gameId,
        player_id: playerId
    };
    $.post('api/start', postData, function(data) {
        // TODO(paul): decide what game to create based on gameName
        refreshState(gameName, gameId, playerId, true);
    });

}
function refreshState(gameName, gameId, playerId, refreshOnce) {
    var getParams = {
        game_name: gameName,
        game_id: gameId,
        player_id: playerId,
    };
    $.get('api/state', getParams, function(data) {
        data = JSON.parse(data);
        if (data['started'])
            gameInstance.paintBoard(data['board']);
        if (refreshOnce == false)
            setTimeout(refreshState, 3000, gameName, gameId, playerId, false);
    });
}

