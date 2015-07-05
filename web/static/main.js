var mainHtml = '';

function setUpMainMenu() {
    $('.game-link').click(function() {
        mainHtml = $('#main').html();
        var gameName = $(this).text();
        var gameTitle = '<h2>' + gameName + '</h2>';
        var backToMain = "\
        <div id='home-menu'> \
            <a id='main-link' onclick='javascript: loadMainMenu()'>Main Menu<\a> \
        </div>";
        var gameMenu = '\
        <div id="game-container"> \
            <a id="newGame" onclick="javascript: loadNewGame()">New Random Game<\a> \
        </div>';
        $('#main').html(backToMain + gameTitle + gameMenu);
    });
}

$(document).ready(setUpMainMenu);

function loadMainMenu() {
    $('#main').html(mainHtml);
    setUpMainMenu()
}

function loadNewGame() {
    canv = '\
    <div id="gameCanvasContainer" text-align="center"> \
        <canvas width="600" height="600" id="board" onclick="javascript: clickHandler(event);"></canvas> \
    </div>'
    $("#game-container").html(canv)
    createGame();
}

function createGame() {
    $.post('api/create', function(data) {
        updateBoard();
    });
}

function updateBoard() {
    $.get('api/state', function(data) {
        data = JSON.parse(data);
        paintBoard(data['board']);
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
        update_json: JSON.stringify({
            square: [x, y]
        })
    };
    $.post('api/update', postData, function(data) {
        updateBoard();
    });
}

function paintBoard(boardState) {
    var board = document.getElementById('board');
    var width = board.width;
    var height = board.height;
    var context = board.getContext('2d');

    var img = new Image();
    img.onload = function() {
        context.drawImage(img, 0, 0, 600, 600);
        var len = 3;
        for (var x = 0; x < len; ++x) {
            for (var y = 0; y < len; ++y) {
                if (boardState[x][y] == 'y') {
                    paintPiece(x, y, 'o');
                } else if (boardState[x][y] == 'x') {
                    paintPiece(x, y, 'x');
                }
            }
        }
    }
    img.src = 'static/tictactoe-board.png';
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
