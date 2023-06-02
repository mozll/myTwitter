from bottle import post, request, response
import x

@post('/activate-user')
def _():
    try: ## Useren med 'denne reset key' skal have ændret sit password til denne værdi, fra en form
        # user_new_password = x.validate_new_password()

        user_activation_key = request.forms.get("user_activation_key")
        user_activation_key = user_activation_key.replace(" ","") ## removing extra spaces from input
        print(user_activation_key)

        db = x.db()
        rows_affected = db.execute(f"""
        UPDATE users
        SET user_active = ?
        WHERE user_activation_key = ?
        """,(1,user_activation_key))

        if not rows_affected: raise Exception(400, "invalid info")
        
        db.commit()


        response.status = 303
        response.set_header("Location", "/login")

        return {'info':'Ok, user should be active now'}
    
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