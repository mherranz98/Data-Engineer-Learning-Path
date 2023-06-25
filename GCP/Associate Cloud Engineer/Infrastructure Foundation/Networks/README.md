<br>
<br>

# **Infrastructure Foundation: Introduction to Projects and Networking📚☁️**

---

<br>

Compute Engine is a IaaS that let's you deploy applications by means of VMs that you can configure and manage. This will be the scope of this course. App Engine is a PaaS fully managed service that lets you deploy applications in microservices
without dealing with infrastructure. On the other side, there is Cloud Functions a complete serverless service (like Cloud Run).

<br>

---

<br>

## **Interacting with GCP**

Explore GUI and command-interface. There are 4 ways to interact with GCP; Console, Shell and SDK, REST-based API, Cloud Mobile App. Console is a GUI where we can view details in a user-friendly interface. We can open Cloud SDK, a command-line
find on the top right part of the GUI. In the GCP console, we can click the three horizontal lines that open the menu with services. Now, we can choose the service we want to work with.
In addition to SDK or Cloud Shell, one can use client libraries for accessing GCP services. These are available with most popular languages (Java, Python, Node.js, Ruby, Go, PHP, etc.). Client libraries expose APIs for two puroposes; App APIs
allows to access the services, and Admin APIs offer functionality for resource management. OAuth 2 is used for all authentication. GET, POST, PUT and DELETE return a json.
Cloud Mobile App allows to manage services from IOS or Android device. We can start, stop and SSH VM instances, set up customizable graphs for resource management with important metrics, etc, manage billing, manage apps in App Engine, etc.

<br>

---

<br>

## **Projects**

Resources can only be created and consumed within projects. Projects isolate resources from one another. Can switch context between projects. To create a project we can click on project name on top and Create Project, then define a project
name, an id will be created. Some services might not be initially available, after switching projects, we can go to settings and shut it down (shut will take 30 days). We can go home, select a project, and start working.
Going to Cloud Shell inside a project, we can use the command "gcloud config list command" to give more information about the configuration we have. Even though changing the project of the Console, the shell will still be located in the previous
project. To swap back and forth, we must get the Project ID and paste the following command "gcloud config set project $projectID" where the variable $projectID has been previously defined with command "export projectID=<projectID>". We will
see that the project displayed in the shell will change. This is switching context between projects.

<br>

---

<br>

## **Virtual Networks**

GCP uses a software defined network built on a global fiber infrastructure. We must think about resources as services instead of as hardware. On a high level, there are regions (geographical location where you can run your resources). Regions are
then followed by zones, most of them having 3 of these. PoPs are where Google's network is connected to the rest of Internet. GCP can bring traffic closer to peers because it operated with global network of interconnection points, reducing
cost and a better user experience. Network connects regions and PoPs, and is composed of a global network of fiber optic cables.

<br>

---

<br>

## **VPC**

GCP allows to provision resources and connect them between each other and isolate from each other in a VPC. One can also define fine-grained network and policies within GCP and between GCP and on-premises. VPC is a comprehensive set of Google managed
networking objects. Projects hold networks. Networks come in three flavors: default, auto mode and custome mode. Subnetworks allow to divide or segregate the environment.
Regions within zones represent datacenters that provide Datab protection and high availability.

<br>

---

<br>

## **Projects, networks and subnetworks**

