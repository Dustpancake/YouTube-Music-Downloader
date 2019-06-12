FROM alpine:3.7
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
    ffmpeg \
    git \
  && rm -rf /var/cache/apk/* \
  && mkdir /music /code && git clone https://github.com/minwook-shin/pytube && mv pytube/pytube ./code/ \
  && rm -rf pytube && ls -l && ls -l code
COPY src/dload.py /code/
ENTRYPOINT ["python", "/code/dload.py"]