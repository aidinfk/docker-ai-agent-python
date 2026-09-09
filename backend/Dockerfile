FROM python:latest

# host.docker.internal -> localhost
# curl -X POST -d '{"message": "hello world!"}' -H "Content-Type: application/json" http://localhost:8080/api/chats
RUN apt-get update && apt-get install -y curl

# create python virtual environment
# isolate our python app and installs from system-level python
RUN python -m venv /opt/venv/
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY ./src .

CMD ["python", "-m", "http.server", "8000"]
