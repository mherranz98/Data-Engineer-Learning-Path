<br>
<br>

# **Infrastructure Foundation: Virtual Machines in Compute Engine 📚☁️**

---

<br>

VM are most common infrastructre component. Not exactly a hardware computer. VM include memory, disk storage, CPU and IP address. Similar to physical hardware, but these can have micro VM that share CPU with other VMs offering less capacity
at a lower cost. Also some VMs offer burst capability meaning that the virtual CPU will run above its rated capacity for a brief period of time using available shared CPU.

<br>

---

<br>

## **Compute Engine review**

IaaS that supports any language, with any generic workloads as primary use case (enterprise app designed to run on a server infrastructure). Has utmost flexibility compared to other computing services, can decide how to manage, how to autoscale,
etc. Makes Compute Engine very portable and easy to run in the cloud.
Compute Engine is physical servers running inside GCP environment with a number of configurations. Predefined and custom machine types allow to decide memory and CPU. Choose the type of disk you want (can be a mix). Can configure the networking
interfaces and run a combination of Linux and Windows machines. There are many features that will be later discussed.

<br>

---

<br>

## **VM access**

The creator on an instance has full root privileges on it. A Linux insance creator has SSH capabilities and can grant these to others. On a Windows, the creator can create a username and password to connect to the insance using Remore Desktop Protocol,
or RDP client.
The lifecycle of a VM is represented by different statuses:
-After clicking Create button, we enter the Provisioning stage. Reources (CPU, memory and disks are being reserved) but this is not running
-Staging is where the instance is prepared for launch. Adds IP addresses, boots the system image (from Google Storage), and the system itself.
-In the Running stage, it will go through the pre-configured startup scripts and enabling SSH or RDP access
-Some actions can be performed while the VM is running (move to different zone, take a snapshot of persistent disk, reconfigure metadata, etc.); others require the VM to stop (upgrade the machine adding more CPUs). For stopping,
the machine will go through pre-configured shutdown scripts and it will end up in the Terminated status. From here, we can choose to restart the instance and bring it back to the provisioning stage, or delete it.
There is also the option of reset a VM, which wipes the memory contents and resets the VM to the original state. Instance remains running.
With regard to the methods, some are performed from the OS of the VM (reboot and shutdown) and others from gcloud commandline (stop, restart, delete). Restarting, rebooting, stopping and deleting an instance, can take about 90 sec. For preemptible
VMs, it does it automatically after 30sec.
Compute Engine can migrate VM to another host due to maintaince event to prevent exeriencing disruptions. The VM availability policies determines how the instance behaves in such an event. By default, it will live migrate, but you could terminate
the instance. Likewise, if terminated due to crash or mantainance, it will automatically restart, which can be also changed.
With regard to the OS updates, when provisioning a premium image, there is a cost for the image usage and the patch management. With Google Cloud, we can easily manage OS patches effectively keeping it up-to-date and reducing security vulnerabilities.
Long-running VM require perioid c system updates to protect against defects. OS patch management service has two component: patch compliance reporting (reports insights of patch status of VM instances), patch deployment automates the OS update
process. A patch job runs across instances. There are some settings that can be configured:
-Select what patches to apply (patch approvals)
-Set up flexible scheduling
-Advanced patch configuration settings (pre and post patching scripts)
-Manage patch jobs from a centralized location
When VM is terminated we still have to pay for reserved external IP addresses and attached disks, but not the memory or vCPUs.
Availabilty policies can be changes while the instance is running. In the terminated state, we cannot change the image of an stopped VM. Will thus need to delete and recreate.

<br>

---

<br>

## **Compute Engine Options**

