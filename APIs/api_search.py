from bottle import post, response, request, get
import json
import x

@get('/search')
def _():
    try:
        db = x.db()

        searchInput = request.query.get("searchInput")
        searchResults = db.execute("SELECT * FROM users_search WHERE user_name LIKE ?",(f'{searchInput}%',)).fetchall()

        print(searchInput,"searchinput ###")
        print(searchResults, "searchresult print")
        return {"info":"ok", "searchResults":searchResults }
    except Exception as ex:
        print(ex)
        if "db" in locals(): db.rollback()
    finally:
        if "db" in locals(): db.close()