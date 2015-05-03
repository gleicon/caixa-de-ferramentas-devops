FROM ubuntu:14.04
RUN apt-get update && apt-get -y install php5-fpm php-config php5-mysql nginx
ADD default /etc/nginx/sites-available/default
CMD /etc/init.d/nginx start && php5-fpm -F
