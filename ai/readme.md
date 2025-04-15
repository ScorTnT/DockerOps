# Docker build
`PWD : Dockerfile & requirements.txt folder` 
```
docker build -t tf-dev .
```
# Docker run 
`PWD : python code - tensorflow`
```
docker run -it -d --name {container label~~} -v ${PWD}:/workspace tf-dev
```