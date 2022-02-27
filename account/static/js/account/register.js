magic_number = undefined;
form_data = {}
function registerBtnClickHandler(e){
    // References
    let registerContentDiv = document.getElementById('register-content-div');
    // Prevent the default event from happening
    e.preventDefault();
    // Saving the Form Data
    form_data['username'] = document.getElementById('id_username').value;
    form_data['email'] = document.getElementById('id_email').value;
    form_data['password1'] = document.getElementById('id_password1').value;
    form_data['password2'] = document.getElementById('id_password2').value;
    form_data['g-recaptcha-response'] = "asd";
    form_data['csrfmiddlewaretoken'] = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    // Setting the 'Enter Verification Code Tab'
    $.ajax({ 
        type: 'POST', 
        url: '/account/register/verification/', 
        data: {
            'username': form_data['username'],
            'email': form_data['email'],
            'csrfmiddlewaretoken': form_data['csrfmiddlewaretoken'],
        },
        success: function(resp){
            magic_number = Number(resp);
            console.log({ magic_number })
            registerContentDiv.innerHTML = `
                <div class='container'>
                    <div class='row'>
                        <input type="text" name="username" placeholder='Enter the code here' id='verify_input' autofocus required >

                        <button onclick='checkVerify()' class="btn btn-primary">Verify</button>
                    </div>
                </div>
            `
        }
    });
};

function checkVerify(){
    // references
    let verifyInput = document.getElementById('verify_input');

    if (Number(verifyInput.value) == Number(magic_number)){
        $.ajax({ 
            type: 'POST', 
            url: '/account/register/',
            data: form_data,
            success: function(resp){
                Swal.fire({
                    position: 'top-end',
                    icon: 'success',
                    title: 'Account Created',
                    showConfirmButton: false,
                    timer: 1000
                });
                setTimeout(() => window.location.href = "/account/login/", 2000);
            },
        });
    }else{
        alert("verification failed!");
    };
};