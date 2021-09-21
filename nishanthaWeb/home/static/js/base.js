function addToNewsletter(e){
    // Default Prevention
    e.preventDefault();

    // References
    const email = e.target.parentElement.children[1];

    if (email.value){
        // Posting data
        $.ajax({
            type: 'POST',
            url: '/home/add_to_newsletters/',
            data: { 
                'email': email.value, 
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
                email.value = "";
            }
        });
    };
}