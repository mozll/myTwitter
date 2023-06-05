from bottle import post, request
import x


@post('/like-tweet-remove')
def _():
    try:
        x.db()
        return {'info':'Ok'}
    except Exception as ex:
        if 'db' in locals(): db.rollback()
        print(ex)
    finally:
        if 'db' in locals(): db.close()