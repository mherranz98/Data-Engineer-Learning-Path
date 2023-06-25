<br>
<br>

# **Infrastructure Foundation: part 2 📚☁️**

---

<br>

# **Identity and Access Management**

Sofisticated system built on top of email-like address names, job type roles in granular permissions. It is a way of identifying who can do what on which resource. Who can be a person, group or an application; what can be an action or specific
privileged, and the resource any GCP service. IAM is composed of different objects: organization, folders, projects, resources, roles and members.
GCP resources are organizaed hierarchically in a tree structure. Organization is the root node, split in folders, and projects, which host resource. Each resource has exactly one parent. The organization represents the company. IAM roles
granted at the organization level are inherited by all resources hosted in any of the organization's projects. The folders might represent departments in a company, and similarly, all IAM roles granted at this level are inherited. Projects
represent a trust boundary within your company. Services within the same project have the same default level of trust.

<br>

---

<br>

## **Organization**

Root node of GCP hierarchy. This has many roles, like the organization admin role, which provides access to administer all resources belonging to the organization, which is useful for auditing. Also, there is a project creator role, that allows
to create projects within the organization. (2 roles)
The organization is closly related to a G Suite or Cloud Identity Account. This organization node is automatically created when a G Suite or Cloud Identity Account created a GCP project. GCP communicated its availability to G Suite or Cloud Identity
super admins. These super admin accounts have a lot of control over the organization and all resources underneath. G Suite or Cloud Identity super admins and organization admin are key during the set up and lifecycle control of the organization
resource. These two roles (G Suite and Cloud Identity super admins, and Organization admin) are assigned to different users or groups.

- Super Admins are responsible for assigning the organization admin roles to users, be the point of contact in case of recovery issues, control the lifecycle of GSuite or Cloud Identity, as well as the organization resource.
- Organization Admin are responsible for defining IAM roles, determining the structure of the resource hierarchy, and delegating the responsability over critical components like billing, networking and resource hierarchy over IAM roles.
  Following the principle of least privilege, this role does not include permissions to perform other actions, such as creating folders. It is thus necessary to associate to himself other additional roles to his account.

With regards to folders, it can be understood as suborganizations within organizations. Can be used to monitor different legal entities, departments or teams. Can contain subfolders containing applications, products, etc. Folders allow delegation
of administration rights, meaning that the head of a department would be granted full ownership of resource belonging to his department. Similarly access to resources can be limited by folders, so users from one department can only access and create
GCP resources within the same folder (which means same department).
Let's take a closer look at resource manager roles:

- Organization: admin (full control over all resources of the org) and viewer
- Folder: admin, creator (browse hierarchy and create folders), viewer
- Project: creator (create new projects with automatic ownership and migrate new projects into organization), deleter

<br>

---

<br>

## **Roles**

Define what can be done on resources. There are three types: basic, predefined and custom.
Basic roles are the original available in console, but they are broad. When applying to a project, they apply to all resources within a project. There are four roles:

- Owner: invite memers, remove members, delete projects, and the editor and viewer roles
- Editor: deploy applications, modify code, configure services, and viewer role
- Viewer role: read-only access

These previous roles are concentric. - Billing administrator: manage billing, add and remove adminsitrators without the right to change the resources in the project. Each project can have multiple owners, editors, viewer and billing admin.
Predefined IAM roles offer more fine-grained permissions on particular services. This provides members granular access to specific resources and prevents unwanted access to other resources. These roles are a collection of permissions.
Usually need more than one permission For instance, the role InstanceAdmin Role consists of a list of permissions that can be broken down into service, resource and action (correspond to REST API action). These are compute.instances.{delete,
get, list, setMachineType, start, stop}. Some predefined IAM roles are the following:

- Compute Admin: full control over resources. Includes all permissions beginning with compute.instances.
- Network Admin: permission to create, modify, and delete networking except firewall rules and SSL certificates. (read-only mode for firewall and ephemeral IP addresses)
- Storage Admin: permission to create, modify, and delete disks, images, and snapshots.

Roles are meant to represent abstract functions and are customizable in order to align with real jobs. It is therefore that if a role does not have enough permissions, we need to go for custom roles. Most companies use the least privilege
model in which each person in the organization is given the minimal amount of privilege needed to do his job. Custom roles to define specific and job-tailored roles linking them to a set of permissions. Custom roles are not managed by Google
meaning that if new permissions are added, custom roles will not be updated and these new permissions included.

