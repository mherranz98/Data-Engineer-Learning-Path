<a name="build-image"></a>

## **Containerized Environment**

For this case, the docker compose consists of Nifi, Kafka, both database images along with their respective UIs, and finally a Python image that will be created using a Dockerfile. Python directory is stored in the local machine but by means of a volume it is mapped to the Python container. We will need to access the Python container image CLI to execute the python main script.
For that reason, we will need to use the internal address for connecting the Python container with the Kafka one as they both reside in the same Docker host. The host:port pair for connecting the Python client (host machine) to Kafka broker (Docker host) is kafka:9092, because _kafka_ is the name of the Kafka service host (container name in Docker), and 9092 is the internal port exposed by Kafka to access their brokers.

For building our own Python image, we will design it taking into consideration the layered architecture of Docker images. The first command in the Dockerfile is the FROM, which states the base image that will be used to start the build process. In our case, this will be a Python image.
Then a WORKDIR statement is used to define the directory that will be used from the base image to work from. Once in the directory, a set of commands are executed by means of a RUN statement. Finally, we need to write in the CMD statement the program that will be executed by default once the container is running. This will need to point to the main.py file of the working directory.

```docker
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

#COPY . .
#CMD ["python3", "script.py"]
```

Once the Dockerfile is designed, we need to build the image by means of a docker build command. This will take the image provided by Docker Hub and build our own from it with the requirements specified in the Dockerfile. To do so, we must execute the following command in the directory where the Dockerfile is stored:

```docker
docker build -t python-for-challenge2 .
```

This will create in our personal image repo, a customized image following the Dockerfile criteria. After the image is created, we need to recreate the compose by running the docker-compose up -d command. This will make the containers update given the changes made in the compose file.

```bash
py main.py
```
