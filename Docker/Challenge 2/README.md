<br>
<br>

# **Challenge 2: Apache Kafka, Python and DBs 🐋🧑🏼‍💻**

---

The goal of this challenge is to familiarize yourself with Apache Kafka, an event streaming platform that enables us to handle real-time data feeds. We will go through the basics of its architecture and finally do some processing with a Python scripts. Resulting data will be pushed to databases, relational and non-relational.

In the [second part of the Challenge 1](../Challenge%201/README.md#readme-second), we were able to discover the power of Nifi as an streaming tool. A similar pipeline will be used to stream data to a queue on Kakfa. This messages (or records) will be ingested, processed and written to DB using a Python script.

<br>

## **First step**: Download the required images and create compose file

In the host CLI we execute the following command:

```bash
docker pull <image_name>
```

Once downloaded, we will proceed creating a yaml file. Unlike with single running containers, a compose file allow us to define all the services we need to build our application, and the way they should interact with regard to ports or storage, amid others.
A yaml (or yml) file is a descriptive script that tells Docker the services we need, and this deploys all the infrastructure.

![img1](pics/pic2_1.png)

<br>

## **Second step**: Start the services in YAML file

We can start the compose by executing the following command:

```bash
docker-compose up -d
```

This, will spin up all resources in the Docker Compose file, with the configuration defined in it (network, volumes, image, version, etc.)

<a name="build-image"></a> _needed for referencing in Docker Basics_
