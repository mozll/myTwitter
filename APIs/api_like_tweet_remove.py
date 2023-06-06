from bottle import post, request
import x

@post('/like-tweet-remove')
def _():
    try:
        db = x.db()
        tweet_like_removed = request.forms.get("tweet_id")

        db.execute("UPDATE tweets SET tweet_total_likes = tweet_total_likes - 1 WHERE tweet_id = ?",(tweet_like_removed,))
        
        db.commit()
        return {'info':'Ok',"tweet_like_removed":tweet_like_removed}
    except Exception as ex:
        print(ex)
        if 'db' in locals(): db.rollback()
    finally:
        if 'db' in locals(): db.close()