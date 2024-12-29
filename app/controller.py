
from nexy import Params, useView,HTMLResponse

@Params(response_class=HTMLResponse)
def GET(): 
    return useView(
        {
            "name":"Espoir",
            "image":{"a":"a","b":"b"},
            "users":["Espoir","Force","Loemba","Packa"]
        }
        ,"index.html")



    