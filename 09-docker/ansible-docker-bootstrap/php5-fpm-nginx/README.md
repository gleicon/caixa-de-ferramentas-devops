## Dockerfile for PHP5 applications
Contains php5-fpm and nginx.
Maps a local source to a docker's image /app through -v, listens at port 80

## Building
$ docker build -t php5-fpm-nginx .

## Running a simple application
$ docker run -d -p 80:80 -v /full/path/to/local/application/simple:/app php5-fpm-nginx

## Running wordpress
$ wget https://wordpress.org/latest.tar.gz
$ tar -zxvf latest.tar.gz
... edit wp-config.php stuff ...
$ docker run -d -p 80:80 -v /full/path/to/local/wordpress:/app php5-fpm-nginx

## Volumes
The volume /app might be mapped to the full path of the code from the host
