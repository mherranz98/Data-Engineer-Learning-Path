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
