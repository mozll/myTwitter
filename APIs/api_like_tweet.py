from bottle import post, request, response
import x

@post("/like-tweet")
def _():
    try:
        user_cookie = request.get_cookie("user_cookie", secret="my-secret")
        user_obj = {} if not user_cookie else user_cookie

        db = x.db()
        tweet_liked_id = request.forms.get("tweet_id")

        db.execute("UPDATE tweets SET tweet_total_likes = tweet_total_likes + 1 WHERE tweet_id = ?",(tweet_liked_id,))
        db.commit()

        return {"info":"ok","tweet_liked_id":tweet_liked_id}
    except Exception as ex:
        if "db" in locals: db.rollback()
        print(ex)
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()

