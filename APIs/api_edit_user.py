from bottle import post, request, response
import x


@post("/edit-user")
def _():
    try:
        # user_gold_key = str(uuid.uuid4()).replace("-","")
        # user_gold_key = str(shortuuid.ShortUUID().random(length=6))
        user_cookie = request.get_cookie("user_cookie", secret="my-secret")
        user_obj = {} if not user_cookie else user_cookie

        db = x.db()
        print("#######################################")
        print(user_obj.get("user_name"))
        # print(user_obj.get("user_first_name"))
        # print(user_obj.get("user_last_name"))
        # print(user_obj.get("user_email"))
        print("#######################################")

        user_name = request.forms.get("user_name")
        print("I got the user_name")
        user_first_name = request.forms.get("user_first_name")
        user_last_name = request.forms.get("user_last_name")
        user_email = request.forms.get("user_email")
        
        # user_first_name = request.forms.get("user_first_name")
        # print("I got the first_name")

        user_updated = db.execute(f"""
            UPDATE users
            SET user_name = ?, user_first_name = ?, user_last_name = ?, user_email = ?
            WHERE user_id = ?
            """,(user_name, user_first_name, user_last_name, user_email, user_obj.get("user_id"))).rowcount
        

        # user_first_name_updated = db.execute(f"""
        #     UPDATE users
        #     SET user_first_name = ?
        #     WHERE user_email = ?
        #     """,(user_first_name, user_obj.get("user_email"))).rowcount
        
        print("TESTe")

        # if not user_name_updated or user_first_name_updated: raise Exception(400,"something went wrong, try writing in a field")
        if not user_updated: raise Exception(400,"something went wrong, try writing in a field")

        user = db.execute("SELECT * FROM users WHERE user_email = ? LIMIT 1", (user_email,)).fetchone()

        user_obj = {
            "user_id":user["user_id"],
            "user_name":user["user_name"],
            "user_first_name":user["user_first_name"],
            "user_last_name":user["user_last_name"],
            "user_email":user["user_email"],
            "user_avatar":user["user_avatar"]
            }

            # Set cookie and redirect to home page
        response.set_cookie("user_cookie", user_obj, secret="my-secret", httponly=True)
        response.status = 303
        response.set_header("Location", "/")

        db.commit()


        response.status = 303
        response.set_header("Location", "/")

        return {
            "info" : "Your change has been made"
        }

    except Exception as ex:
        if 'db' in locals(): db.rollback()
        print(ex)
    finally:
        if 'db' in locals(): db.close()