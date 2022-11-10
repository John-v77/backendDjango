
    $(document).on('submit', '#message-form', function(e){
        e.preventDefault()

        console.log('sending')
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
                // alert(response)
            }
        })
        document.getElementById('message').value = ''
    })