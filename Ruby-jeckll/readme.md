# Docker build
```
docker build -t jekyll-blog .
```

# Docker run
```
docker run -d -p 4000:4000 -v ${PWD}:/app --name jekyll-blog jekyll-blog
```