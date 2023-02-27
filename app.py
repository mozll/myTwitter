## 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  TOKEN FROM GITHUB


# https://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@github.com/mozll/myTwitter.git

from bottle import default_app, get, template, run, view, post, static_file, response, request
import sqlite3
import pathlib
import git
import x


# This data will come from the database
# For now, we just hard coded the data
# 0 False 1 True
tweets = [
  { "verified":1, "image_name":"1.jpg", "fullname":"Elon Musk", "username":"elonmusk","message":"All things in moderation, especially content moderation", "total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},

  { "verified":0, "image_name":"2.jpg", "fullname":"Joe Biden", "username":"joebiden","message":"I am THE president","message_image":"73120ca128fb49f18a1585f929af42ad.jpg","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},

  { "verified":1, "image_name":"1.jpg", "fullname":"Elon Musk", "username":"elonmusk","message":"Surround your house with treadmills set to jogging speed to stop walking dead ur welcome","message_image":"FpR2F4kaEAAE9Xk.jpg", "total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  
  { "verified":1, "image_name":"4.png", "fullname":"Peter Rasmussen", "username":"dupreeh","message":"""2-1 vs @FNATIC and we’ve secured our spot in the Spodek! Very excited to be back! 🤝🏽❤️ 
  Hard time as T today! But we managed to pull through with some crucial rounds and some decent CT sides! 
  Room for improvement - one step at a time!""","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  
  { "verified":1, "image_name":"1.jpg", "fullname":"Elon Musk", "username":"elonmusk","message":"Don’t worry, just some of my 👽 🛸 friends of mine stopping by …", "total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},

  { "verified":1, "image_name":"1.jpg", "fullname":"Elon Musk", "username":"elonmusk","message":"","message_image":"Foaz7GYX0AU9unl.jpg","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
]

# list = array
# dictionary is {}. Think of it as JSON
# trends = [
#   {"title":"Gaming", "total_hash":5451},
#   {"title":"Counter-Strike", "total_hash":231},
#   {"title":"Movies", "total_hash":346},
#   {"title":"Coding", "total_hash":465},
# ]

########################
@get("/js/<filename>")
def _(filename):
  return static_file(filename, "js")
#########################

def get_trends():
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
    db.row_factory = dict_factory
    trends = db.execute("SELECT * FROM trends ORDER BY CAST (trend_total_tweets AS INTEGER) DESC").fetchall()
    return trends
  except Exception as ex:
    print(ex)
    return "error"
  finally:
    if "db" in locals(): db.close()

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################
@get("/")
def render_index():
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
    db.row_factory = dict_factory
    tweets = db.execute("SELECT * FROM tweets JOIN users ON tweet_user_fk = user_id ORDER BY tweet_created_at DESC").fetchall()
    
    # """ {'tweet_id': '485db3c60952420e9c4670bb8d3c5830', 'tweet_message': 'The cutest 😍', 'tweet_image': '', 'tweet_created_at': '1676655238', 'tweet_user_fk': 'f15e3f7afcf945e2bea6b4553f25fe75', 'user_id': 'f15e3f7afcf945e2bea6b4553f25fe75', 'user_name': 'rihanna', 'user_first_name': 'Rihanna', 'user_last_name': '', 'user_avatar': 'a22da1effb3d4f03a0f77f9aa8320203.jpg', 'user_created_at': '1676630057', 'user_total_tweets': '0', 'user_total_retweets': '0', 'user_total_comments': '0', 'user_total_likes': '0', 'user_total_dislikes': '0', 'user_total_followers': '0', 'user_total_following': '0'}  """

    return template("index", title="Twitter", tweets=tweets, trends=get_trends(), tweet_min_len=x.TWEET_MIN_LEN, tweet_max_len=x.TWEET_MAX_LEN)
  except Exception as ex:
    print(ex)
    return "error"
  finally:
    if "db" in locals(): db.close()



@get("/header")
def _():
  return template("header")

@get("/contact")
def _():
  return template("contact-us")  
@get("/about")
def _():
  return template("about-us")  


##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")

  ##############################
@get("/images/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./images")

##############################
@get("/images/<filename:re:.*\.jpg>")
def _(filename):
  return static_file(filename, root="./images")

##############################
@get("/images/<filename:re:.*\.jpeg>")
def _(filename):
  return static_file(filename, root="./images")

##############################
@get("/images/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./images")

##############################
@get("/thumbnails/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./thumbnails")

##############################
@get("/thumbnails/<filename:re:.*\.jpg>")
def _(filename):
  return static_file(filename, root="./thumbnails")

##############################
@get("/cover-image/<filename:re:.*\.jpg>")
def _(filename):
  return static_file(filename, root="./cover-image")

## TEST WITH NEW FOLDER NAME, IT WORKS

##############################
@get("/<username>")
# @view("profile")
def _(username):
  try:
    # db = sqlite3.connect("/home/fulldemo/mysite/twitter.db")
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
    db.row_factory = dict_factory
    user = db.execute("SELECT * FROM users WHERE user_name=? COLLATE NOCASE",(username,)).fetchall()[0]
    
    # Get the user's id
    user_id = user["user_id"]
    print("#"*30)
    print(f"user id:{user_id}")
    # With that id, look up/get the respectives tweets
    tweets = db.execute("SELECT * FROM tweets JOIN users ON tweet_user_fk = user_id WHERE user_id=? ORDER BY tweet_created_at DESC LIMIT 10", (user_id,)).fetchall()
    print("#"*30)
    print(tweets)
    print("#"*30)
    # pass the tweets to the view. Template it
    
    print(user) # {'id': '51602a9f7d82472b90ed1091248f6cb1', 'username': 'elonmusk', 'name': 'Elon', 'last_name': 'Musk', 'total_followers': '128900000', 'total_following': '177', 'total_tweets': '22700', 'avatar': '51602a9f7d82472b90ed1091248f6cb1.jpg'}
    return template("profile", user=user, trends=get_trends(), tweets=tweets)
  except Exception as ex:
    print(ex)
    return "error"
  finally:
    if "db" in locals(): db.close()

############################################################
# VIEWS
import views.tweet

############################################################
# APIs
import APIs.api_tweet


##############################
##############################

@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./myTwitter')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""

##############################


# Run in AWS
try:
  import production
  print("Server running on AWS")
  application = default_app()
# Run in local computer
except Exception as ex:
  print("Running local server")
  run(host="127.0.0.1", port=80, debug=True, reloader=True)
