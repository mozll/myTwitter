from bottle import post, response, request
import uuid
import x
import smtplib, ssl
# import shortuuid
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from twilio.rest import Client


@post('/send-gold-key')
def _():
    try:
        user_gold_key = str(uuid.uuid4()).replace("-","")
        # user_gold_key = str(shortuuid.ShortUUID().random(length=6))
        user_cookie = request.get_cookie("user_cookie", secret="my-secret")
        user_obj = {} if not user_cookie else user_cookie

        db = x.db()
        print("#######################################")
        print(user_obj.get("user_email"))
        
        account_sid = "ACecb93b361a8d0891f97586c794d8a025"
        account_token = "78e585b8a58662063c37122194c3f848"

        client = Client(account_sid, account_token)
        
        user_phone = request.forms.get("user_phone")
        print("##########TEST")
        message = client.messages.create(
        from_='+15075195097',
        body=f"""Hi,
        To golden your user, enter this key {user_gold_key}
        """,
        # media_url ="https://cdn.cnn.com/cnnnext/dam/assets/221208163103-20221208-twitter-verification-cost-light-super-tease.jpg"
        to=f"+45{user_phone}"
)

        

        print(message.sid)


        gold_key_updated = db.execute(f"""
            UPDATE users
            SET user_gold_key = ?
            WHERE user_email = ?
            """,(user_gold_key, user_obj.get("user_email"))).rowcount
        
        user_phone_updated = db.execute(f"""
            UPDATE users
            SET user_phone = ?
            WHERE user_email = ?
            """,(user_phone, user_obj.get("user_email"))).rowcount
        

        if not gold_key_updated & user_phone_updated: raise Exception(400,"user not found")

        db.commit()


        response.status = 303
        response.set_header("Location", "/goldify-user")

        return {
            "info" : "Check your phone to golden your account"
        }

    except Exception as ex:
        if 'db' in locals(): db.rollback()
        print(ex)
    finally:
        if 'db' in locals(): db.close()