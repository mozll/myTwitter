from bottle import post, request, response

@post("/api-follow")
def _():
	try:
		# TODO: get user from cookie
		# user = request.get_cookie("user", secret="XXXXXXXX")
		# TODO: get user id from the user from the cookie
		# TODO: Validate the followeer's id
		# TODO: Connect to the database
		# TODO: Insert into followers table
		user_followee_id = request.forms.get("user_followee_id", "")

		if "unfollow" in request.forms:
			return {"info": f"You unfollowed user with id: {user_followee_id}"}
		else:
			return {"info": f"You followed user with id: {user_followee_id}"}
	except Exception as e:
		print(e)
		pass
	finally:
		pass