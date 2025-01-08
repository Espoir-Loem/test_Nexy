from app.view import App
from nexy import Params, HTMLResponse

@Params(response_class=HTMLResponse)
def GET(): 
    return f"{App()}"
