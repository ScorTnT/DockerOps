# Docker build
```
docker build -t jekyll-blog -f .\Dockerfile {project-path}
```
ScorTnT : `C:\_VsCode\git.Blog`
# Docker run
```
docker run -d -p 4000:4000 -v ${PWD}:/git.Blog --name jekyll-blog jekyll-blog
```