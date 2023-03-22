from bottle import post, request, response

@post('/api-reset-password')
def _():
    try:
        return {'info':'Ok'}
    except Exception as ex:
        if 'db' in locals(): db.rollback()
        print(ex)
    finally:
        if 'db' in locals(): db.close()