from bottle import post, request, response

@post("/follow-user")
def _():
	try:
		# TODO: get user from cookie
		# user = request.get_cookie("user", secret="XXXXXXXX")
		user_cookie = request.get_cookie("user_cookie", secret="my-secret")
		user_obj = {} if not user_cookie else user_cookie
		# TODO: get user id from the user from the cookie
		# TODO: Validate the followeer's id
		# TODO: Connect to the database
		# TODO: Insert into followers table
		user_followee_id = request.forms.get("user_followee_id", "")

		if "unfollow" in request.forms:
			info = f"You unfollowed user with id: {user_followee_id}"
		else:
			info = f"You followed user with id: {user_followee_id}"
        
		print(info)  # Print the info text to the console
        
		return {"info": info}  # Return the info as the response body
	except Exception as e:
		print(e)
		pass
	finally:
		pass