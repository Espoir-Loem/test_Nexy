from nexy import Params, useView,HTMLResponse

@Params(response_class=HTMLResponse)
def GET(page:int): 
    data = [
        {
            "name":f"Espoir {page}",
            "image":{"a":"c","b":"d"},
            "users":["Espoir","Force","Loemba","Packa"]
        },
        {
            "name":f"Espoir {page}",
            "image":{"a":"e","b":"f"},
            "users":["Espoir","Force","Loemba","Packa"]
        }
    ]
    return "Espoir" #useView(path="index.html")

def PUT():
    return "ok page"


    