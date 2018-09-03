FROM alpine:3.7
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
    ffmpeg \
  && pip install pytube \
  && rm -rf /var/cache/apk/* \
  && mkdir /music
COPY dload.py /
ENTRYPOINT ["python", "/dload.py"]

