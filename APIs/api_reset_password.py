from bottle import post, request, response

@post('/reset-password')
def _():
    try: ## Useren med 'denne reset key' skal have ændret sit password til denne værdi, fra en form
        return {'info':'Ok'}
    except Exception as ex:
        if 'db' in locals(): db.rollback()
        print(ex)
    finally:
        if 'db' in locals(): db.close()