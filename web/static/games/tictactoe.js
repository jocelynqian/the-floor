function TicTacToe() {
}
 
TicTacToe.clickHandler = function(e) {
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
        refreshState(gameName, gameId, playerId, false);
    });
}

TicTacToe.prototype.paintBoard = function(boardState) {
    var self = this;
    var board = document.getElementById('board');
    if (board == null) {
        var canv = '\
        <div id="gameCanvasContainer" text-align="center"> \
            <canvas width="600" height="600" id="board" onclick="javascript: TicTacToe.clickHandler(event);"></canvas> \
        </div>';
        $("#game-container").html(canv);
        board = document.getElementById('board');   
        var width = board.width;
        var height = board.height;
        var context = board.getContext('2d');

        var img = new Image();
        img.onload = function() {
            context.drawImage(img, 0, 0, width, height);
            self.paintPieces(boardState);
        }
        img.src = 'static/tictactoe-board.png';
    } else {
        self.paintPieces(boardState);
    }

}

TicTacToe.prototype.paintPieces = function(boardState) {
    var len = 3;
    for (var x = 0; x < len; ++x) {
        for (var y = 0; y < len; ++y) {
            if (boardState[x][y] == 'o') {
                this.paintPiece(x, y, 'o');
            } else if (boardState[x][y] == 'x') {
                this.paintPiece(x, y, 'x');
            }
        }
    }
}

TicTacToe.prototype.paintPiece = function(x, y, piece) {
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
