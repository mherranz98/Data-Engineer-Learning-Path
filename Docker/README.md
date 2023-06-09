<div>
<h1 align="center"; style="font-size:30px">
  <br>
  <a href="https://hpai.bsc.es/"> 
      <img src="../Images/Logos/logo-docker.webp" alt="UB Logo" width="25%">
</a>

<h1 align = "center">
    Docker Challenges 🐋📚
</h1>

<h2 align="center">
  Marc Herranz i Alié
</h2>

<br></br>

</div>

## 🧪 What is Docker ?

---

Docker is a PaaS product that uses OS-virtualization to deliver software in form of packages called images. It is an open source service used to automate the deployments of applications in lightweight containers so applications can work efficiently in different environments.

Containers are fundamentally changing the way we develop, distribute, and run software.
Developers can build software locally, knowing that it will run identically regardless of host environment—be it a rack in the IT department, a user’s laptop, or a cluster in the cloud. (Mouat, pg 3)

Instead of operating the software and apps in the host, it isolates the applications and its dependencies in containers, which at first glance are simply lightweight read-only images that contain multiple layers, among which application code, libraries, tools, dependencies and other files.

<p align = "center">
  <img src="../Images/pics/docker-vm-architecture.png" alt="VM vs Containerized Architecture" width="400">
  <p align = "center">
    <i>VM vs Containerized Architecture</i>
  </p>  
</p>

At first glance, they appear to be just a lightweight form of virtual machines, but they have several advantages that these lasts don't and enable us to easily deploy portable, flexible and lightweight software. The main differences with VMs are:

- Containers **share the OS with the host**, which makes them more efficient and lightweight (OS-level virtualization). VMs on the other side, have a component named hypervisor that allows one host computer to support multiple guest OS and virtually share its hardware, such as memory and processing.
- The lightweight nature of containers means developers **can run dozens of containers** at the same time emulating a production-ready distributed system on a single host machine without the need to use VMs alone.
- Images are **fast-booting**, meaning that they can be started and stopped in a fraction of a second. VMs are not easily bootable and can take minutes to start. Applications running in containers incur little to no overhead compared to applications running natively on the host OS.
- There is **no need to worry about configuration** or changes required to the system. In turn, users can download and run complex applications and developers can avoid worrying about differences in user environments and the availability of dependencies.
- The **portability** of containers has the potential to eliminate a whole class of bugs caused by subtle changes in the running environment.
- The final purpose of a containers is to **make applications portable and self-contained** while VMs try to emulate a foreign environment. (Mouat, pg 3-4)

<br>

## 🧑🏼‍💻 Why Docker ?

---

Docker is a popular containerization platform that allows you to create, deploy, and run applications in a portable and efficient manner. The main reasons to go for Docker were:

- <ins>Isolation:</ins> Docker uses containerization to isolate your applications and dependencies from the underlying system, ensuring that they run consistently across different environments. Can develop and deploy with confidence, knowing that they will work the same way everywhere.

- <ins>Portability:</ins> containers can run on any system that supports Docker, making it easy to use other apps in different environments.

- <ins>Efficiency:</ins> By means of a layered file system and sharing of resources, it minimizes the amount of disk space and memory required for each container.

- <ins>Security:</ins> Containers run in a sandboxed environment, which provides an additional layer of security to your applications by limiting access to the underlying system.

- <ins>Flexibility:</ins> Easy to manage and scale applications, allowing you to quickly spin up new instances of your containers and distribute them across multiple hosts.

Overall, and specially focusing on the exercises and challenges that we will develop, Docker is the best option to start the data engineering path because it simplifies the process of configuring, developing and packaging software. Moreover, in a production environment it is a good option as it also helps in the application deployment and scaling.
Its popularity and community support mean that there are multiple resources and tools available to get you started and solve problems along the way.

Nowadays, a lot of Big Data software is open source and can be downloaded using Docker Hub, a public online repository of images from community developers and well-known software vendors. We will use this public repository to download images and work with them in order to create our projects. Docker Hub does also support private container images sharing, but we will not use this feature.

<br>

## 🏛 Docker Challenge Folder Structure

---

The structure of each challenge is generally different, but in summary it contains the README file explaining the steps followed during programming process, a Dockerfile or compose file used to build images or run containerized applications, repectively, as well as the extra code, files and dependencies required to execute it.

- [**Challenge 1**](Challenge%201) taking advantage of Apache Nifi open source image provided by Apache it explores its main functionalities. Docker architecture will be briefly introduced to understand how it works. In this exercise we will process some data stored in a local JSON file and data extracted by means of API calls.

- [**Challenge 2**](Challenge%202) will explore the advantages that event storing has for stream processing. The streaming data source will be a Nifi pipeline that will pour data in a Kakfa queue. Once there, messages will be consumed by a Python script that will send them to databases (DBs). The DBs will be relational (Postgres) and non-relational (Mongo).

- [**Challenge 3**](Challenge%203) will explore the PySpark functionalities in a simple standalone dockerized architecture where a Spark public image will be used to emmulate a master-slave distributed architecture. After processing, data will be sent to the same databases explained above.

- [**Challenge 4**](Challenge%204) will use Java to create a purely stream processing (not microbatching) by means of Flink software. With regard to the IDE, Intellij has been chosen as the best option for compilation and dependencies.

- [**Challenge 5**](Challenge%205) will introduce Spark Scala. Scala is considered to be the "Python of Java" due to its object-oriented and functional programming in a concise and high-level language. Further details regarding Spark Scala will be explained later (...).

- [**Challenge 6**](Challenge%206) processing with GCP and orchestration with Airflow will be done on data extracted by means of an API. A complete, monitored and scheduled pipeline will be created.

<br>

## 📗 Bibliography

---

- Mouat, A. _Using Docker: Developing and Deploying Software with Containers_. (1st ed.). O'Reilly, 2015

<br>

## 🎓 License

---

This repository and thereby all its content is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<br>

## Further Issues and questions ❓

---

If you have issues or questions, don't hesitate to contact Marc Herranz i Alié at [mherranz98@gmail.com](mailto:mherranz98@gmail.com).
