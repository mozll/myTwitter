from bottle import post, request
import x

@post('/delete-tweet')
def _():
    try:
        db = x.db()
        tweetDeleted = request.forms.get("tweet_id")

        db.execute("DELETE from tweets WHERE tweet_id = ?",(tweetDeleted,))

        db.commit()
        return {'info':'Ok',"Tweet deleted with id":tweetDeleted}
    except Exception as ex:
        if 'db' in locals(): db.rollback()
        print(ex)
    finally:
        if 'db' in locals(): db.close()