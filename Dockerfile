FROM python:2.7-alpine
RUN apk add --no-cache docker

COPY . /tmp/dockerfactory

RUN pip install --no-cache-dir /tmp/dockerfactory && \
    rm -Rf /tmp/*

ENTRYPOINT ["dockerfactory"]