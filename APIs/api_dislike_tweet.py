from bottle import post, request
import x

@post('/dislike-tweet')
def _():
    try:
        db = x.db()
        tweet_disliked = request.forms.get("tweet_id")

        db.execute("UPDATE tweets SET tweet_total_dislikes = tweet_total_dislikes - 1 WHERE tweet_id = ?",(tweet_disliked,))

        db.commit()
        return {'info':'Ok', "tweet_disliked":tweet_disliked}
    except Exception as ex:
        print(ex)
        if 'db' in locals(): db.rollback()
    finally:
        if 'db' in locals(): db.close()