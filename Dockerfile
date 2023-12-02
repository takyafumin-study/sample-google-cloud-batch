FROM python:3.9.0-slim

ENV PYTHONUNBUFFERD True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ./requirements.txt ./requirements.txt
COPY ./src/* ./src/

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "/bin/bash", "./src/run.sh" ]

