FROM python:latest

WORKDIR /app

ENTRYPOINT ["bash", "-c", "cp /path/${0} . && python3 ${0}"]

# run the container
# docker build -t python .
# docker run --rm -v ${PWD}:/path python python_script.py