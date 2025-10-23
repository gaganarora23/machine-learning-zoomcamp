from fastapi import FastAPI
import uvicorn


app = FastAPI(title="ping")

@app.get('/ping')
def ping():
    return 'PONG'

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=9696)

# Run this via python ping.py and access localhost:9696/ping