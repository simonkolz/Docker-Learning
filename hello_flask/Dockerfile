#FROM python:3.8-slim
#
#WORKDIR /app
#COPY . .

# Install system dependencies needed to build mysqlclient
#RUN apt-get update && apt-get install -y \
 #   pkg-config \
  #  default-libmysqlclient-dev \
   # build-essential \
 #&& pip install --no-cache-dir flask mysqlclient \
 #&& apt-get clean \
 #&& rm -rf /var/lib/apt/lists/*

#EXPOSE 5000
#CMD ["python", "app.py"]





#Stage 1: Build stage
FROM python:3.8-slim as build

WORKDIR /app

RUN apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
 && pip install --no-cache-dir flask mysqlclient \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

 COPY . .


 #Stage 2: Production stage

 FROM python:3.8-slim

 WORKDIR /app

 COPY --from=Build /app /app

 EXPOSE 5000

 CMD ["python", "app.py"]