<br>

---

<br>

## **Members**

Define who can do what. There are 5 tpyes of memebrs:

- Google Account represents any person (developer, admin, etc.) that interacts with GCP associated to any e-mail account that interacts with Google account.
- Service Account: belongs to an application instead of an individual end user. Running code hosted in GCP, you specify an account that code should run as. Can represent multiple though limited by a quota.
- Google Group: named collection of Google accounts and service accounts. Have a unique e-mail address, and are convinient way to apply access policy to a collection of users. Can grant and change access to whole group at once instead
  of individual users.
- Workspace Domain (G Suite): represents a virtual group of all the accounts that have been created in an organization's workspace account. They represent the organization's Internet domain name. When a user is added to the Workspace
  domain, a new Google account is created for the user inside of this virtual group.
- Cloud Identity lets you manage users and groups using Google Admin console. GCP customers that are not workspace customers.

Important to note that IAM does not allow to create nor manage users or groups. Instead, you can use Cloud Identity or Workspace to do so.

- A policy consists of a list of bindings from a list of members to a role, where the members can be user accounts, Google Groups, Google Domains and service accounts. A role is a named list of permissions defined by IAM.
  A policiy is a collection of access statements attached to a resource. Each policy contains a set of roles and role members, with resources inheriting policies from their parent. Resources policies are a union of parent and resource, where
  the less restrictive parent policy will always override the most restrictive policy. The IAM policy hierarchy always follows the same path as the Google Cloud resource hierarchy (org, folder, etc.) meaning that if we change the resource
  hierarchy, the IAM policy hierarchy will do so (for example, moving project into a different organization will make inherit the new organization's IAM policy). Also, child policies cannot restrict access granted at the parent level. (Editor
  at folder and Viewer at project implies having editor at project too). It is, therefore, best practice to follow the principle of least privilege. In order to reduce the exposure to risk, it obligues to select the smallest scope of tasks required
  for the job. This applies to identities, roles and resources. Can also use a recommender for role recommendations to identify and remove excess permissions improving security configurations and enforcing the principle of least privilege.
  The recommender identifies excess permissions using policy insights, which are ML-based findings about permission usage in the project folder or organization.
- IAM conditions allow to define and enforce conditional attribute-based access control for GCP resources. With IAM Conditions, you can choose to grant resource access to identities (members), only if conditions are met. (configure temporary access for
  users in the eveny of a production issue to limit access to resources for employees making requests from the coorporate office). Conditions are specified in the role bindings of a resource's IAM policy. When a condition exists and evaluates
  to true, the access request is granted. Each condition expression is a set of logic statements allowing to specify one or more attributes to check.
- An organization policy is a configuration of restrictions defined configuring a constraint with the desired restrictions for that organization. It can be applied to the organization node and all its folders, or projects within the node.
  Descendants of the targeted resource hierarchy inherit the organization policy applied to the parent. Exceptions to these policies can be made but only with the organization policy admin role.
- If you already have a different corporate directory and we want to get users into Google Cloud, using Google Cloud Directory Sync administrators can log in and manage GCP resources using the same username and passwords that they already use.
  This tool synchronizes users and groups from existing active directory or LDAP system with users and groups in Google Cloud Identity domain. This is just a one-way sync meaning that no content in active directory is modified. This tool is
  designed to run scheduled synchronizations without supervision after sync rules are set up.
- GCP provides single sign on authentication (SSO) so one can still use your own system. When authentication is required, Google will redirect to yor system, and if authenticated, access to Google Cloud is given. If your own authentication system supports
  SAML 2 SSO, this can also be configured with three links and a certificate. If not supported, can also use third-party solutions like ADFS, Ping or Okta.
- Can still create an account without Gmail if you don't want to receive main through Gmail.

<br>

---

<br>

## **Service Accounts**

Type of member that belongs to an applications. Provides an ID to perform server-to-server interactions in a project without supplying user credentials. Can program the application to obtain credentials from the service account, which will
be granted read-write access. By doing this, the app authenticates seamlessly to the API without embedding any secret keys or credentials in your application code or image. Service accounts are identified by an email. There are three types:

- User-created (custom)
- Built-in -> project-number-compute@developer.gserviceaccount.com
- Google API -> project-number@cloudservices.gserviceaccount.com

