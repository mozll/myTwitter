from bottle import post, request, response
import x

@post('/reset-password')
def _():
    try: ## Useren med 'denne reset key' skal have ændret sit password til denne værdi, fra en form
        # user_new_password = x.validate_new_password()
        # print(user_new_password)
        user_new_password = request.forms.user_new_password
        user_password_reset_key = request.forms.user_password_reset_key
        print(user_password_reset_key)

        db = x.db()
        rows_affected = db.execute(f"""
        UPDATE users
        SET user_password = ?
        WHERE user_password_reset_key = ?
        """,(user_new_password, user_password_reset_key))
        
        if not rows_affected: raise Exception(400, "invalid info")
        db.commit()

        return {'info':'Ok, password should be changed now'}
    

    except Exception as ex:
        print(ex)
        if 'db' in locals(): db.rollback()
        try: # Controlled exception, usually coming from the x file
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except: # Something unknown went wrong		
			# unknown scenario
            response.status = 500
            return {"info":str(ex)}
        
    finally:
        if 'db' in locals(): db.close()