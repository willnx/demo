FROM postgres:15.2-alpine
RUN apk update && apk upgrade
COPY postgresql.conf /etc/postgresql/
COPY tables/* /docker-entrypoint-initdb.d/
