from bottle import post, request, response
import x

@post('/deactivate-user')
def _():
    try:
        user_deactivation_key = request.forms.get("user_deactivation_key")
        print(user_deactivation_key)

        db = x.db()
        rows_affected = db.execute(f"""
        UPDATE users
        SET user_active = ?
        WHERE user_deactivation_key = ?
        """,(0,user_deactivation_key))

        if not rows_affected: raise Exception(400, "invalid info")

        db.commit()

        
        return {'info':'You have been deactivated'}
    except Exception as ex:
        if 'db' in locals(): db.rollback()
        print(ex)
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
    finally:
        if 'db' in locals(): db.close()