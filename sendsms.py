from bottle import post, request, response

@post("/api-sendsms")
# _____-
@post
def_

import requests
print("ok")
user_api_key =
sms_message =
sms_to_phone = " 50504417"


payload = {"user_api_key":user_api_key,
           "sms_message":sms_message,
           "sms_to_phone":sms_to_phone}

res = requests.post("https://smses.eu.pythonanywhere.com/api-sendsms", data=payload)

print(res)
print(res.text)