FROM python:3.11-slim-buster
LABEL authors="lyapin"

RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:ubuntugis/ppa \
    && apt-get install -y libgeos++-dev \
    && apt-get install -y proj-bin \
    && apt-get install -y gdal-bin \
    && apt-get install -y libgdal-dev

WORKDIR /

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip  \
    && pip install --no-cache-dir -r ./requirements.txt

COPY . .
