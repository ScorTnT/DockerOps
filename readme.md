# Docker build
`PWD : Dockerfile & requirements.txt folder` 
```
docker build -t yt-script .
```
# Docker run 
`PWD : python code - tensorflow`
```
docker run -it -d --name {container label~~} -v ${PWD}:/workspace yt-script
```