By default, all projects come with Compute Engine built-in default service account. Apart from this, all projects come with a Google Cloud API service account, which is designed to run internal processes on your behalf and it is granted the Editor
role on the project. You can also start an instance with a custome service account, which are more flexile than the default but require more management. Can create as many as needed. Sign any arbitrary access scopes or Cloud IAM roles and assign
the service accounts to any machines.
With regard to the default, when starting a new instance using gcloud, the default service account is embedded on that instance. Can override this behaviour specifying another service acccount or disabling the service accounts for the isntace.
-Authorization is the process of determining what permissions an authenticated identity has on a set of specified resources. Scopes are used to determine whether an authnticated identity is authorized. Each application sends a request to Google
Authorization Server and in return receives an access token with the scope (permissions) that is has. Scopes can be customized when you create an instance using the default service account. These scopes can be changes after the instance is
created by stopping them. Access scopes are a legacy method of specifying permissions for your VM. Before the existence of IAM roles, access scopes were the only mechanism for granting permissions to service accounts.

- Roles for service accounts can also be assigned to groups or users. First, you create a service account that has the InstanceAdmin role (create, modify and delete machine instances and disks), then you treat the service account as a resource
  and decide who can use it by provisioning users or groups with the Service Account User role, which allows users to use the service account on their behalf. It is therefore that granting Service Account User role to a user or a group is something
  to be reconsidered cautiously. In the same projects, different VMs can be attached to different service accounts, sculpting permissions without recreating VMs. Cloud IAM lets you slice projects into microservices each with access to different
  resources by creating service accounts to represent each one. You assign service accounts to the VMs when they are created, and you don't need to ensure thay credentials have been correctly managed as Googles does it for you.
- Answering the question: how are Service Accounts authenticated?, there are two types of Google service accounts. By default, GCP service accounts from Compute Engine or App Engine have their keys automatically managed by Google itself.
  If you want to use the service accounts outside of GCP, or want a different rotation period, it is possible to manually create and manage your own service account keys. All service accounts have Google-managed key pairs. With Google-managed
  service account keys, Google stores both the public and private portion of the key and rotates them regularly. Each public key can be used for signing for a maximum of two weeks. The private part is always held securely and never directly accessible.
  May optionally create one or more user-managed key pairs (external keys). THe user is responsible for the security of the private key and performing other management operations such as key rotation. Users can create up to tens service account
  keys per service account to facilitate key rotation. Can be managed using Cloud IAM API, command-line or Service Account page in console. Google does not save user-managed private keys, so no help for recovery will be provided. They should
  be used as a last resort.

<br>

---

<br>

## **Best Practices**

- Understand resource hierarchy
- Use projects to group resources that share the same trust boudary
- Check policy granted on each resource and make sure you understand inheritance (Principle of Least Privilege).
- Audit policies with Cloud audit logs
- Audit memberships of groups used in policies
- Grant roles to groups instead of individuals so will jsut need to update group membership instead of changing IAM policy. Can create multiple groups. Groups are associated to role assigned in project.

With regard to service accounts:

- Be careful granting serviceAccountUser role
- Display name that identifies clearly its purpose. Establish naming convention
- Establish key rotation policies and methods, and audit with serviceAccount.keys.list() method

Finally, use Identity-Aware Proxy (IAP), which lets you establish a central authorization layers for applications accessed with HTTPS (identity based access control). Apps protected by Cloud IAP can only be accessed through the proxy by
users and groups with correct Cloud IAM role. It performs authentication and authorization checks when a user tries to access a Cloud IAP secure resource. IAM policy is applied after authentication.

<br>
<br>

# **Storage and Database Services**

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
<br>

# **Resource Management**

