FROM python:3.7.3-slim-stretch

WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip==19.0.3 && \
    pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile
