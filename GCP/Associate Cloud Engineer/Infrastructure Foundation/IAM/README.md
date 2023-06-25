<br>
<br>

# **Infrastructure Foundation: Identity and Access Management📚☁️**

---

<br>

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
