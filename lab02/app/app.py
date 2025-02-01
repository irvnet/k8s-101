from fastapi import FastAPI, Request
import uvicorn
import signal
import sys
from datetime import datetime

app = FastAPI()

# Request Handler
@app.get("/")
async def read_root(request: Request):
    print(f"[{datetime.now().isoformat()}] Received request for URL: {request.url}")
    return {"message": "Hi Python!!"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, log_level="info")
