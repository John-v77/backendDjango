// on load display message and query every 2 seconds
$(document).ready(function(){
    room_name = $('#room_name').val()
        setInterval(function(){
            $.ajax({
                type: 'GET',
                url: `/getMessages/${room_name}/`,
                success: function(response){
                    $("#display").empty();
                    for(let key in response.messages){
                        let temp="<div class='container darker'><b>"+response.messages[key].user+"</b><p>"+response.messages[key].value+"</p><span class='time-left'>"+response.messages[key].date+"</span></div>";
                        $("#display").append(temp);
                    }
                },
                error: function(response){
                    alert(`An error ocured: ${response}`)
                }
            })
        }, 2000)
    })


// on submit {message-form} add message to DB
$(document).on('submit', '#message-form', function(e){
    e.preventDefault()
    let csrftoken = '{{ csrf_token }}'

    $.ajax({
        type: "POST",
        headers:{'X-CSRFToken':csrftoken},
        url: '/send',
        data: {
                username:$('#username').val(),
                room_id:$('#room_id').val(),
                message:$('#message').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            },
        success: function (response) {
            console.log(response, typeof(response))
            alert(response)
        }
    })
    document.getElementById('message').value = ''
})