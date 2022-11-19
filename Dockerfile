##### building stage #####
FROM python:3.10

RUN apt-get update && apt-get install -y \
    unzip

# python package
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r  requirements.txt
RUN apt install -y docker.io docker-compose

WORKDIR /app