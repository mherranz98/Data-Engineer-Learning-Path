<br>
<br>
<a name="readme-top"></a>

# **Challenge 1: Apache Nifi with local file and API 🐋🧑🏼‍💻**

---

The goal of this challenge is to familiarize yourself with Apache Nifi, a powerful tool designed to control the data flow between systems by means of a user-friendly web interface. In addition, and due to the fact that it is the first challenge using Docker, I will go through the basics of this tool.

In this challenge, we will read, process and write data in two separate pipelines: the first one will read a local csv file, filter it by an attribute and write it to a json file; the second is an streaming processing pipeline that ingests data from a public API, processes it and finally writes in a json file.

[Nifi](https://nifi.apache.org/docs/nifi-docs/html/nifi-in-depth.html) is an Apache project designed to integrate and automate the flow of data between systems. It is an open source low-code program that consists of the following components:

- **Web Server** is an HTTP-based component used to visualize the data flow and monitor the events in a user-friendly environment.
- **Flow Controller** is in charge of the Nifi behaviour, extensions and schedules
- **Flowfile** are data records that consist of the content and attributes of data.
- **Processors** are used to listen for incoming data; pull data from external sources; publish data to external sources; and route, transform, or extract information from FlowFiles.
- **Provenance** is a record of what tranformations have undegone the Flowfile.
- **Extensions** can be created to build your own processors with a rapid development and effective testing.
- **Repositories** allow us to undestand Flowfiles and how they have been used by the underlying system. There are three: Flowfile repository for metadata of current Flowfiles in the flow, Content repository for content of current and past Flowfiles, and Provenance repository for the history of Flowfiles.

Apache NiFi works by creating data flows, which are composed of interconnected processors that perform specific data processing tasks such as filtering, aggregation, splitting, and merging. Each of them has its own set of properties that can be configured to control its behavior, such as the input and output formats, the criteria for filtering data, and the rules for routing data to different destinations.

As the data flows through the processors, NiFi keeps track of its provenance, or lineage, which provides a complete record of the data's origin, transformation, and destination. This provenance data can be used for auditing, troubleshooting, and compliance purposes.

Once the data has been processed, NiFi can route it to various destinations, such as databases, Hadoop clusters, messaging systems, or other applications. NiFi also provides a range of data routing options, such as round-robin, load balancing, and failover, to ensure that data is delivered to its intended destination in a timely and reliable manner.

Overall, NiFi's drag-and-drop interface onto a canvas, extensive set of processors, and support for real-time data processing and routing make it a powerful and flexible data integration tool that can be used for a wide range of data integration use cases.

To know more about Apache Nifi, read the article [`How Apache Nifi works - surf on your dataflow, don’t drown in it`](https://www.freecodecamp.org/news/nifi-surf-on-your-dataflow-4f3343c50aa2/)

<br>

## **First step**: Download the Apache Nifi from Docker Hub with a "docker pull" command

In the host CLI we execute the following command:

```bash
docker pull apache/nifi
```

Because a version is not specified in the command, the lastest will be downloaded in our local image repository. Once downloaded, we can execute the command:

```bash
docker images
```

and a detailed list of the available downloaded images will be displayed.

![img1](pics/pic2_1.png)

<br>

## **Second step**: Instantiate the apache/nifi image

Once downloaded the image, we need to make it run by executing the following command:

```bash
docker run --name nifi \
  -p 8443:8443 \
  -d \
  -e SINGLE_USER_CREDENTIALS_USERNAME=admin \
  -e SINGLE_USER_CREDENTIALS_PASSWORD=ctsBtRBKHRAx69EqUghvvgEvjnaLjFEB \
  apache/nifi:latest
```

With this command we are able to instantiate the image, that is creating a container. In the command we specify the name of the container "nifi", which must be unique, the ports mapped (port 8443 from container maps to port 8443 on host), and finally a single user authentication credentials that are specified as environment variables. No volumes are created so far (see Challenge 2)

Once executed, we can see in the Docker Desktop container page there is an instance of the Apache Nifi image running with some details are displayed. We can also display the running containers on the CLI by executing the command:

```bash
docker ps
```

![img2](pics/pic2_22.png)

We can also access the CLI of the container by clicking on the container of Docker Desktop and accessing the Terminal page in it. Another option is the execute the command below, which will make a bash CLI of the container pop up in the same host CLI. We can go back to the host terminal with an _exit_ command.

```bash
docker exec -it <container_name> /bin/bash
```

![img3](pics/pic2_3.png)

<br>

## **Third Step**: Copy the local file in host to nifi container

Because no volumes were mounted, we need to copy the required files stored in our host to the container so as to work with it. Afterwards, we will have to copy the resulting file to host.

To copy the file we must execute the following command in the host prompt:

```bash
docker cp data/netflix.json nifi:/opt/nifi/nifi-current/input_data
```

This command has been executed inside the Challenge 1 directory, so in order to access the json file we must write the relative path, and for the destination file we first need to specify the container name, which is the one we have given when instantiating the image in the run command, and the absolute path to the destination directory.

Note that by executing the command below on the _nifi/current_ directory, we can see that not all the read-write permissions of the input_data directory directory are granted.

```bash
dir -ls
```

![img23](pics/pic2_23.png)

<br>

## **Fourth Step**: Access the web-based interface of Nifi and build the pipeline

Enter the hyperlink [https://localhost:8443/nifi/](https://localhost:8443/nifi/), and after clicking on _Proceed Unsafe_, you need to introducte the credentials used when creating the container. Once logged in, we can start building the pipeline.

Two different pipelines will be created; the first will read the data from a local json file, will filter some films depending on their film rating, and finally write it to a csv file. The second pipeline, on the contrary, will take the data from an API in streaming, it will apply some transformations and write the records in a csv file.

<p align="right"><a href="#readme-top">🔙</a></p>

---

<br>

## **1. Batch pipeline with local JSON file**

The first processor we will need to use is the GetFile where we will write the absolute path of the JSON file in the container (because it is where the program is running, not on the host).

Afterwards, we will use the UpdateAttribute processor that takes the JSON and converts it into a CSV file. Once converted into a Flowfile, we can filter the records by simply applying a SQL-like query.

```SQL
SELECT * FROM FlowFile WHERE rating NOT IN ('TV-MA', 'NC-17', 'R')
```

This will exclude all films not allowed for people under 14 years old, which are the following ratings:

- TV-MA: _"Mature Audience Only"_
- NC-17: _"No One under 17 and under Admitted"_
- R: _"Restricted"_

To materialize the writing into a file, we will use a PutFile processor. In this, we will include the absolute path in the container.

![img6](pics/pic2_8.png)

Posteriormente le adjudicamos al flowfile un schema que se llamará _netflix_.
![img7](pics/pic2_9.png)

<br>

## **Quinto paso**: Filtramos los records deseados mediante una query SQL

Con el processor QueryRecord filtramos las peliculas aptas para mayores de 14, o dicho de otra manera las que no pueden ver menores de 14. Con la query:

> SELECT \* FROM FlowFile WHERE type LIKE '%Movie%' AND rating NOT IN ('TV-MA', 'NC-17','R')

poderemos filtrar las peliculas que no tengan los ratings:

- TV-MA: _"Mature Audience Only"_
- NC-17: _"No One under 17 and under Admitted"_
- R: _"Restricted"_

![img8](pics/pic2_10.png)

<br>

## **Sexto paso**: Transformamos el csv a json definiendo su esquema

Con el processor ConvertRecord, leemos el csv y lo escribimos como un json. El CSVReader inferirá el esquema, tendrá como delimitador una coma (véase en el mismo documento), e incluye los headers.

![img9](pics/pic2_18.png)

Por su parte, el JsonRecordSetWriter cogerá el schema que definamos en un registro de esquema Avro.

![img10](pics/pic2_20.png)

En la definición de esquema, debemos utilizar el mismo nombre de esquema que hemos utilizado en el UpdateAttribute del principio donde hemos definido su nombre. En este caso, lo hemos llamado _netflix_. Pasamos a definir todos sus campos como strings.

![img11](pics/pic2_16.png)

<br>

## **Séptimo paso**: Creamos el documento el el directorio output_files

Con el processor PutFile, configuramos el directorio donde queremos dejarlo.

![img12](pics/pic2_13.png)

<br>

## **Octavo paso**: Copiamos el archivo desde el contenedor hasta la carpeta host dónde estamos trabajando

De forma análoga a lo que hicimos para copiar el archivo netflix.csv desde el host hasta el contenedor, ahora copiamos el archivo resultante desde la carpeta output_files del contenedor hasta nuestro lugar de trabajo /RETO 3.

![img12](pics/pic2_17.png)

<p align="right"><a href="#readme-top">🔙</a></p>

---

<br>

<a name="readme-second"></a>

## **2. Stream pipeline with API**

<p align="right"><a href="#readme-top">🔙</a></p>
