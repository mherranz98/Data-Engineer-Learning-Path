<br>
<br>

# **Infrastructure Foundation: Storage and Database Services📚☁️**

---

<br>

Every app needs to store data (streaming, central, etc.) Important that service supports the application's requirements for effectively storing and retrieving data given its characteristics.
The purpose of module is to explain the services available and when to consider from an infrastrucure perspective.

<br>

---

<br>

## **Cloud Storage**

Object storage service. Worldwide storage and retrieval of any amount of data at anytime. Can be used in different scenarios: website content, archival and disaster recovery or distributing large data objects to users via direct download.
Some of its features:

- Scalable to exabytes of data
- Time to first byte is in milliseconds
- High availability across all storage classes
- Single API acorss storage classes

Not a file system, instead a collection of buckets where objects are placed. Can create directories, but these are objects, that will hold other objects. Not easy to index files, instead have specific URL to access objects. Four different
storage classes:

- Standard: data frequently accessed or stored for brief periods of time. Most expensive but no minimum duration nor retrieval cost. In a region, appropriate for storing data in the same location as GKE or instances that use the data
  Colocating resources maximizes performance for data intensive computations and reduces network charges. In a dual region, still get optimized performance when accessing GCP products that are located in one of the associated two regions.
  Also get improved availability if storing data in separate locations. In multiregion mode, appropriate for casing where access to data is requires across the world (website content, stream videos, interactive workloads, etc.).
- Nearline: low cost highly durable for infrequently accessed data like backup, long tailed multimedia content, and data archiving. Better choice than standard when lower availability, authority day, minimum storage duration,
  and costs for data access are acceptable tradeoffs for lowered at less storage costs. 30-day minimum storage duration
- Coldline: very lowcost, highly durable for infrequently accessed data. Better choice than standard storage or nearline storage when lower availability, a 90 day minimum storage duration and higher costs for data access are acceptable
  tradeoffs for lowered address storage costs. 90-day minimum storage duration
- Archive: lowest cost, highly durable for data archiving, online backup and disaster recovery. Unlike the source, big coldest storage service offered by other cloud providers, your data is available within milliseconds, not hours or
  days. Unlike others, archive storage has no availability SLA though the typical is comparible to nearline and coldline. Has higher costs for data access and operations as well as a 365 day minimum storage duration. Best for accessing
  data less than once a year.

In each of classes provide three location types:

- Multiregion
- Dual region
- Regional -> not georedundant

Durability has 11 9's, meaning that you won't lose data. Availability is equivalent to a bank closing.
Cloud Storage is broken down into a couple of items: buckets have globally unqiue name and cannot be nested. The data that you put in buckets are objects that inherit the storage class of the bucket and can be all kind of files. There is no m
minimum size and can scale up to what the quota allows. There is unlimited storage. To access the data, you can use the gsutil command, or either JSON or XML APIs.
When upload object to bucket, it is assigned the bucket storage class, unless specified another. Cannot change the location type. Can change the storage type without need to move the object from bucket. For objects that will not be accessed
frequently, it can be changed (object cycle management).
For access control:

- IAM: which individuals can see the bucket, list objects inside, etc. Roles inherited from project to bucket to object.
- ACLs: fine-grain control to define who has access to buckets and object as well as their level. Can create up to 100 ACL entries. Have a scope (persons, group) and a permission (actions to be performed).
- Signed URLs: cryptographic key for time-limited access to bucket or object. Easier and more efficient to grant limited time access tokens that can be used by any user instead of using account based authentication.
  Grant access to specific GCS resource and specifies when this expires. Signed with a private key associated with their service account.

<br>

---

<br>

## **Cloud Storage Features**

- Customer-supplied encryption keys instead of Google-managed keys
- Object Lifecycle Management: archive or delete automatically objects
- Object Versioning: charged as multiple files.
- Directory Synchronization: can sync a VM directory with a bucket
- Signed Policy Document: refined control determining what file can be uploaded by someone with a signed URL
- Object change notification
- Data import
- Strong consistency
- Objects are immutable. Object versioning feature can be enabled for a bucket, and creates an archive object every time a live object is deleted or overwritten. Can restore the object to an older state, or delete a version. Turning versioning
  off causes the bucket to accumulate new objects.
