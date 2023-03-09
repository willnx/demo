FROM postgres:15.2-alpine
RUN apk update && apk upgrade
COPY tables/* /docker-entrypoint-initdb.d/
