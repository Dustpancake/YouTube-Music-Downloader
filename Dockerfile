FROM alpine:3.7
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
    ffmpeg \
  && pip install pytube \
  && rm -rf /var/cache/apk/* \
  && mkdir /music /code
COPY src/dload.py /code/
ENTRYPOINT ["python", "/code/dload.py"]

