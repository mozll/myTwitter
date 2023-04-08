from bottle import post, response, request
import uuid
import x
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

@post('/send-gold-key')
def _():
    try:
        user_gold_key = str(uuid.uuid4()).replace("-","")
        user_cookie = request.get_cookie("user_cookie", secret="my-secret")
        user_obj = {} if not user_cookie else user_cookie

        db = x.db()
        print("#######################################")
        print(user_obj.get("user_email"))
        
        rows_affected = db.execute(f"""
            UPDATE users
            SET user_gold_key = ?
            WHERE user_email = ?
            """,(user_gold_key, user_obj.get("user_email"))).rowcount
        

        if not rows_affected: raise Exception(400,"user not found")

        db.commit()

        message = MIMEMultipart("alternative")
        message["Subject"] = "Deactivate your account"
        message["From"] = x.EMAIL_FROM
        message["To"] = user_obj.get("user_email")

        # Create the plain-text and HTML version of your message
        text = f"""\
        Hi,
        To deactivate your user, send a POST request to:
        https://mozel.eu.pythonanywhere.com/deactivate-user
        and use the deactivation key: {user_gold_key}
        """
        html = f"""\
        <html>
        <body>
            Hi,
            To deactivate your user, send a POST request to:
            https://mozel.eu.pythonanywhere.com/deactivate-user
            and use the deactivation key: {user_gold_key}
        </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(x.EMAIL_FROM, x.EMAIL_SECRET)
            server.sendmail(
                x.EMAIL_FROM, user_obj.get("user_email"), message.as_string()
            )

        response.status = 303
        response.set_header("Location", "/deactivate-user")

        return {
            "info" : "Check your email to deactivate your account"
        }

    except Exception as ex:
        if 'db' in locals(): db.rollback()
        print(ex)
    finally:
        if 'db' in locals(): db.close()