Means controlling cost. Quotas that limit consumption and can be raised on request. Billing to set budgets and alerts. Resource management let's you manage resources hierarchically by folder, project and organization. Policies contain a set of
roles and members that are set on resources. These are inherited and if a parent policy is less restrictive, it overrides the more restrictive resource policy. Child policies cannot restrict access granted at parent level. IAM policies are
inherited from top to bottom, but billing is accumulated from bottom up. Resource consumption is measured in quantities like rate of use, number of items or feature use. Because a resource just belongs to one project, the project accumulates the
consumption of all its resources. A project is associated with one billing account, and an organization contains all billing accounts.
Organization Admin delegates privileges and access to individual projects to Project Creator. A project accumulates the consumption of its resources, it can be used to track resources and quota usage. Projects where billing is enabled, permissions are
managed, and services and API are enables, can track resource and quota usage. To interact with GCP resources, you must provide the project identifying information for every request. The project name is human-readalbe way to identify projects though
is not used by API; project ID generated unique; and project number automatically generated by server.
Resources are categorized as regional (External IP addresses), zonal (instances and disks) or global (images, snapshots, networks). Regardless into type, each resources is organzied into a project (logical instead of physical organization). Billing
and reporting is done per project.

<br>

---

<br>

## **Quotas**

All resources are subject to project quotas or limits. They are part of one of three categories:

- Resources per project (15VPC networks per project)
- API request rate in project (5 admin actions per second on Cloud Spanner)
- Resources per region (24 CPUs per region)

Even though we have these quotes, GCP allows to exand over time and increase accordingly to your usage. In case of an upcoming increase in usage, you can proactively request quota adjustments in Cloud Console. Even though they can be changes,t hey exist to
avoid runaway consumption in case of malicious or error attack (1). A quota might also prevent billing spikes (2) in case of creating 100 instances instead of 10 due to a typo. These are not the same as budget alerts. They are also used to force sizing
considerations and periodic review to go for cheaper alternatives (3).
Note that quotas limit the amount of resources that can be created but they do not guarantee that resources will be available.

<br>

---

<br>

## **Labels**

Allows more granularity for segregating and organizing resources. They can be attached to resources with Console, gcloud or API. Can be used to define the environment of the VM (test or dev) so we can search and list all production resources
for inventory purposes. They can also be used in scripts to help analyze costs or run bulk operations on multiple resources.
It is recommended adding labels based on teams or cost center (team: marketing, research, etc.) to distinguish components (component: frontend, redis, etc.), or environments (environment: prod, test, etc.). Can also be used to define the owner or primary contract for a
resource (owner: gaurav, contact: opm, etc.), or even the state of the resource (state:in-use, ready-for-deletion, etc.).
It is key to distinguish them from tags. Labels are user-defined strings in key-value format used to organize resources that are propagated through billing. On the other side, tags are user-defined strings applied to instances that are primarily
used for networking like applying firewall rules.

<br>

---

<br>

## **Billing**

All resources under one project accumulate into one billing account. To help project planning and controlling costs, you can set a budget that lets you track your spend growth towards an amount. For setting a budget, first you select a name, and choose
the projects to which they apply. Later, you set the budget at a specific amount of set it to previous month spend. Afterwards, you can set alerts that send emails to Billing Admins after the spend exceeds a percentage or specified amount of the budget. By default, it
will be sent at 50, 90 and 100%. Can also send an alertt when the send is forecasted to exceed the % of the budget amount by the end of the budget period.
Can use Pub/Sub to programatically receive spend updates about this budget. Can create a Cloud Function that listens to the PubSub topic and automates cost management.
The mail contains the project name, % of budget exceeded, and budget amount. Can also use labels to help optimize spend (instances across different regions incur in higher costs, so might consider relocating some instances or using caching service like Cloud CDN and
therefoe reduce networking traffic).
It is recommended to label all resources and exporting billing data to BigQuery to analyze spend. It is easy to create queries, and can also visualize spend over time with Data Studio.

<br>
<br>

# **Resource Monitoring**

## **GCP Operations Suite**

Stackdriver dynamically discovers cloud resources and apps based on deep integration with GCP and AWS. Access to powerful data and analytics tools plus third-party providers. Has services for monitoring, logging, error reporting, fault tracing and debugging.
You pay for what you use with free usage allotments. It works in a single, comprhensive and integrated service. To create reliable, stable and mantainable applications, Stackdriver supports a rich and growing ecosystem. Helps expand the IT Ops, security, compliance
capabilities to GCP customers. There are multiple integrations with third-party software providers.

<br>

---

<br>

## **Cloud Monitoring**

