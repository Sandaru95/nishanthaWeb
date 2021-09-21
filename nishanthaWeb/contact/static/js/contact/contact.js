function sendMessage(e){
    // Default Prevention
    e.preventDefault();

    // References
    const conName = document.getElementById('con_name');
    const conPhone = document.getElementById('con_phone');
    const conMessage = document.getElementById('con_message');

    if (conName.value && conPhone.value && conMessage){
        // Posting data
        $.ajax({
            type: 'POST',
            url: '/contact/create_message/',
            data: { 
                'sender_name': conName.value, 
                'sender_tel': conPhone.value,
                'sender_message': conMessage.value,
                'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
            },
            success: function(resp){
                // Success Alert 
                Swal.fire({
                    position: 'top-end',
                    icon: 'success',
                    title: 'Message sent successfully',
                    showConfirmButton: false,
                    timer: 1000
                });
                // Clearing the Inputs
                conName.value = "";
                conPhone.value = "";
                conMessage.value = "";
            }
        });
    };
};