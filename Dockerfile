FROM alpine:3.17
RUN apk update && apk upgrade && apk add python3 python3-dev build-base linux-headers py3-pip

COPY ./dist/*.whl .
RUN pip install ./*.whl
WORKDIR /usr/lib/python3.10/site-packages/demo
CMD gunicorn -c config.py demo:app
