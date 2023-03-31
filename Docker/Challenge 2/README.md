<br>
<br>

# **Challenge 2: Apache Kafka, Python and DBs 🐋🧑🏼‍💻**

---

The goal of this challenge is to familiarize yourself with Apache Kafka, an event streaming platform that enables us to handle real-time data feeds. We will go through the basics of its architecture and finally do some processing with a Python scripts. Resulting data will be pushed to databases, relational and non-relational.

In the [second part of the Challenge 1](../Challenge%201/README.md#readme-second), we were able to discover the power of Nifi as an streaming tool. A similar pipeline will be used to stream data to a queue on Kakfa. This messages (or records) will be ingested, processed and written to DB using a Python script.

Apache Kafka is a distributed streaming platform open-sourced by Apache Software Foundation that is used to handle large amounts of real-time data and provides a highly scalable and fault-tolerant architecture for streaming data.

At its core, Kafka consists of a few key components:

- **Brokers**: are servers that handle the storage and distribution of Kafka topics. Each broker stores one or more partitions of a topic, and all brokers work together to form a Kafka cluster. Brokers within a cluster communicate with each other to ensure data replication for fault tolerance.

- **Topics**: is a named stream of data that is divided into partitions. Somehow, they can be undestood as tables of event storage. Each partition of a topic can be replicated across multiple brokers for fault tolerance.

- **Producers**: are applications or processes that generate data to be sent to Kafka topics. Producers can send data to specific partitions or let Kafka decide which partition to write to based on a configurable partitioning strategy.

- **Consumers**: are applications or processes that read data from topics. They can subscribe to one or more topics and read data from specific partitions of those topics. Kafka supports both single-consumer and multi-consumer scenarios.

- **Consumer Groups**: is a group of consumers that work together to read data from Kafka topics. Each consumer in a consumer group reads data from a unique subset of partitions of a topic, and Kafka ensures that each partition is read by only one consumer in the group.

- **Connectors and APIs**: Kafka Connect is a framework for building and running connectors that move data between Kafka and other data systems such as databases, Hadoop, etc. It also provides various APIs for developers to work with, including a high-level streaming API and a lower-level producer and consumer API.

<p align = "center">
  <img src="../../Images/pics/kafka-architecture.png" alt="Kafka Architecture" width = 500>
  <p align = "center">
    <i>Kafka Architecture</i>
  </p>  
</p>

One of the key features of Kafka is its ability to handle data in real-time with low latency, which makes it an ideal choice for real-time data processing (streaming analytics, monitoring, or alerting).

Apache Kafka uses ZooKeeper to manage and coordinate the cluster of Kafka brokers. ZooKeeper is a centralized service that provides distributed synchronization and coordination for distributed systems. At the end, it is responsible for:

- **Cluster coordination** as it keeps track of the status of each broker, the topics and partitions, and the configuration data for the cluster.

- It **elects the leader** because in a Kafka cluster, each partition of a topic is managed by a single broker, known as the leader. ZooKeeper helps to elect the leader for each partition in the event that the current leader fails or goes offline.

- Kafka uses ZooKeeper for **configuration management** as it stores and manages various configuration data, such as the location of topics, the number of replicas for each partition, and the offset of the last message read by a consumer.

- ZooKeeper can be used to **enforce quotas** on the number of requests that a Kafka broker can handle, to prevent from becoming overloaded.

Overall, ZooKeeper is a critical component of the Kafka ecosystem and plays a key role in managing the cluster and ensuring that it remains scalable, reliable, and fault-tolerant.

<p align = "center">
  <img src="../../Images/pics/kafka-architecture-2.webp" alt="Kafka Replication Strategy" width = 500>
  <p align = "center">
    <i>Kafka Replication Strategy</i>
  </p>  
</p>

To know more about Kafka, read the article [`In-Depth Summary of Apache Kafka`](https://aozturk.medium.com/kafka-guide-in-depth-summary-5b3cb6dbc83c).

<br>

## **First step**: Create compose file and start its services

There is no need to download one by one the images that are going to be used in the challenge. Instead, by simply building up the compose, images not available in the local image repository will be downloaded (pull flag in _docker-compose up_ command is set to "always" by default).

We will proceed creating a yaml file that unlike with single running containers, it allow us to define all the services we need in order to build our application, and the way they should interact with regard to ports or storage, amid others.
A yaml (or yml) file is a declarative script that tells Docker the services we need to deploy and this does it by itself.

<p align = "center">
  <img src="pics/pic2_1.png" alt="Docker Compose YAML File" width="350">
  <p align = "center">
    <i>Docker Compose YAML File</i>
  </p>  
</p>

<br>

We can start the services in the compose by executing the following command:

```bash
docker-compose up -d
```

<p align = "center">
  <img src="pics/pic2_3.png" alt="docker-compose up command" width="600">
  <p align = "center">
    <i>docker-compose up command</i>
  </p>  
</p>

<br>

This, will spin up all resources in the Docker Compose file with the configuration defined in it (network, volumes, image, version, etc.). The services we include in this challenge are:

- **Nifi** image which includes a UI that can be accessed through the port 8443
- **Kakfa** images that consist of 3 distinct services: a web-based UI, Zookeeper for distributed coordination of Kafka brokers (though not needed), and Kafka itself
- **Python** image to execute scripts
- **Postgres** which includes a UI named pgadmin and the database itself
- **MongoDB** which includes a UI named mongo-express and the database itself

<br>

## **Second step**: Design the streaming pipeline in Nifi

Once services are up and running, we can access Nifi in a similar way we did in Challenge 1. Next we will create a similar pipeline to the one we made in the [second part of the Challenge 1.](../Challenge%201/README.md#readme-second) The processors that we will use will be _GetHTTP_, _SplitJson_, and _Publish_Kafka_2_6_.

The first processor is resposible of performing the HTTP requests for the API and streaming the response to the SplitJson processor, which separates the different records stored in a single HTTP response and sends them into the publisher processor, which receives individual messages and publishes them into the Kafka topic.

<p align = "center">
  <img src="pics/pic2_4.png" alt="NiFi pipeline" width="400">
  <p align = "center">
    <i>NiFi pipeline</i>
  </p>  
</p>

Because we want to publish the messages to Kafka, we will set the Kafka broker address to the name of the container that can be found executing the commands below, and the port number that was set to 9092 in the docker-compose file:

```bash
docker network ls
```

```bash
docker inspect <network_name>
```

This will display a list of the running containers in the compose chosen with its corresponding names. You will see that this name corresponds to the one set in the docker-compose file to the Kafka service.

Whilst running the pipeline, we can open the Kafka UI accessing the [http://localhost:8080/](http://localhost:8080/) and check that messages are properly being sent to the topic. The topic name is set in the publisher of the NiFi pipeline. We can set a Live mode so messages will be shown in the UI as they are published to the topic.

<p align = "center">
  <img src="pics/pic2_5.png" alt="Kafka UI in Live mode" width="400">
  <p align = "center">
    <i>Kafka UI in Live mode</i>
  </p>  
</p>

<br>

## **Third step**: Program the Python script

The first thing we need to consider when composing the Python script is where it will be executed. So as to know the address of the listener, we must have in mind the Kafka Architecture briefly explained above. In case the program is executed in a container from Docker, the port must be the 9092. On the contrary, if trying to access the Kafka listener from outside Docker (localhost), port 9092 should be then used.

In order to work with Kafka from a Python program, we must its client library python-kafka. It provides a convenient and powerful way for Python developers to produce and consume messages to and from Kafka clusters.

<p align = "center">
  <img src="pics/pic2_2.png" alt="Kafka Architecture within Docker" width="400">
  <p align = "center">
    <i>Kafka Architecture within Docker</i>
  </p>  
</p>

<a name="build-image"></a> \_needed for referencing in Docker Basics_when creating own python image