- Can set a time to live. Object Lifecycle Management can be configured to a bucket and will apply to all of its objects. Performs a specific action on the object if condition is fulfilled (delete, keep only, downgrade storage class). Inspections
  occur in asynchronous batches. Updates to lifecycle configuration can take up to 24 hours, so it will continue with previous congifuration until changed.
- Object change notification can be used to notify an application when an object is updated or added to a bucket. The notification channel is the means by which the notification message is sent to an app watching the bucket. Pub/Sub notifications
  is recommended (more flexile, cost effective, easy to set up, and faster) to manage changes in buckets.
  Console allows to upload individual files, but if needed to upload loads of data: - Transfer Appliance: hardware to securely migrate large volumnes of data from 100TB to 1PB too GCP without disrupting operations - Storage Transfer Service: enables high performance imports of online data (S3, http location, another bucket, etc.) - Offline Media Import: third party service where it is sent to a provider that uploads the data from physical media
  GCS offers strong global consistency. When upload an object to GCS, and receive a success response, it is ready for download from any location where Google offers service. True for creating new objects or overwritting existing ones. Because
  uploads are strongly consistent. It also extends to the deletion of objects. An attempt to download after deleting object or its metadata, an error will arise. Bucket listing and object listing are also globally consistent.

<br>

---

<br>

## **Choosing the GCS class**

Depending on the amount of times we want to read the content of the bucket, we will choose:

- Less than once a year -> archive
- Less than once every 90 days -> Coldline
- Less than once every 30 days -> Nearline
- For more ofter read and writes -> Standard

Want to take into account the location type:

- Single region: optimize latency, netqwork bandwidth, pipelines grouped in the same region
- Dual-region: similar performance as single region but higher availability
- Multi-region: serve content for consumers outside Google network, large geographic areas, and higher availability

<br>

---

<br>

## **Filestore**

Managed file store service for apps that require a file system interface and shared file system for data. For Compute Engine and GKE isntances. Ability to finely tune performance and capacity independently making it predictable and fast performance
for file-based workloads. It supports NFSv3. Benefit from scaling out, up to 100TB, and file locking without the need to install any plugin.
Many use cases:

- Application migration: on-premise app. Filestore supports app that need a shared file system
- Media rendering: filestore file share Compute Engine instances enabling visual effect artitst to collaborate on the same file. Rendering runs across multiple machines, thereby shared file system. Scale for rendering needs
- Electronic Design Automation (EDA) data management batch workloads across 1000s of cores with large memory needs.
- Data Analytic workloads latency-sensitive that need scaling out based on needs. Because persistent and shareable storage layer, we have immediate access to data for high-performance analytics without need to downloading and offloading data
- Genome processing: billions of data, needing speed, security and scalability. Offers predictable prices for performance
- Web content for large hosting providers

<br>

---

<br>

## **Cloud SQL**

No need to install SQL on a VM using Compute Engine. Doing this we have a fully-managed service of MySQL, PostgreSQL or SQL Server meaning that patches and updates are automatically applied. Still have to administer users, authentication tools,
etc. It supports many clients like Cloud Shell, App Engine or Workspace scripts. High performance and scalabuluity up to 64TB of capacity, 60.000 IOPS and 624GB of RAM per instance. Can scale up to 96 processors and scale out to read replicas.
Supports just some versions of previous SQL choices.
Other services provided by Cloud SQL are:

- HA configurtion within a region instance, there is a primary instance and standby. All writes are replicated to disks in both zones before a transaction is commited. In an event of failure, the persistent disk is attached to the
  standby instance and it becomes the primary. Users are then reroutes. This process is called failover.
- Backup service is automated and on-demand with point-in-time recovery
- Import/export databases or csv files
- Scale up for improving machine capacity, and out for increasing read replicas (Cloud Spanner)

For connecting to Cloud SQL we can choose:

- Private IP: most secure and private. Never exposed to public Internet. Needs to be located in the same region. It is a performance-based recommendation in case it is in the same region
- Cloud SQL Proxy handles authentication, encryption and key rotation
- Manual SSL Connection for managing authentication, encryption and key rotation by your own
- Authorized Networks with IP address over its external IP address in case SSL connections are forbidden

<br>

---

<br>

## **Cloud Spanner**

