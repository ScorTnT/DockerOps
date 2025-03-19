# docker build 
docker build -t python:latest .

# docker run
docker run -itd --name python-latest -v ${PWD}:/app python-latest