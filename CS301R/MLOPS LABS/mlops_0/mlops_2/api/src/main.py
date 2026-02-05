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
