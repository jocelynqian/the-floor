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
    var postData = {
        game_name: gameName,
        game_id: gameId,
    };
    $.post('api/join', postData, function(data) {
        data = JSON.parse(data);
        playerId = data['player_id'];
        // TODO(paul): decide what game to create based on gameName
        gameInstance = new TicTacToe();
        refreshState(gameName, gameId, playerId);
    });
}

function refreshState(gameName, gameId, playerId) {
    var getParams = {
        game_name: gameName,
        game_id: gameId,
        player_id: playerId,
    };
    $.get('api/state', getParams, function(data) {
        data = JSON.parse(data);
        gameInstance.paintBoard(data['board']);
        setTimeout(refreshState, 3000, gameName, gameId, playerId)
    });
}