In case CloudSQL does not have enough horizontal scalability. Provide petabytes of capacity, strong consistency at global scale, automatic synchronous replication for high availability. A particular use case is financial and inventory applications
Depending on regional or multiregional, we will have different SLAs. Combines both strengths of relational (schema, SQL, consistency) and non-relational (high availability, and scalability) DB. It replicates data in N cloud zones, in one region
or across multiple. The placement is configurable allowing global placement and high availability. Replication of data will be synchronized with Google fiber network. Using atomic clocks ensures atomiciy whenever updating data.

<br>

---

<br>

## **Firestore**

Highly scalable, NoSQL database. Fast fuly-managed, serverless, No-SQL document database that simplifies storing, sinking and querying data for mobile, web and IoT apps at global scale. It supports ACID transactions. There is a live synchronization
and offline support in case no internet is available temporarily. With automatic multiregion replication and strong consistency, data is secure. It also allows to perform sophisticated queries against data without any degradation in performance
giving more flexibility in how to structure data.
Firestore is an upgrade of Datastore, though it can go back to that mode. It is backwards compatible with Datastore. In Datastore mode, you can access an improved storage layer while keeping Datastore system behaviour. Some limitations that
are removed are queries are no longer eventually consistent, but rather all now; transactions are not limited to 25 entity groups, and rights not limited to 1 per second.
In native mode it introduces new features like a strong consistent storage layer, collection and document data model, real time updates and mobile and web libraries. Firestore is compatible with Datastore but these last three, are not.
Datastore mode -> new server projects
Native mode -> mobile and web apps
As the next generation of Cloud Datastore, Cloud Firestore is compatible with all Cloud Datastore, APIs and client libraries. Existing Cloud Datastore users will be live upgraded to Cloud Firestore automatically at a future date. If your
schema might change and you need an adaptable database, you need to scale to zero or you want low maintenance overhead scaling up to terabytes consider using Cloud Firestore
If you don't require transactional consistency, you migh want to consider BigTable.

<br>

---

<br>

## **BigTable**

If don't require transactional consistency.

- Fully managed NoSQL wide column database
- Petabyte-scale
- Sub 10-ms latency
- Seamless scalability for throughput
- Learns to adjust to specific access patterns
- Great choice for operationala and analytical apps including IoT, user analytics, financial analysis
- Ideal ML storage engine
- Easily integrates with other Big Data tools (DataProc, DataFlow) and open source APIs

Stores data in massively scalable tables, each of which sorted key value map. Table is composed of rows, each describing a single entity. Each columns is identified by a combination of column family and column qualifier, which is a unique name.
Each row-column intersection can contain ultiple cells or versions at different timestamps so we know how stored data has been altered over time. Table are sparse. If there is no data in a cell, it does not take up any space. The design choice
takes advantage of the sparseness of BigTable tables and the fact that new qualifiers can be added as data changes.
With regards to the architecture, there is a frontend server pool and nodes, which is separated from storage. Table is shared into blocks of contigous rows called tablets. Tablets are stored in Colossus, Google File Table in SSTable format,
which provides a persistent, ordered, immutable map of keys to values. BigTable learns to adjust to specific access (query) patterns, so if a node frequently accesses a certain subset of data, BigTable udates indexes so other nodes can distribute
workload evently. Throughput scales linearly with the number of nodes.
If needed to store more than 1TB of structure data, or have to write high volumnes of data, or have rw low latency (<10ms) and have strong consistency, choose BigTable. The smallest node configuration is three nodes that can handle up to 30.000
operations per second. Furthermore, it is relevant to note that you'll be paying for amount of time nodes are operational, regardless of the application that is using them is working or not.

<br>

---

<br>

## **Memorystore**

- Fully managed in-memory data store scalable, secure and highly available infrastucture. High performance can be achieved leveraging highly scalable, available and secure Redis service.
- Allows to spend time writing code and apps. It automates complex tasks enabling high availability, failover, patching and monitoring.
- High availability instances are replicated across two zones providing 99.9% SLA.
- Can achieve submilisecond latency and desired throughput.
- Can grow instances effortlessly with minimal impact on app availability. Can support instances up to 300GB and network throughput of 12GBps.
- Because it is fully compatible with Redis Protocol, can lift and shift local Redis apps without code changes using the import/export feature. All libraries will work.

<br>
