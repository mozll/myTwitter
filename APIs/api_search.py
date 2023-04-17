from bottle import post, response
import json


@post('/search')
def _():
    try:
        response.set_header("content-type", "application/json");
        return json.dumps[{"Name":"A"},{"name":"B"}]
    except Exception as ex:
        pass
    finally:
        pass