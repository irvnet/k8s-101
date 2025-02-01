
## Containerize a simple node.js process

In this section we'll create a simple Python microservice and wrap it in a docker container.


1. Create ./app/app.py using your preferred editor and add the following code:
```
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
    return {"message": "Hi Py!!"}

# Graceful Shutdown Handling
def graceful_shutdown(signal_num, frame):
    print("Shutting down gracefully...")
    sys.exit(0)

# Capture SIGINT and SIGTERM
signal.signal(signal.SIGINT, graceful_shutdown)
signal.signal(signal.SIGTERM, graceful_shutdown)

# Entry Point
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, log_level="info")
```

2. Create Dockerfile and enter the following code

```
FROM python:3.11-slim

WORKDIR /app
COPY ./app/app.py .
RUN pip install fastapi uvicorn
EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
```

3. Build the Docker image
```
docker build -t hipy:v1.0 .
```

4. Run the image and test it locally

```
docker run -d -p 8080:8080 --name sample00  hipy:v1.0
```

  For a quick test of the container running locally on your machine, In your browser, access http://localhost:8080.  

5. Multiple copies of the application can run at the same time

```
{
 docker run -d -p 8081:8080 --name sample01  hipy:v1.0
 docker run -d -p 8082:8080 --name sample02  hipy:v1.0

 docker ps
}
```


6. Create a custom index.html page and deploy it on nginx using a container volume
```
{ 
 mkdir content

 echo '<H1>Welcome to the Team A intranet site!</H1>' > content/index.html

 docker run --name teamA -d -p 90:80 -v $(pwd)/content:/usr/share/nginx/html nginx 
 curl localhost:90
}
```

7. get the container id to connect to the running container and see where the custom page is found
```
{
docker run --name teamA -d -p 90:80 -v $(pwd)/content:/usr/share/nginx/html nginx
docker exec -it $(docker ps -q --filter "name=nginx") /bin/sh
}
```

8. Review the custom index page in the container
```
{
ls -la /usr/share/nginx/html
cat /usr/share/nginx/html/index.html
}
```

9. Exit the container and cleanup

```  
{
docker stop $(docker ps -q)
docker rm $(docker ps -aq)
}
```


---
