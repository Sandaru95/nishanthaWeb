import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def py_mail(TO, USERNAME):
    SUBJECT = f"Hello {USERNAME}!, Thanks for Your Signup with Nishantha Book Store."
    FROM = "nishanthabookstore@gmail.com"
    BODY = f"""
    <html lang='en'>
        <head>
            <meta charset='UTF-8'>
            <meta http-equiv='X-UA-Compatible' content='IE=edge'>
            <title>Welcome</title>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU' crossorigin='anonymous'>
        </head>
        <body>
            <!-- Body Starts Here -->
            <img src='https://scontent.fcmb2-2.fna.fbcdn.net/v/t1.6435-9/206992949_1243155906141695_6350381019870034521_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=973b4a&_nc_ohc=bS8nsENc3pQAX_6fdqT&_nc_ht=scontent.fcmb2-2.fna&oh=4d98307a83849d12a910a96d2c034838&oe=616FCD27' style='width: 100%;'>
            <br>
            <br>
            <nav aria-label='breadcrumb'>
                <ol class='breadcrumb' style='margin-left: 2%;'>
                    <li class='breadcrumb-item'><a href='#' style='font-size: 22px'>Nishantha Book Store</a></li>
                    <li class='breadcrumb-item active' aria-current='page'  style='font-size: 22px'>Welcome</li>
                </ol>
            </nav>
            <!-- Card -->
            <div class='card' style='width: 79rem;'>
                <div class='card-body'>
                    <h5 class='card-title' style='font-size: 42px;color: mediumseagreen;padding-left: 20%'>Welcome, to Nishantha Book Store</h5>
                    <br>
                    <h1 class='card-text' style='font-size: 34px;'>Thanks for your sign up with Nishantha Book Store. Using our platform You can browse for more than 10000+ books. If you are looking for where to get started please proceed with the following links.</h1>
                    <br>
                    <br>
                    <button type='button' class='btn btn-warning' style="font-size: 28px;margin-left: 32%;">Visit Nishantha Bookstore</button>
                </div>
            </div>
            <!-- ./ Body Ends Here -->
            <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js' integrity='sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ' crossorigin='anonymous'></script>
        </body>
    </html>
    """

    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = FROM
    MESSAGE.preamble = """
    Your mail reader does not support the report format.
    Please visit us online!"""

    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)

    # The actual sending of the e-mail
    server = smtplib.SMTP('smtp.gmail.com:587')

    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)

    # Credentials (if needed) for sending the mail
    password = "Srilanka1234"

    server.starttls()
    server.login(FROM,password)
    server.sendmail(FROM, [TO], MESSAGE.as_string())
    server.quit()

def py_mail_verifycode(TO, USERNAME, verify_code):
    SUBJECT = f"Nishantha Book Store Verify Code: {str(verify_code)}"
    FROM = "nishanthabookstore@gmail.com"
    BODY = f"""
    <html lang='en'>
        <head>
            <meta charset='UTF-8'>
            <meta http-equiv='X-UA-Compatible' content='IE=edge'>
            <title>Welcome</title>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU' crossorigin='anonymous'>
        </head>
        <body>
            <!-- Card -->
            <div class='card' style='width: 79rem;'>
                <div class='card-body'>
                    <h1 class='card-text' style='font-size: 34px;'>Your Verification Code is {str(verify_code)}</h1>
                </div>
            </div>
            <!-- ./ Body Ends Here -->
            <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js' integrity='sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ' crossorigin='anonymous'></script>
        </body>
    </html>
    """

    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = FROM
    MESSAGE.preamble = """
    Your mail reader does not support the report format.
    Please visit us online!"""

    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)

    # The actual sending of the e-mail
    server = smtplib.SMTP('smtp.gmail.com:587')

    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)

    # Credentials (if needed) for sending the mail
    password = "Srilanka1234"

    server.starttls()
    server.login(FROM,password)
    server.sendmail(FROM, [TO], MESSAGE.as_string())
    server.quit()