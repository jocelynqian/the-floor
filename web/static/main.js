var mainHtml = '';
var gameName = '';
var gameId = '';
var playerId = '';

function setUpMainMenu() {
    $('.game-link').click(function() {
        mainHtml = $('#main').html();
        gameName = $(this).text();
        var gameTitle = '<h2>' + gameName + '</h2>';
        var gameIdLine = '<div id="game-id"></div>'
        var backToMain = "\
        <div id='home-menu'> \
            <a class='link' onclick='javascript: loadMainMenu()'>Main Menu</a> \
        </div>";
        var gameMenu = '\
        <div id="game-container"> \
            <a class="game-link" onclick="javascript: createGame(\'' + gameName + '\');">New Random Game</a><br> \
            <a class="game-link" onclick="javascript: getGameIdAndJoin(\'' + gameName + '\');">Join Game</a> \
        </div>';
        $('#main').html(backToMain + gameTitle + gameIdLine + gameMenu);
    });
}

$(document).ready(setUpMainMenu);

function loadMainMenu() {
    $('#main').html(mainHtml);
    setUpMainMenu();
}

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
        paintBoard(data['board']);
        setTimeout(refreshState, 3000, gameName, gameId, playerId)
    });
}

function clickHandler(e) {
    var board = document.getElementById('board');

    var width = board.width;
    var height = board.height;
    var context = board.getContext('2d');

    var clientX = e.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
    var clientY = e.clientY + document.body.scrollTop + document.documentElement.scrollTop;

    clientX -= board.offsetLeft;
    clientY -= board.offsetTop;

    var y = Math.floor(clientY / (height / 3));
    var x = Math.floor(clientX / (width / 3));

    var postData = {
        game_name: gameName,
        game_id: gameId,
        player_id: playerId, 
        update_json: JSON.stringify({
            square: [x, y]
        })
    };
    $.post('api/update', postData, function(data) {
        refreshState(gameName, gameId, playerId);
    });
}

function paintBoard(boardState) {
    var board = document.getElementById('board');
    if (board == null) {
        var canv = '\
        <div id="gameCanvasContainer" text-align="center"> \
            <canvas width="600" height="600" id="board" onclick="javascript: clickHandler(event);"></canvas> \
        </div>';
        $("#game-container").html(canv);
        board = document.getElementById('board');   
        var width = board.width;
        var height = board.height;
        var context = board.getContext('2d');

        var img = new Image();
        img.onload = function() {
            context.drawImage(img, 0, 0, width, height);
            paintPieces(boardState);
        }
        img.src = 'static/tictactoe-board.png';
    } else {
        paintPieces(boardState);
    }

}

function paintPieces(boardState) {
    var len = 3;
    for (var x = 0; x < len; ++x) {
        for (var y = 0; y < len; ++y) {
            if (boardState[x][y] == 'o') {
                paintPiece(x, y, 'o');
            } else if (boardState[x][y] == 'x') {
                paintPiece(x, y, 'x');
            }
        }
    }
}

function paintPiece(x, y, piece) {
    var board = document.getElementById('board');
    var width = board.width;
    var height = board.height;
    var context = board.getContext('2d');

    var offsetX = 25;
    var offsetY = 25;
    var beginX = x * (width / 3) + offsetX;
    var beginY = y * (height / 3) + offsetY;

    var img = new Image();
    img.onload = function() {
        context.drawImage(img, beginX, beginY, 125, 125);
    }
    if (piece == 'x')
        img.src = 'static/tictactoe-x.png';
    else
        img.src = 'static/tictactoe-o.png';
}
