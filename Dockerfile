FROM python:3.10-slim

RUN apt-get update

WORKDIR /app
COPY . . 

RUN pip install --upgrade pip
RUN pip install -r requirements-dev.txt

RUN flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
RUN flake8 . --count --max-complexity=10 --max-line-length=127 --statistics

ENV PYTHONPATH=".:src/"
RUN pytest

RUN python -m pip install -e .
RUN python -m kdistiller "Hello World!"

RUN chmod +x ./bin/release.sh
RUN chmod +x ./bin/release_testpypi.sh
RUN chmod +x ./bin/release_pypi.sh
