from bottle import post, response, request, redirect, route
import time
import sqlite3
import pathlib
import json


def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

@post("/login")
def _():
    
    try:
        
        # Retrieve login form data
        user_name = request.forms.get("user_name")
        user_password = request.forms.get("user_password")
        print(f"user_name: {user_name}, user_password: {user_password}") 

        # Connect to the SQLITE Database
        db = sqlite3.connect(str(pathlib.Path(__file__).resolve().parent.parent) + "/twitter.db")
        db.row_factory = dict_factory

        user = db.execute("SELECT * FROM users WHERE user_name=? AND user_password=?", (user_name, user_password)).fetchone()
        print(f"user: {user}") 

        if user:
            # Create user object for the cookie
            user_obj = {
                "user_id":user["user_id"],
                "user_name":user["user_name"],
                "user_first_name":user["user_first_name"],
                "user_last_name":user["user_last_name"],
                "user_avatar":user["user_avatar"]
            }

            # Set cookie and redirect to home page
            response.set_cookie("user_cookie", user_obj, secret="my-secret", httponly=True)
            response.status = 303
            response.set_header("Location", "/")

            return "Login successful"
    
        else:
            response.status = 303
            response.set_header("Location","/login")
            return "invalid email or password"
    
    except Exception as ex:
        print(f"Exception: {ex}")
        response.status = 303
        response.set_header("Location", "/login")
        return "Invalid username or password"

    finally: 
        if "db" in locals(): db.close()