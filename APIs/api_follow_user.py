from bottle import post, request, response
import x

@post("/follow-user")
def _():
	try:
		# get user from cookie
		user_cookie = request.get_cookie("user_cookie", secret="my-secret")
		user_obj = {} if not user_cookie else user_cookie


		# get user id from the user from the cookie
		user_obj.get("user_id")

		# Validate the followeer's id
		# validate(user_obj.get("user_id"))

		# Connect to the database
		db = x.db()

		# Insert into followers table
		user_followee_id = request.forms.get("user_followee_id")
		
		if request.forms.get("followInput") == "unfollow":
			info = f"You unfollowed user with id: {user_followee_id}"
			db.execute("UPDATE users SET user_total_followers = user_total_followers - 1 WHERE user_id = ?",(user_followee_id,))

		else:
			info = f"You are following user with id: {user_followee_id}"
			db.execute("UPDATE users SET user_total_followers = user_total_followers + 1 WHERE user_id = ?",(user_followee_id,))

		db.commit()
		print(info)  # Print the info text to the console
        
		return {"info": info}  # Return the info as the response body
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
		if "db" in locals(): db.close()