from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
#Este es el endpoint
@app.get("/")
def get_list():
    return [1,2,3]

@app.get("/bienvenida", response_class =HTMLResponse)
def get_letras():
    return '''
            <h1>Hola mundo desde fastapi</h1> 
           '''

    
