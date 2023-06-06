from bottle import post, request
import x

@post("/dislike-tweet-remove")
def _():
    try:
        db = x.db()
        tweet_dislike_removed = request.forms.get("tweet_id")
        
        db.execute("UPDATE tweets SET tweet_total_dislikes = tweet_total_dislikes - 1 WHERE tweet_id = ?",(tweet_dislike_removed,))
        
        db.commit()
        return {"info":"ok","tweet_dislike_removed":tweet_dislike_removed}
    except Exception as ex:
        print(ex)
        if "db" in locals(): db.rollback()
    finally:
        if "db" in locals(): db.close()