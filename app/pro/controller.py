from nexy import Params, useView,HTMLResponse


@Params(response_class=HTMLResponse)
def GET(): 
    return useView(
        {
            "name":"Force",
            "image":{"a":"b","b":"a"},
            "users":["Espoir","Force","Loemba","Packa"]
        }
        ,"index.html")



    