Projects are the key organizer of infrastructure resources in GCP. A project associates services with billing. Projects contain entire networks. The default quota for each project is five networks. Can also request more with Console. These networks can be
shared with other projects, or be peered with other project networks. These networks don't have IP ranges but are a construct of all individual IP addresses and services within a network.
GCP networks are global, spanning all available regions. Inside a network, you can segregate resources by regional subnetworks.
With regards to network flavors, each project is provided with a default VPC network with preset subnets and firewall rules. These preset rules are:
-A subnet for each region with non-overlapping CIDR blocks
-Allow ingress for traffic for ICMP, RDP and SSH traffic from anywhere, and ingress traffic from within the default network from all protocols and ports.
In auto mode netowork, one subnet from each region is created. The default network is actually a auto mode network. These subnets use a set of predefined IP ranges with mask /20 that can be expanded to /16 mask. All these subnets fit within the 10.128.0.0/9
CIDR block. As new regions become available, new subnets in these will be added to auto mode networks using the IP range from that block.
A custom mode does not create subnets automatically, so it provides you with complete control over its subnets and IP ranges. Decide subnets to create, in which regions and which IP ranges. These IP ranges cannot overlap with subnets of the same network. Can convert an
automode network to custom to take advantage of the control that custom mode networks provide, but this is just a one-way conversion.  
Example, project with 5 networks expanding multiple regions. Each net has several VMs, because they are in the same net, they can communicate with internal IP addresses even though they are in different regions (global optic fiber). On the
contrary, different nets, even though VMs are in the same region, they must communicate with external IP address. Communication will not go through the public Internet but rather the Google Edge Routers.
A single VPN can connect on-premise net with Cloud VPC network. In case VPC instances are in different regions, they can communicate with the on-premises and within them they can use private network by means of a VPN Gateway reducing cost
and net management. Subnetworks can extend zones within the same region. A subnet is an IP address range that can be used. The two first are reserved for network gateway and subnet's gateway, making .2 and .3 assigned to two VM instances. The last
two addresses are known as the broadcast.
Two VMs withing a single subnet can communicate using the same IP subnet address even though being in different zones. This implies that same firewall rules apply.
GCP VPCs allow to increase the IP address space of any subnet without any workload shutdown or downtime.
Important points: - The new subnet mask cannot overlap with any subnet in the same VPC in any region. - Each IP range for all subnets in a VPC network must be a unique valid CIDR block. - The new subnet IP ranges are regional internal IP addresses and have to fall within valid IP ranges - Subnets ranges cannot match, be narrower, or be broader than a restricted range - Subnet ranges cannot span a valid RFC range and a privately used public IP address range - Subnet ranges cannot span multiple RFC ranges. - The new subnetwork range must be larager than the original (prefix length must be a smaller number -> cannot undo an expansion) - Automode subnetworks start with a /20 IP range, and they can be expanded to a /16 . Alternetively, can convert the auto mode to custo to further increase the IP range. - Avoid to create large subnets as they are mode likely to cause CIDR range collisions when using Multiple Network Interfaces and VPC Peering or when configuring a VPC or other connections to on-premises. Do not scale beyond what
you actually need.

<br>

---

<br>

## **IP Addresses**

In GCP, each VM can have two IP addresses assigned. One internal assigned via DHCP internally. All VM that starts in any service (App Engine, GKE) has an internal IP address assigned. When a VM is created, its symbolic name is registered with
an internal DNS service that translated the name to an internal IP address. The DNS is scopted to the network, so it can also translate web URLs and VM host names in the same network, but not in different networks.
The external IP address is optional in case it the VM is externally facing. The external IP address can be assigned from a pool, making it ephemeral; or on the contrary it can be assigned from a reserved external IP address making it static.
Reserved (also known as static) external IP addresses not assigned to a resource are charged at a higher rate that static external IP addresses in use (assigned) or ephemeral external IP addresses.
Can use own publicly routable IP addresses as GCP external IP addresses abd advertise them on the Internet. By default, exteral IP addresses are ephemeral.

<br>

---

<br>

## **Mapping IP addresses**

External address is unkown to the OS of the VM. It is mapped to the VMs internal address by VPC.
Lets explore the DNS resolution for internal and external addresses. For the internal, each instance has a host name that can be resolved to an internal IP address. There is also a FQDN (Fully Qualified Domain Name) for each instance. If one
deletes and recreates an instance, the intenal IP address can change, which can lead to disruptions of connection from other Compute Engine resources that need to obtain the new IP address before connecting. However, the DNS name always points
to a specific instance no matter the IP address is. Each instance also has a metadata server that acts as a DNS resolver for that instance. This server handles all DNS queries for local network resource and also routes all other queries to
Google's public DNS server for public name resolution. An instance is not aware of any external IP address assigned to it. Insteadm the network stores a lookup table that matches external IP addresses with internal IP addresses of relevant instances.
With regards to external addresses, this allow connections from hosts outside the project. Public DNS records pointing to instances are not published automatically; however admins can publish using existing DNS servers.
Domain name servers can be hosted on GCP, using Cloud DNS. This is a managed service.
Cloud DNS is a scalable, reliable and manage authoritive Domain Name System service running on the same infrastructure as Google. This service translates requests for domain names like google.com into IP addresses. It uses Google's glboabl network
of Anycast name servers to serve DNS zones from redundant locations proiding low latency and high availabliity (100% SLA for domains configured in Cloud DNS -> veruy important).
Do not need to manage your own DNS servers or software. Instead, you can use a GUI, command-line or API.
Another networking feature of GCP is Alias IP Ranges that let you assign a range of internal IP addresses as an alias to a virtual machine's network interface. Useful with multiple services running on a VM, and want to assign different IP
addresses to each service. Can configure multiple IP addreses representing different containers in a VM without having to define separate network interface.

