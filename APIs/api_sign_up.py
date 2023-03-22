
from bottle import post, request, response
import uuid
import x
import time
import sqlite3
import pathlib
import bcrypt

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
        # user_avatar = str(uuid.uuid4()).replace("-","")
        # user_cover_image = str(uuid.uuid4()).replace("-","")
        # db = x.db()
        user_first_name = request.forms.get("user_first_name")
        user_last_name = request.forms.get("user_last_name")
        user_email = request.forms.get("user_email")
        user_password = request.forms.get("user_password").encode("utf-8")
        # print(f"user_name: {user_name}, user_password: {user_password}") 

        user = {
            "user_id":user_id,
            "user_name":user_name,
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "user_email": user_email,
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
            "user_password": bcrypt.hashpw(user_password, salt)
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

        response.status = 303
        response.set_header("Location", "/login")

        return "Sign-up successful"

    except Exception as ex:
        # print(f"Exception: {ex}")
        response.status = 303
        response.set_header("Location", "/sign-up")
        return {"info":str(ex)} # cast to string

    finally:
        if "db" in locals(): db.close()