Important because it is at the base of SRE (Site Reliability Enginereeing). It applies software engineering to operations to create ultra scalable and highly reliable systems. It has enabled Google to build, deploy, monitor and mantain larg ecosystems. Stackdriver
dynamically configures monitoring after resources are deployed, and has intelligent defaults that allow to create charts for basic monitoring allowing to monitor your platflow, system and application metrics by ingesting data such as events, metrics and metadata.
You can generate insights with data through dashboards, charts and alerts. A workspace is the root entity that holds monitoring and information in Stackdriver monitoring. Can have between 1 and 100 monitored projects, and can hav as many workspaces as you want.
A workspace can access data from monitored projects, but the log entries remain in individual projects. The first monitor project is called hosting project and the name of the name becomes the name of the workspace. Allows to monitor all GCP projects in a single
place. There is an AWS connector to monitor AWS accounts. Stackdriver role assigned to one person on one project applies equally to all projects monitored by that workspace. So to give people different roles per different projects and to control visibility of data,
it is recommended to place the monitoring of projects in different workspaces.
Cloud Monitoring allows to create custom charts of metrics we want to control. They provide visibility into the utilization and network traffic. We can apply filters, remove noice, aggregate, etc. They can only provide insights in case someone is looking at them. In case
there is anyone, we mst create alerting policies that notify you in case some conditions are met. Can be notifies through email, SMS or other channels. Can create alerts when you approach the threshold for billing. Recommend alerting on symptoms and not causes, so for
example we might want to get notified for failing queries in a DB and later identify whether the DB is down, or there is another major issue. This avoids a single point of failure in alerting strategy. It is also recommended to customize alerts depending on the audience,
explaining the resources and actions to be taken. Also, avoid noise because this will cause alerts to be dismissed over time. Adjust them so they are actionable and not set it on everything possible.
Can create uptime checks that test the availability of public services. An HTTP check have a certain timeout, and are considered failures if no response is obtained in this period. You can also install a monitoring agent (CPU utilization, disk traffic, etc.). To access
additional resources and services this agent is recommended. It is supported by Compute Engine and EC2 instances.
If default metric provided by Stackdriver do not fit your needs, you can create your custom ones.

<br>

---

<br>

## **Logging**

Allows to store, analyze and search log data from GCP and AWS. Fully managed service that performs at scale and ingests app and system log data from thousands of VMs. Logging includes storage for logs, a GUI called the log viewer, and an API to manage logs programatically.
Lets you read and write log entries, seach, filter and create log-based metrics.
They are only retained for 30 days but they can be exported to GCS buckets, PubSub or BigQuery datasets. Exporting logs to Cloud Storage makes sense for more than 30 days. BigQuery allows to analize logs and even visualize them in Data Studio. It runs fast SQL queries on
GBs to PBs of data. Can better understand traffic growth for forecast capacity. Network usage to optimize traffic expenses (depending on IP addresses) or forensics to analyze incidents. Can visualize them with Data Studio and can convert raw data into metrics and dimensions
so can create reports. With ubSub, can stream logs to applications or end points. Like Stackdriver Monitoring agent, it is best practice to install the logging agent to all VM instances. Supported in Compute Engine and EC2 instances.

<br>

---

<br>

## **Error Reporting**

Counts, analyzes and aggregates the errors in Cloud services. There is a centralized error management interface that displays the results with sorting and filtering capabilities. You can set up real-time notifications when errors are detected. The exceptuon stack trace parser
is able to be processed in Go, Java, Node.js, PHP, Python and Ruby. Error reporting is able for App Engine Standard and beta for flexible, Compute Engine, Cloud Functions and EC2.

<br>

---

<br>

## **Tracing**

Integrated into GCP and important for overall performance to manage the timings of the apps to handle incoming requests and perform operations. Distributed tracing system:

- Collects latency data from apps and displays it in the console.
- Can track how requests propagate through your applications and receive detailes near real-time performance insights.
- Per-URL latency sampling

It automatically analyzes all app traces to generate depth latency reports from performance degradations from App Engine, HTTPS load balancers, and apps instrumented with Cloud Trace SDKs (Stackdriver Trace API).

<br>

---

<br>

## **Debugging**

Feature of GCP that allows to inspect the state of the running application in real time without stopping or slowing it down. The debugger adds less than 10ms to the request latency when the state is captured (not noticeable by users). This feature allows to understand the behavior of code
in production and analyze its state to locate hard to find bugs. With few clicks, can take a snapshot of running applications state (call stack and local variables), or inject a new logging statement (debug logpoints). It supports multiple languages like Java, Python, Go, Node.js or Ruby.
