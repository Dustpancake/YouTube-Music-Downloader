# YouTube-Music-Downloader
Dockerized command line tool for downloading and extracting audio from YouTube URLs.

Download to folder and build image simply with:
```
docker build -t {IMG_NAME} .
```
To use, docker requires a shared volume with the host machine to save the .wav file - I have named the shared folder in the container '/music'. As such, example execution:
```
docker run -v {PATH_TO_HOST_FOLDER}:/music {IMG_NAME} {YOUTUBE_URL}
```
