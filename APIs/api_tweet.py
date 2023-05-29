from bottle import post, request, response, get
import x
import uuid
import time

@post("/tweet")
def _():
    try:
        user_cookie = request.get_cookie("user_cookie", secret="my-secret")
        user_obj = {} if not user_cookie else user_cookie

        user_id = user_obj.get("user_id")

        x.validate_tweet()
        db = x.db()
        # tweet_id = str(uuid.uuid4()).replace("-","")
        tweet_id = str(uuid.uuid4().hex)
        tweet_message = request.forms.get("message")
        tweet_image = ""
        tweet_created_at = int(time.time())
        tweet_user_fk = user_id
        tweet_total_comments = ""
        tweet_total_retweets = ""
        tweet_total_likes = ""
        tweet_total_dislikes = ""
        tweet_total_views = ""
        db.execute("INSERT INTO tweets VALUES(?,?,?,?,?,?,?,?,?,?)", (tweet_id, tweet_message, tweet_image, tweet_created_at,tweet_user_fk, tweet_total_comments, tweet_total_retweets, tweet_total_likes, tweet_total_dislikes,tweet_total_views))
        db.commit()
        return {"info":"ok", "tweet_id":tweet_id,}
    except Exception as ex:
        response.status = 400
        return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()
