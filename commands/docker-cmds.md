# Docker Command Line

## On Window containers with Experimental setting
```
docker version
docker info
```

## Lists all containers
```
docker container ls -a
docker ps
```

## Removes 1 or more containers
```
docker container rm abc
docker container rm def
docker container rm abc def
```

## Remove all containers (even running ones)
```
docker rm $(docker ps -aq) -f
```

## Create an nginx container
```
docker container run -it -p 80:80 nginx
```
* -it 
    * Interactive mode, runs in the foreground
* -p or --publish
* port1:port2
    * port1 == port on local machine
    * port2 == port that is exposed on container
* nginx 
    * name of image (for this example)

## See images, even if container was deleted
```
docker images
```

## Remove an image
```
docker image rm ***
```

## Pull an image down without creating container
```
docker pull ****
docker pull nginx
```

## Run nginx in background
```
docker container run -d -p 8080:80 --name mynginx nginx
```
* -d or --detach 
    * runs in the background

## Run apache in background
```
docker container run -d -p 8081:80 --name myapache httpd
```

## Run mysql in background
```
docker container run -d -p 3306:3306 --name mysql --env MYSQL_ROOT_PASSWORD=12345 mysql
```

## Stop a container
```
docker container stop ****
docker container stop mynginx
```

## Edit files in the nginx server
 Bash into the nginx container
```
docker container exec -it mynginx bash
```

## Bind mount
Map area on local machine to area on container
```
# linux
docker container run -d -p 8080:80 -v $(pwd):/usr/share/nginx/html --name nginx-website nginx

# windows
docker container run -d -p 8080:80 -v C:Users/leonl/Desktop/foobar:/usr/share/nginx/html --name nginx-website nginx
```