Focusing on CPU and memory. Three options: console, cloud shell, or rest API. For complex configurations, might want to use programatically the REST API and define different optios for the environment. First configure throught the console,
and then with the command-line equivalence, automate it avoiding typos.
Machine family -> machine series -> machine type. When creating an instance, we choose a predefined or custom machine type from the preferred machine family. Alternatevely, we can create custom machine types. These let you specfici number of vCPUs
and he amount of memory for the instance. Machine families are optimized for their specific purpose.
There are four machine families: general-purpose, compute-optimized, memory-optimized and accelerator-optimized.
The general-purpose machine family has the best price-performance with flexible vCPU to memory ratios and provides features that taget most standard and cloud-native workloads.
-E2 machine series is suited for day-to-day computing at low cost, especially when there are no dependencies on specific CPU architecture. These provide a variety of resources for the lowest price. Need to pick the vCPU and memory
desired. Standard E2 VMs have between 2 to 32 vCPU with 0.5 to 8 GB of memory per vCPU. Great choice for small-medium DB, web servers, app servers, etc. Good for cases wher ethere are no strict perfromance requirements.
E2 machine series also contains shared-core machine types that use context-switching to share a physical core between vCPUs for multitasking. Shared-core machines can be more cost effective for running small. non-resource intensive
applications than standard, high-memory, or high-CPU machine types. They have between 0.25 to 1 vCPUs (unlike physical infrastructure that is indivisible) with 0.5 to 8 GB per vCPU.
-N2 and N2D are next generation following N1. These provide a balanced price/performance as they offer a significant performance jump. They are the most flexible VM types. Good for medium-large DB. Have sustained discounts.
-Tau T2D optimized for cost-effective performance for demanding scale-out workloads (web seervers, containereized microservices, media transcoding and large-scale Java apps). These come in predefined VM shaped, with up to 60vCPUs
and 4GB of memory per vCPU. Supported by GKE to optimize price-performance.
Compute-optimized machine family has the highest performance per core on Compute Engine and oprimized for compute-intensive workloads.
-C2 best fit VM type for compute-intensive workloads. Best suited for HPC, AI, Ad serving, gaming, high-performance web serving, media transcoding, etc. Also apps with expensive per core licensing as performance per core is optimized.  
 Offer up to 3.8 GHz sustained all-core turbo with full transparency. From 4 to 60 vCPUs and up to 240 GB of memory. Can attach up to 3 TB of local storage.
-C2D largest VM sizes best-suited for HPC, have largest LLC (last-level cache) cache per core. From 2 to 112 vCPUs and offer 4 GB of memory per core. Can attach up to 3TB of local storage if require high storage performance.
Memory optimized machine family offer the most compute and memory resources of any machine. Ideal for workloads that require higher memory-to-vCPU ratios than the high-memory machine types in the general-purpose. Large in-memory databases
Lowest cost per GB of memory; good choice for workloads that use high memory configurations with low computing resource requirements. Offer sustained-use discounts and additional savings for 3-year commitments.
-M1 up to 4 TB of memory
-M2 up to 12 TB
Accelerator-optimized family ideal for massively parallelized CUDA (compute unified device architecture) workloads like ML and HPC. Optimal if require GPUs.
-A2 has from 12 to 96 vCPUs and up to 1360 GB of memory. Have a fixed number (up to 16) of NVIDIA GPUs providing 40GB of memory, ideal for language models, databases, and HPC
In case none of the prefefined machine types match our need, we can specify the number of vCPUs and amount of memory. Ideal for workloads that require more processing power or memory, or that don't fit the predefined. Cost is slightly higher
and there are some limtiations: only machines with 1 vCPU or an even number of it can be created, and memory must be between 0.9 to 6.5 GB. The total memory og the instance must be a multiple of 256MB. Using extended memory, you can get more
memory per vCPU beyond the 6.5 limit, at an additional cost. First thing we need to consider for creating and running resources is the region and zone. The instance will use the default processor of the zone.

<br>

---

<br>

## **Compute Pricing**

- All vCPUs, GPUs and GB of memory are charged a minimum of 1 minute.
- Compute Engine uses a resource-based pricing model where resources (vCPUs, etc.) are billed separately. Will still create instances using predefined machine types but bill reports them as individual vCPUs and GB of memory.
- Several discounts available:
  - Resource-based pricing allows to apply sustained use discounts in a region collectively rather than individual machines
  - For stable and predictable workloads, can discount off of normal prices commiting to a usage term of 1 year or 3 years. Up to 57% for custom machine types and most of predefined, and up to 70% for memory-optimized
    family machines
  - Preemptible and Spot VMs are instances than can create and run at a much lower price. Both might terminate if Compute Engine requires to access resources. These machines are excess of Compute Engine capacity thereby their
    availability varies with usage. Preemptible have a maximum runtime of 1 day whilst Spot don't have any.
