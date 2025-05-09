# PLEASE CHECKING YOUR WORKING PATH !!
`WIN/MAC PATH : ~\Vite`

# docker build
```
docker build -f ~\Vite -t vite {project-path}
```

# docker run
```
docker run -it -d --name vite-real-time-container -v "{project-path}:/app" -p 5173:5173 vite
```