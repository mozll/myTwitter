
from bottle import post, request, response
import uuid
import x
import time
import sqlite3
import pathlib
import bcrypt
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

salt = bcrypt.gensalt()

def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################

@post("/sign-up")
def _():
    try:
        ## Retrieve sign up form data
        user_id = str(uuid.uuid4()).replace("-","")
        user_name = x.validate_user_name()
        user_password = x.validate_user_password()
        # user_avatar = str(uuid.uuid4()).replace("-","")
        # user_cover_image = str(uuid.uuid4()).replace("-","")
        # db = x.db()
        user_first_name = request.forms.get("user_first_name")
        user_last_name = request.forms.get("user_last_name")
        user_email = x.validate_user_email()
        # user_email = request.forms.get("user_email")
        user_activation_key = str(uuid.uuid4()).replace("-","")
        user_deactivation_key = ""
        user_gold_key = ""
        user_password = request.forms.get("user_password").encode("utf-8")
        # print(f"user_name: {user_name}, user_password: {user_password}") 

        # https://website.dk/activationCode?={user_activation_code}

        user = {
            "user_id":user_id,
            "user_name":user_name,
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "user_email": user_email,
            "user_phone":"0",
            "user_avatar":"egg3442e1f6463624338504cd021bf23aef84411x.jpg",
            "user_cover_image":"3d41c7550f67429cb7590d62ab0eca2d.jpg",
            "user_created_at": int(time.time()),
            "user_total_tweets":"0",
            "user_total_retweets":"0", 
            "user_total_comments":"0",
            "user_total_likes":"0",
            "user_total_dislikes": "0",
            "user_total_followers": "0",
            "user_total_following": "0",
            "user_verified":"0",
            "user_active":"0",
            "user_activation_key":user_activation_key,
            "user_deactivation_key":user_deactivation_key,
            "user_gold":"0",
            "user_gold_key":user_gold_key,
            "user_password": bcrypt.hashpw(user_password, salt),
            "user_password_reset_key": ""
        }
        # print(user) 

        values = ""
        for key in user:
            values = values + f":{key},"
        values = values.rstrip(",")
        # print(values)

        # Connect to the SQLITE Database
        db = sqlite3.connect(str(pathlib.Path(__file__).resolve().parent.parent) + "/twitter.db")
        db.row_factory = dict_factory

        db.execute(f"INSERT INTO users VALUES({values})", user)
        # db.execute("INSERT INTO users VALUES(:user_id, :user_name)", user)
        # db.execute(f"INSERT INTO users VALUES({values})", user)

        db.commit()

        message = MIMEMultipart("alternative")
        message["Subject"] = "Activate your MyTwitter account"
        message["From"] = x.EMAIL_FROM
        message["To"] = user_email

        # Create the plain-text and HTML version of your message
        text = f"""\
        <html>
        <body>
            Hi, thank you for signing up.
            Before you can use your myTwitter account, you need to activate it at:
            https://mozel.eu.pythonanywhere.com/activate-user
            and use your activation key: {user_activation_key}
        </body>
		</html>
		"""
        html = f"""\
		<html>
		<body>
			Hi, thank you for signing up.
			Before you can use your myTwitter account, you need to activate it at:
			https://mozel.eu.pythonanywhere.com/activate-user
			and use your activation key: {user_activation_key}
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
                x.EMAIL_FROM, user_email, message.as_string()
            )

        response.status = 303
        response.set_header("Location", "/activate-user")

        return {
            "Sign-up successful - check your email for activation link"
        }

    except Exception as ex:
        print(ex)
        if "db" in locals(): db.rollback()
        
        try: # Controlled exception, usually coming from the x file
            response.status = ex.args[0]
            return {"info":ex.args[1]}

        except:
            response.status = 500
            return {"info":str(ex)}

    finally:
        if "db" in locals(): db.close()