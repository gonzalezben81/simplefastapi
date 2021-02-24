## simplefastapi

This is a simple fastapi you can get up and running via Docker. 

#### Build the Docker Image

```
docker build -t simplefastapi .
```

#### Run the Docker Image

```
docker run --rm -p 80:80 simplefastapi
```

#### Kill the Docker contain that is running

**Note: This will call all Docker containers that are currently running.**

```
docker kill $(docker ps -q)
```