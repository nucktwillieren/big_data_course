FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY my_nginx.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/my_nginx.conf /etc/nginx/sites-enabled/
RUN mkdir /etc/nginx/ssl/
RUN mkdir -p /var/www/html/
RUN mkdir -p /etc/letsencrypt/live/
RUN apt update
RUN apt install -y nano 
RUN apt install -y software-properties-common
# RUN add-apt-repository ppa:certbot/certbot
# RUN apt-get update
# RUN apt-get install -y certbot python-certbot-nginx
# RUN mkdir -p /etc/nginx/sites-enabled/\
#     && ln -s /etc/nginx/sites-available/my_nginx.conf /etc/nginx/sites-enabled/\
#     && rm /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
