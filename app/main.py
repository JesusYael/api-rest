from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()

@app.get("/nombre")
def read_root():
    nombre = 'Jesus Yael'
    return {"nombre": nombre}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Usa el puerto de Render o 8000 por defecto
    uvicorn.run(app, host="0.0.0.0", port=port)