
## Containerize a simple node.js process

In this section we'll create a simple node.js process and wrap it in a docker container.


1. create server.js using your preferred editor and add the following code:
```
  var http = require('http');

  var handleRequest = function(request, response) {
  console.log('Received request for URL: ' + request.url);
  response.writeHead(200);
  response.end('Hello World!');
  };
  var www = http.createServer(handleRequest);
  www.listen(8080);
```

2. Create Dockerfile and enter the following code

```
  FROM node:6.9.2
  EXPOSE 8080
  COPY server.js .
  CMD node server.js
```

3. Build the Docker image
```
$ docker build -t mynode:v1.0 .
```

4. Run the image and test it locally

```
$ docker run --rm -d -p 8080:8080 --name mynode-sample  mynode:v1.0
```

  For a quick test of the container running locally on your machine, In your browser, access http://localhost:8080.  

5. Stop the locally running container

```  
$ docker stop mynode-sample
```


---
