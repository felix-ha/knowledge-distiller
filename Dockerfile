FROM python:3.10-slim

RUN apt-get update

WORKDIR /app
COPY requirements.txt requirements-dev.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements-dev.txt

COPY . . 

ENV PYTHONPATH=".:src/"
RUN pytest

RUN python -m pip install -e .
RUN python -m kdistiller "Hello World!"

RUN chmod +x ./bin/release.sh
RUN chmod +x ./bin/release_testpypi.sh
RUN chmod +x ./bin/release_pypi.sh
