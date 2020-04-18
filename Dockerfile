FROM tensorflow/tensorflow:2.1.0-gpu-py3

WORKDIR /tensortrade

SHELL ["/bin/bash", "-c"]
RUN apt-get update && apt-get install -yq --assume-yes --no-install-recommends \
  wget \
  zip \
  git \
  python3-pip \
  python3-dev \
  python3-setuptools

RUN pip install --upgrade pip

COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt

COPY ./examples/requirements.txt ./examples/requirements.txt
RUN pip install -r ./examples/requirements.txt

COPY ./tensortrade ./tensortrade
COPY ./tests ./tests
COPY ./docs ./docs
COPY ./examples ./examples
COPY ./setup.* ./
COPY ./README.md ./
COPY ./MANIFEST.in ./

RUN pip install -e .[tf,ccxt,stochastic,docs,tests]
