FROM nginx:1.23-alpine
RUN apk update && apk upgrade && mkdir -p /var/lib/nginx/static/
COPY static/ /var/lib/nginx/static/
COPY nginx.conf /etc/nginx/nginx.conf
COPY server.* /etc/ssl/
