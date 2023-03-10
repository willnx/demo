FROM nginx:1.23-alpine
RUN apk update && apk upgrade && mkdir -p /var/lib/nginx/
COPY static/ /var/lib/nginx/
COPY nginx.conf /etc/nginx/nginx.conf
COPY server.* /etc/ssl/
