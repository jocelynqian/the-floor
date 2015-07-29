function loadLog(){     

        var success = function(html) {
            $("#chat-box").html(html); //Insert chat log into the #chatbox div  
        };


        $.ajax({
            type: 'GET',
            url: 'api/messages',
            data: 'user_name=anon',
            cache: false,
            success: success,
        });
    }




$(document).ready(function(){
    setInterval(loadLog, 2500);
});