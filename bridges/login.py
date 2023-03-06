from bottle import post, response
import time

@post("/login")
def _():
    # Redirection
    
    # Status code

    # The redirected page

    user = {
        "user_name":"mozel",
        "user_first_name": "Andreas",
        "user_last_name":"Hansen"
    }


    # cookie_expiration_date = int(time.time()) + 7200
    response.set_cookie("user_cookie", user, secret="my-secret", httponly=True)
    response.status = 303
    response.set_header("Location", "/")

    return "This is the bridge" 