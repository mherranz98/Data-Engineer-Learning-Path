<br>
<br>

# **Introduction: Preparing your Associate Cloud Engineer Exam 📚☁️**

---

<br>

## **Introduction and theoretical basis**

An associate Cloud Engineer is able to deploy, secure applications and infrastructure, monitor operations of multiple projects and mantain enterprise solutions to meet target metrics.
He is able to work with on-premise and cloud solutions, work with Cloud Console or command line interface for performing the basic routines. He is familiar with compute, storage, IAM to resources, and networking services in GCP.

On the contrary, professional level certifications expects the know how to evaluate case studies and design solutions to meet business requirements.
Migrating applications provides some advantages.

<br>

---

<br>

## **Setting up a Cloud Solution Environment**

Steps to be followed are:

- Setting up cloud projects and accounts (resource hierarchy, organizational policies, managing users and groups applying access management)
- Managing billing configuration
- Installing and configuring CLI

Resource hierarchy depends on the needs and structure of the organization. Folders for each division and each application are optional. There might be multiple projects underneath each application (CI/CD, Dev, Stag, and Production, for example). Will also need to grant organizational policies. Will also need to enable API within projects during setup. Will also need to grant members IM roles to ensure they have the right access to projects, depending on their job needs and their role in the company. Individuals will be added to a group, this eases permission management. Permissions are included in defined roles, which will be given access to groups. Will need to know how to manage users and groups in cloud identity, a service for managing users and groups.

<br>

---

<br>

## **Who can do What in Which resource?**

Can also set up project scoping, which is related to monitoring of some projects over others. Scoping projects monitor monitored projects. IT expenditure will be passed to operational expenses, and the departments associated with each application (projects) will be responsible for computing and storage costs. Will need to create a different billing account for each group and link each project to the appropriate account (just one account for project). Many projects can be linked to a single billing account.
Will need to set up custom billing projets and alerts for some departments. Each department will also need you to set up billing exports that can be used to track charges.
Can automate resource maangement tasks on the command line. Cloud SDK has a G-Cloud command set that allows configuration of GCP resources as an script. Can also use "gcloud config set" to configure default options of project and compute region. SDK will use these default simplifying further the code.

<br>

---

<br>

## **Planning and Configuring Cloud Sloutions**

To plan solutions we have to assess:

- Transactional or analytical data processing
- Relational or non-relational data
- Provide connectivity or internal components for private network
- Protect applicant network or system outages
- Amount of data to be transmitted

<br>

---

<br>

## **Deplying and Implementing a Cloud Solution**

Expected to implement specific computing solutions (Compute Engine, KGE, etc.). Need to understand availability, concurrency, conectivity and access options. Also storage with relational and no-SQL data structures, with analytical or transactional use cases, optimized for low latency and global availability.
Marketplace for specific software need to support on Compute Engine instances, no need to reinvent the wheel. For devops practice, deploy infra in a declarative way with configuration files. This (IaC) reduces human error and speeds up resource allocation.
To use GCP, we can use Google Cloud Console, a GUI where we can specify the configuration and settings of the resources for each project. We can also use CLI (command-line interface) where in a fast way we can access and configure resources available in GCP. For this, we can use Cloud SDK on your local machine, or Cloud Shell, a cloud based terminal with G-Cloud CLI (desktoplike).

<br>

---

<br>

## **Ensuring Successful Operation of a Cloud Solution**

Once deployed and implemented the solutions. One must know how to work with compute, storage and networking resources in GCP. Needs the skills to manage the resources of the solution as well as monitoring and logging. Upgrading the OS, A/B testing of capability upgrades, change disk type can be modifications on Compute Engine VMs. Need to make sure that the change is propagated to al VM in the isntance.

<br>

---

<br>

## **Configuring Access and Security**

Application uses Google Cloud Network. Must be able to manage IAM in GCP (projects and accounts), familiar with service accounts, know how to access audit logs.
For a certain app that uses Cloud SQL as a backing data store, a service account attached to the virtual machine that runs it is designed to enable machine-machine communications. To do so, first we must create the service account, secondly assign permissions to it, finally attach this service acccount to a Compute Engine VM. This attachment allows the VM and all the apps running on it to use the permissions assigned to this service account.
First go to desired project, open Service Account tab in IAM & Admin, then Create Service Account. In the dialog name account and the email associated with it.
Once created, the account will be added to the list of all service accounts. On three-dots on right, select Manage permissions, Add permissions to it.
Copy the service account email address identifier and search to borwse the permissions to find the ones you need to add. Finally, when you add your VM isntance, you can also add the service account to it under the identity and API access section. Authentication should be the next step.
