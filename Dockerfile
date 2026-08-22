FROM arm64v8/python:3.11-slim

LABEL org.opencontainers.image.source="https://github.com/ducky4life/ugli-ferg"

COPY requirements.txt /

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ferg.py .env /

WORKDIR /

CMD [ "python", "ferg.py" ]