<br>

---

<br>

## **Routes and firewalls**

By default every network has routes that let instances in a network send traffic directly to each other, even across subnets. Default route directs packets to destinations that are outside the network. These routes cover most of the normal needs,
but you can also create special ones that overwrite these.
Firewall rules allow the packet. The default network has pre-configured firewall rules that allow all isntances in the network to talk to each other. Manually created networks don't have these firewalls by default, so they must be created.
Routes match packets bt destination IP addresses. However, no traffic will flow without matching a firewall rule (default least priority allow traffic).  
A route is created whan a network is created, enabling traffic delivery from anywhere. A route is also created when a subnet is created. This enables VMs on the same network to communicate. Each route in the Routes Collection tab apply to one
or more instances if network (not IP address -> When a VM is created with a matching tag, the firewall rules apply irrespective of the IP address it is assigned) and tags are the same. If there is no tag, all routes apply to all isntances within the same network.
Firewall rules protect VM instances from unapproved connections (inbound or outboud, ingress or egress respectively). VPC network functions work as a distributed firewall. Firewall are applied to the network as a whole but connections are allowed
or denied at an instance level. Firewalls are statefull (connection allowed, subsequent traffic will be allowed -> bidirectional communication once a session is established). If all fireall rules are deleted, there is an implied rules of
deny all ingress and allow all egress.
Firewall configuration as a set of firewall rules with following parameters: - Direction: egress or ingress - Source or destination for ingress and egress directions - Protocol and port - Action meaning allow or deny - Priority: first matching rule with higher priority is applied - Rule assignment to assign to certain instances
Egress firewall rules control outgoing connections originated inside GCP network. Allow rules allow outbound connections that match destionation (IP CIDR ranges to protect from undesired connections initiated by VM instances towards an external
host. Can also to prevent undersired connections from internal VM instances to specific GCP CIDR ranges VM inappropiately connecting to another VM in same network), protocol and port rules.
Ingress rules protect from incoming connections to the instance from any source. Allow rules allow specific protocol ports and IP ranges to connect. The firewall prevent isntances from receiving connections from specific ports and protocols. Can
also be forced to apply to specific sources (external network or GCP IP ranges).

<br>

---

<br>

## **Pricing**

Ingress is not charges unless comming from a load balancer processing ingress traffic. Egress to same zone is not charged as far as it is through the same internal IP address of an instance. Egress to Google Products (YouTube, Maps, etc.) is not
charged. There is a charge for egress between zones in the same region, in the same zone using external IP address, and between regions (Canada and US regions have different price from rest).
Also charged for external IP addresses. Static IP address assigned but unused (0.01), static and ephemeral in use on standard VM (0.004) and static and ephemeral un use on preemptible VM (0.002) per hour. When attached to forwarding rules, they are
not charged.

<br>

---

<br>

## **Common Network Designs**

-Increased Availability with multiple zones -> same security management complexity, within same subnetwork (firerules to same subnetwork), provides isolation for many types of infrastructure, hardware and software failures
-Globalization with multiple regions -> provides even a higher degreee of failure independence. Build robust systems, with resources spread across different failure domains. With HTTP load balancer, can route traffic to instance closer to user, resulting
in better latency and lower network traffic costs.
As a general security best practice, only assign internal IP addresses to VM instances whenever possible. Google NAT is a Google managed network address translation service that allows instances accessing the internet for updates, patching, configuration
management, etc. without public IP addresses and accessing the public internet in a controlled and efficient manner. Allows also to implement restrictions on inbound NAT, meaning that hosts ourside VPC network cannot access directly the instances behind the NAT
gateway.
Similarly, you should enable private Google access to allow instances that only have internal IP addresses to reach the external IP addresses of Google APIs and services. You enable Google access on a subnet by subnet basis. This allows instances
that don't have public IP addresses but are in a subnet where Google private access is enabled to access Google APIs and services, as well as the internet. If they have external IP addresses, this service has no effect as they already have access to these services.

<br>
<br>
