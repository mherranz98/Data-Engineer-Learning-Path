<div>
<h1 align="center"; style="font-size:30px">
  <br>
  <a href="https://hpai.bsc.es/"> 
      <img src="Images/Logos/logo-ub.png" alt="UB Logo" width="25%">
      <img src="Images/Logos/logo-eae.jpg" alt="EAE Logo" width="25%">
      <img src="Images/Logos/logo-gft.jpg" alt="GFT Logo" width="19.4%">
</a>

<h1 align = "center">
    Data Engineer Learning Path 🧑🏼‍💻🤖
</h1>

<h2 align="center">
  Marc Herranz i Alié
</h2>

<h3 align ="center">
  Physicist, Big Data Engineer and Technology Enthusiast
</h3>

<br></br>

</div>

This GitHub repository aims to shed some light on the current trends in data departments of companies, and specifically of data engineer roles. By means of exercises, books, projects and more content, I will try to share with you the most demanded programming and scripting languages, as well as libraries, frameworks, and technologies.

As I mentioned before, I am a physicist that came to this new world without deep programming nor technological knowledge. During my Master's at EAE Business School, I was introduced to some past, present and future technologies and frameworks like relational databases, Spark, or Databricks. During my Master's, I did an internship in a delivery company fulfilling duties related to database management and business reporting to managers where I could master SQL and some visualization tools.
Next step was to specialize in Data Engineering, and to do so, I started working in the data family at GFT, a technological German consultory. This learning path started at the end of 2022 whilst I was doing my traineeship at GFT Technologies.

This repository contains a collection of notes, exercises and small projects developed by myself since 2022. Most of them are related to data processing but each of them is performed with different technologies. The content is separated in different folders, the content of which is briefly explained below.

<br></br>

# 🏛 Repository Structure Overview

---

## 🧑🏼‍💻 Code Folder

- [`Docker`](Docker) : notes and set of challenges using a vast variety of technologies using containerized software. In these challenges, we explore the basics of Docker and we develop data pipline with either batch or stream processing from various data sources like APIs, local files, Cloud Storage files, etc.
  - [`Notes`](Docker/Basics%20of%20Docker/README.md) explains the basics of Docker architecture, the differences and advantages with VMs and other deployments, as well as some basic commands
  - [`Challenge 1`](Docker/Challenge%201) uses Apache Nifi and explains the basics of Docker
  - [`Challenge 2`](Docker/Challenge%202) uses Apache Kafka for event processing, Python for processing and databases (PostgreSQL and MongoDB) for storage purposes.
  - [`Challenge 3`](Docker/Challenge%203) uses Apache PySpark to perform some processing on events stored in a Kafka queue. Similarly, records are stored in DB.
  - [`Challenge 4`](Docker/Challenge%204) uses Apache Flink in Java for pure stream processing.
  - [`Challenge 5`](Docker/Challenge%205) uses Apache Spark in Scala for developing a data pipeline
  - [`Challenge 6`](Docker/Challenge%206) uses Apache Beam for deploying on GCP Dataflow job

<br>

- [`GCP`](GCP) : notes and set of exercises using some of the many GCP services. The content from this folder was developed while obtaining the Associate Cloud Engineer Certification from Google Cloud Platform.
  - [`Notes`](GCP/Notes%20on%20GCP/README.md) contains an schematic overview of GCP main services, structure, and other relevant components.

<br>

# 🎓 License

---

This repository and thereby all its content is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<br>

## Further Issues and questions ❓

---

If you have issues or questions, don't hesitate to contact Marc Herranz i Alié at [mherranz98@gmail.com](mailto:mherranz98@gmail.com).
