from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse

app = FastAPI(title="MLOps Service")

# TODO 1: Create GET /health that returns JSON like {"status": "ok"}
@app.get('/health')
def health():
    return {'status':'ok'}

@app.head('/health')
def health_head():
    return Response(status_code=status.HTTP_200_OK)

# TODO 2: Create GET /hello that returns an HTML page using HTMLResponse
@app.get("/hello", response_class=HTMLResponse)
def hello():
    return """<!doctype html>
                <html>
                <head><title>MLOps Lab 1</title></head>
                    <body>
                        <h1>Hello there!</h1>
                        <h1>General Kenobi!! GUAHH *Cough* *Cough*</h1>
                            <p>A legendary battle ensures</p>
                    </body>
                </html>
"""