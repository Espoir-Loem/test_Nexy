from fastapi import WebSocket, WebSocketDisconnect
from nexy import Params, useView,HTMLResponse

 
@Params(response_class=HTMLResponse)
def GET(slug:str):
    return useView(
        {
            "name":"Force",
            "image":{"a":slug,"b":"d"},
            
            "users":["Espoir","Force","Loemba","Packa"]
        }
        ,"index.html")


async def POST():
    return 12

async def SOCKET(app : WebSocket):
    await app.accept()

    try:
        while True:
            print("Client connecté")
            # Recevoir les messages du client
            data = await app.receive_text()
            # Envoyer une réponse au client
            await app.send_text(f"{data}")
    except WebSocketDisconnect:
        print("Client déconnecté")