- There is recommendation engine that will notify you for resizing the machine to further optimize resources. This will appear 24hrs after the instance has been created.
  With regard to the sustained discounts, Compute Engine gives an incremental net discount for instances running a given % of the month, which increases with use. In the first day of the month, discounts are reset, so it is recommended to
  create them by this time. It is based on vCPU and memory usage across each region and separately for custom and predefined categories. Up to 30% net discount for instances that run the entine month.
  For example, given an upgrade of resources in mid of the month, Compute Engine breaks down to individual resources and combines their usage to qualify for the largest sustained usage discounts possible leading to the following: initial
  resources for all month + added resources for half month.

<br>

---

<br>

## **Special Compute Configurations**

Preemptible - Run at much lower cost (up to 91%) -> check whether can make app function completely on preemptible VMs - Might be terminated at any time: no charge if terminated in first minute, 24 maximum runtime, only get 30 sec notification before the instance is preempted - No live migrations to standard VMs nor automatic restarts, but can create mmonitoring and load balancers that start up new ones in case of failure - Major use case is for running batch processing jobs. If terminated, the job slows but does not completely stop (parallel computing) -> can complete batch processing tasks without placing additional workload on existing resources or
paying full price of normal instances
Spot - Latest version of preemptible - VM isntances with spot provisioning model. - Uses the same pricing model as preemptible - Provides new features compared to preemptible: don't have a maximum runtime. - Chance of stopping VMs for a system event is low but might change from day to day and from zone to zone depending on current conditions - Like preemptible, they cannot live-migrate to become standard VMs while running or be set to automatically restart in case of a mantainance event - Resources for spot VMs come out of excess and backup of GCP resource capacity. As good practice, easier to get for smaller machine types with less resources
Sole-tenant nodes to isolate workloads - Physically server dedicated to hosting VM instances only for a specific project. Used to isolate or to group instances in other projects, or from the same when having to meet compliance requirements. - Can also fill the node with multiple smaller VM instances of varying size, including custom machine types and with extended memory. - Can bring-your-own OS license minimizing the physical core usage with the inplace restart feature.
Shielded to verify integrity - Secure boot haven't been compomised by boot or kernel-level malware of rootkits - Virtual trusted platform module (vTPM) help prevent data exfiltration - Need to select a shielded image
Confidential encrypt data in use - Encrypt data while being processed -> can collaborate with anyone while preserving data confidientality - Easy to use with no changes to code or performance downtimes - Type of N2D VM running on hosts based on second generation of Epyc processors. Using AMD SEV (Secure Encrypted Virtualization), they are optimized for both performance and security for enterprise-class high memory workloads - AMD processor optimized for compute-heavy workloads, high memory capacity, high throughput, and parallel workloads - Can be selected this option when creating a new VM instance (consol, commandline and API)

<br>

---

<br>

## **Images**

Consists of boot loader, OS, file system structure, software and customizations. Can select: - Public image: can choose from Linux or Windows. Some of these are premium and have per second charges after one minute, excep SQL Server that has a 10 minute minimum. Premium images vary with machine type, however these prices are
global. - Custom image: create a new image of preconfigured and installed SW, can import images from on-prem, workstation or another cloud with no cost. There are some management features like sharing, image family and deprecation
A machine image is a resource that stores all the configuration, metadata, permissions and data from one or more disks required to create a VM. Can be used in mantainance scenarios (creation, backup, recovery and instance cloning). This is
the most ideal resource for disk backup and instance cloning and replication. For example, persistent disk snaptshot, custom image and instance template do not support all these features.
<br>

---

<br>

## **Disk options**

