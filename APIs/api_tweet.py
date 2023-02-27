from bottle import post, request, response
import x
import uuid
import time

@post("/tweet")
def _():
    try:
        x.validate_tweet()
        db = x.db()
        # tweet_id = str(uuid.uuid4()).replace("-","")
        tweet_id = str(uuid.uuid4().hex)
        tweet_message = request.forms.get("message")
        tweet_image = ""
        tweet_created_at = int(time.time())
        tweet_user_fk = "51602a9f7d82472b90ed1091248f6cb1"
        tweet_total_comments = ""
        tweet_total_retweets = ""
        tweet_total_likes = ""
        tweet_total_dislikes = ""
        tweet_total_views = ""
        db.execute("INSERT INTO tweets VALUES(?,?,?,?,?,?,?,?,?,?)", (tweet_id, tweet_message, tweet_image, tweet_created_at,tweet_user_fk, tweet_total_comments, tweet_total_retweets, tweet_total_likes, tweet_total_dislikes,tweet_total_views))
        db.commit()
        return "ok"
    except Exception as ex:
        response.status = 400
        print(ex)
    finally:
        if "db" in locals(): db.close()
