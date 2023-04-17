import jwt

the_jwt = jwt.encode({"name":"Andreas","last_name":"Hansen"}, "the secret",algorithm="HS256")
# print(the_jwt)

# jwt.decode(the_jwt, "the secret", algorithms=["HS256"])

# print(jwt.decode(the_jwt, "the secret", algorithms=["HS256"]))

try:
    jwt.decode(the_jwt, "the secret", algorithms=["HS256"])
    print(jwt.decode(the_jwt, "the secret", algorithms=["HS256"]))
except Exception as ex:
    print("Sorry we cannot verify you, probably wrong secret")



# response.set_cookie("user", user_jwt, secret=x.COOKIE_SECRET)