The OS will be included as part of a disk. Every VM comes with a single root persistent disk. In it, there will be the image we previously talked about. This image is bootable and durable (survives if instance terminates). Need to disable the
"Delete boot disk when instance is deleted" option. But there are several types of disks. - Persistent disk: - Attached to VM through network interface. It's persistent but not physically attached to machine, which allows the disk to survive if the VM terminates. - Can perform snapshots (incremental backups). - Choice between SSD and HDD will depend on price and performance balance. - Can be dynamically resized when running and attached to a VM. - Can also attach a disk in read-only mode to multiple VMs, so there is no need to replicate data (cheaper). Allows to share static data between VMs. - Zonal persistent offer efficient, reliable block storage. Regional persistent provide disk replication across physical disks in two zones in the same region. Regional also provide durable storage that are synchronously
replicated across zones. These are good choice for high-performance DB and enterprise apps that require high availability. Will have to choose: - pd-standard: backed by an HDD - pd-ssd backed by SSD - pd-balanced: backed by SSD. Alternative to SSD persistent disks that balance performance and cost - pd-extreme: zonal persistent disks backed by SSD and designed for high-end DB workloads, consistent high performance for both random access workloads, and bulk throughput. Can provide IOPS - By default, Google encrypts all data on rest. Can also control encryption (cloud key managed service, or create and manage our own encryption keys) - Can attach up to 16 persistent disks in shared-cored machine types, and up to 128 for the rest (standard, high-memory, high-CPU, memory-optimized, compute-optimized). - Local SSD disks: - Physically attached -> ephemeral - More IOPS, low latency and higher throughput than persistent disks - Up to 8, with 375GB per disk, total of 3TB - Data will survive reset but not stop or terminate as disks cannot be reatached to different VM - RAM disk: - tmpfs to store data in-memory - Faster than local SSD disk - Very volatile, it erases on stop or restart - Might need to use a larger machine type - Consider using a persistent disk to back up data on RAM disk
Throughput is limited by the number of cores. Throughput also shares the same bandwidth as Disk I/O, so if we want to have a high Disk I/O throughput, it will also compete with any network egress and ingress throughput. This is especially
relevant when increasing the number of drives attached to a VM.
The main differences between a physical hard disk in a computer and a cloud persistent disk: - Compute hardware disks have to be partitioned. Take a part for OS, and in case you want to grow it, you need to repartition. Also if you want to make changes, you need to reformat - For computer disks, if you want redundancy, you might need to create a redundant disk array - For computer disks, if you want to encrypt data, you must do it before writing it to the disk. - With cloud persistent disks, all the management is handled by GCP - Cloud disks can be resized because these are virtual network devices - Redundancy and snapshot are built in and automatic encryption is performed.

<br>

---

<br>

## **Common Compute Engine Actions**

Metadata and scripts
Every instance stores metadata on a metadata server. Useful in combination with startup and shutdown scripts because yyou can use the metadata to programatically get unique information about the instance without further authorization.
Default metadata keys are the same for every instance, so we can reuse the same script keeping it less brittle.
Retrieving and storing metadata from instances is very common. It is recommended to store these scripts in Cloud Storage.
Move an instance to a new zone
Do so for geographical reasons or due to a zone deprecation. Can be moved even if VM instance is TERMINATED state, or shielded VM. Can move within the same region ot between regions: - Automated process (same region): using the "gcloud command instances move" command. Must first shutdown, move to destination zone or region, and then restart it. Must then update any references (target VMs or target pools) that point
to the previous VM - Manual process (different region) must follow the process: first, make a snapshot of all persistent disks on source region; create new disks in destination zone restored from snapshots; create VM in destination zone and attach the new
persistent disks to it; assign a static IP; update any reference to the previous VM; and finally, delete the original VM, its disk, and the snapshot.
Snapshots
Have multiple use cases: - Backing up critical data into durable storage solution to meet application, availability and recovery requirements (Cloud Storage) - Migrate data between zones like previously discussed manual, but in this case also within the same region - Transfer to HDD to SSD to improve performance
A disk snapshot is not available for local SSD, just persistent disks. Different from images, which are used to create isntances or instance templates. Snapshots are useful for periodic of dtaa in persistent disks. Are incremental and automatically
compressed. Faster and lower cost that regularly creating a full image of the disk. Can be restored to new persistent disk (like explained in the second use case)
Resize persistent disk
Improve I/O performance. Can be done when attached and without having to create a snapshot. Can never shrink in size, just grow.
