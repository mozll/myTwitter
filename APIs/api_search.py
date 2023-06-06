from bottle import post, response
import json
import x

@post('/search')
def _():
    try:
        db = x.db()

        db.execute("")
        response.set_header("content-type", "application/json");
        return json.dumps[{"Name":"A"},{"name":"B"}]
    except Exception as ex:
        print(ex)
        if "db" in locals(): db.rollback()
    finally:
        if "db" in locals(): db.close()