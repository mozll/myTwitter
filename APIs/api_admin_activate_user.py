from bottle import post, request, response
import x

@post('/admin-activate-user')
def _():
    try:
        db = x.db()
        user_id = request.forms.get("user_id")
        db.execute("UPDATE users SET user_active = 1 WHERE user_id = ?", (user_id,))
        db.commit()

        return {'info':'Ok'}
    except Exception as ex:
        response.status = 400
        print(ex)
        if 'db' in locals(): db.rollback()
    finally:
        if 'db' in locals(): db.close()


