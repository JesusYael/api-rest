from fastapi import FastAPI

app = FastAPI()

@app.get("/nombre")
def read_root():
    nombre = 'Jesus Yael'
    # Devolvemos un diccionario para que FastAPI lo convierta en JSON automáticamente
    return {"nombre": nombre}
