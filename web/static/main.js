$.getScript("game.js");

var mainHtml = '';
var username = null;

function setUpMainMenu() {
    $('.game-link').click(function() {
        mainHtml = $('#main').html();
        var gameLabel = $(this).text();
        var gameName = $(this).attr('gameName')
        var gameTitle = '<h2>' + gameLabel + '</h2>';
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

function getUsernameAndLogin() {
    var name = window.prompt("Enter your username:", "");
    if (name != null) {
        var data = {
            name: name,
        };
        var success = function(data) {
            username = name;
            setUpLogin();
        };

        var error = function(xhr, textStatus, errorThrown) {
            if (xhr.status == 400) {
                alert('Invalid user name!');
            }
        };

        $.ajax({
            type: "POST",
            url: 'api/login',
            data: data,
            success: success,
            error: error,
        });
    }
}

function setUpLogin() {
    var getUsernameLink = '<a class="link" onclick="javascript: getUsernameAndLogin();">Set your username</a>';
    var userInfo = getUsernameLink;
    if (username != null) {
        userInfo = 'Hi ' + username + '!';
    }

    $('#user-info-container').html(userInfo);
}

function onloadSetUp() {
    setUpMainMenu();
    setUpLogin();
}

$(document).ready(onloadSetUp);

// TODO(paul): Keep track of which view we are in (eg, menu, a game, etc) and
//             have a function switch between them appropriately.
function loadMainMenu() {
    $('#main').html(mainHtml);
    setUpMainMenu();
}
