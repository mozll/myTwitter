from bottle import post, request, response
import x

@post('/goldify-user')
def _():
    try:
        user_gold_key = request.forms.get("user_gold_key")
        print(user_gold_key)

        db = x.db()
        rows_affected = db.execute(f"""
        UPDATE users
        SET user_gold = ?
        WHERE user_gold_key = ?
        """,(1,user_gold_key))

        if not rows_affected: raise Exception(400, "invalid info")

        db.commit()

        
        return {'info':'You are now a gold user'}
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