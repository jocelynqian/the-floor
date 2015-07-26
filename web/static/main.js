$.getScript("game.js");

var mainHtml = '';

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

// TODO(paul): Keep track of which view we are in (eg, menu, a game, etc) and 
//             have a function switch between them appropriately.
function loadMainMenu() {
    $('#main').html(mainHtml);
    setUpMainMenu();
}
