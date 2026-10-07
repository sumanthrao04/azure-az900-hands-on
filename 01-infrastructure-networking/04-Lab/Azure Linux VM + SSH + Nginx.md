# Lab 4 — Azure Linux VM + SSH + Nginx

## Overview

In this lab, I deployed an **Ubuntu Linux Virtual Machine in Microsoft Azure**, connected it to the network created in Lab 3, accessed the VM using SSH, installed Nginx, and hosted a custom web page.

The main objective was to understand how Azure compute and networking components work together to host an application.

---

# Architecture

```text
                     Internet
                        |
                        |
                   Public IP
                        |
                        v
              +------------------+
              |       NSG        |
              | az900-web-nsg    |
              |                  |
              | SSH  22  Allow   |
              | HTTP 80  Allow   |
              +--------+---------+
                       |
                       v
              +------------------+
              |    Azure VNet    |
              |    az900-vnet    |
              |   10.0.0.0/16    |
              +--------+---------+
                       |
                       v
              +------------------+
              |    web-subnet    |
              |   10.0.1.0/24    |
              +--------+---------+
                       |
                       v
              +------------------+
              |    Linux VM      |
              | az900-linux-vm   |
              |     Ubuntu       |
              +--------+---------+
                       |
                       v
              +------------------+
              |      Nginx       |
              |     TCP 80       |
              +--------+---------+
                       |
                       v
                 Custom Webpage
```

---

# Resources Used

| Resource          | Purpose                                  |
| ----------------- | ---------------------------------------- |
| Resource Group    | Organize Azure lab resources             |
| Azure VNet        | Private network for Azure resources      |
| Subnet            | Network segment for the web VM           |
| NSG               | Control inbound/outbound network traffic |
| Public IP         | External connectivity to the VM          |
| Network Interface | Connect VM to Azure VNet                 |
| Linux VM          | Compute resource                         |
| Ubuntu            | Linux operating system                   |
| SSH               | Remote Linux administration              |
| Nginx             | Web server                               |

---

# 1. Azure Virtual Machine

An Azure Virtual Machine provides compute capacity in Azure.

For this lab, I deployed an Ubuntu Linux VM:

```text
VM Name:
az900-linux-vm
```

The VM was deployed inside the existing network:

```text
az900-vnet
     |
     v
web-subnet
     |
     v
Network Interface
     |
     v
az900-linux-vm
```

Azure Virtual Machines are an example of **Infrastructure as a Service (IaaS)**.

With IaaS, Azure manages the underlying physical infrastructure while I am responsible for areas such as the guest operating system, installed software, application configuration, and relevant security configuration.

---

# 2. VM Image

A VM image provides the operating system used to create the Virtual Machine.

For this lab, I selected an Ubuntu Server image.

Examples of VM images available in Azure include:

```text
Ubuntu Server
Windows Server
Red Hat Enterprise Linux
SUSE Linux
```

The image allows a VM to be provisioned with an operating system already installed.

---

# 3. VM Size

Azure VM sizes determine resources and capabilities such as:

```text
CPU
Memory
Network performance
Storage capabilities
Cost
```

For this learning environment, a small VM size was selected because the workload only needed to run a lightweight Nginx web server.

This demonstrated that VM sizing should be based on workload requirements and cost.

---

# 4. Network Interface

The VM uses a Network Interface (NIC) to connect to the Azure Virtual Network.

```text
Azure VNet
     |
     v
web-subnet
     |
     v
NIC
     |
     v
Linux VM
```

The NIC provides the network connection between the VM and the VNet.

---

# 5. Private IP Address

The VM received a private IP address from the `web-subnet`.

The subnet address range was:

```text
10.0.1.0/24
```

Therefore, the VM received an address within that subnet range.

The IP configuration was inspected from Linux using:

```bash
ip addr
```

Private IP addresses are primarily used for communication between resources inside private Azure networking.

---

# 6. Public IP Address

A Public IP was configured so that the VM could be reached from outside the Azure VNet when the appropriate NSG rules permitted the traffic.

The administration path was:

```text
Administrator
      |
      | Internet
      v
Public IP
      |
      v
NSG
      |
      v
Linux VM
```

The Public IP was used for SSH access to the VM.

---

# 7. Network Security Group

The NSG configured during Lab 3 controlled network access to the workload.

The important rules for this lab were:

| Protocol | Port | Purpose |
| -------- | ---: | ------- |
| TCP      |   22 | SSH     |
| TCP      |   80 | HTTP    |

The traffic flow can be represented as:

```text
Internet
   |
   v
Public IP
   |
   v
NSG
   |
   +---- TCP 22 ----> SSH
   |
   +---- TCP 80 ----> HTTP
   |
   v
Linux VM
```

For SSH, access should be restricted to trusted source IP addresses whenever possible rather than exposing port 22 broadly to the internet.

---

# 8. SSH

SSH was used to remotely connect to the Linux VM.

The connection flow was:

```text
Local Machine
     |
     | SSH TCP 22
     v
Public IP
     |
     v
NSG
     |
     v
Linux VM
```

Example command:

```bash
ssh -i az900-linux-key.pem azureuser@<PUBLIC-IP>
```

SSH key-based authentication was used instead of a password.

The private key should never be committed to a Git repository.

A `.gitignore` entry can be used to help prevent accidental commits:

```text
*.pem
```

---

# 9. Verify Linux VM

After connecting successfully through SSH, I verified the Linux environment.

Check current user:

```bash
whoami
```

Expected:

```text
azureuser
```

Check hostname:

```bash
hostname
```

Check operating system:

```bash
cat /etc/os-release
```

Check network interfaces:

```bash
ip addr
```

These commands helped verify the operating system and network configuration of the Azure VM.

---

# 10. Install Nginx

First, the Ubuntu package information was updated:

```bash
sudo apt update
```

Nginx was then installed:

```bash
sudo apt install nginx -y
```

Nginx acts as the web server running inside the Azure Linux VM.

Architecture:

```text
Linux VM
   |
   v
Nginx
   |
TCP 80
   |
   v
Web Content
```

---

# 11. Verify Nginx Service

The Nginx service status can be checked using:

```bash
sudo systemctl status nginx
```

Expected state:

```text
active (running)
```

Useful service management commands include:

```bash
sudo systemctl start nginx
```

```bash
sudo systemctl stop nginx
```

```bash
sudo systemctl restart nginx
```

This provided hands-on experience with basic Linux service management.

---

# 12. Verify Listening Port

The listening network ports can be inspected using:

```bash
sudo ss -tulpn
```

For this lab, the important ports were:

```text
22  -> SSH
80  -> HTTP / Nginx
```

Nginx listening on port 80 confirms that the web server is accepting HTTP connections at the operating-system level.

---

# 13. Create Custom Web Page

Instead of using only the default Nginx page, I created a custom page.

The Nginx default web root used in this lab was:

```text
/var/www/html/
```

The page was edited using:

```bash
sudo nano /var/www/html/index.html
```

Example content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>AZ-900 Azure Lab</title>
</head>

<body>

<h1>Azure AZ-900 Hands-On Lab</h1>

<h2>Hosted on Azure Linux VM</h2>

<p>Deployed using:</p>

<ul>
    <li>Azure Virtual Network</li>
    <li>Azure Subnet</li>
    <li>Network Security Group</li>
    <li>Azure Public IP</li>
    <li>Linux Virtual Machine</li>
    <li>Nginx</li>
</ul>

</body>
</html>
```

---

# 14. Verify Web Application

The custom webpage was tested directly from the Linux VM using:

```bash
curl localhost
```

The server successfully returned:

```html
<!DOCTYPE html>
<html>
<head>
    <title>AZ-900 Azure Lab</title>
</head>

<body>

<h1>Azure AZ-900 Hands-On Lab</h1>

<h2>Hosted on Azure Linux VM</h2>

<p>Deployed using:</p>

<ul>
    <li>Azure Virtual Network</li>
    <li>Azure Subnet</li>
    <li>Network Security Group</li>
    <li>Azure Public IP</li>
    <li>Linux Virtual Machine</li>
    <li>Nginx</li>
</ul>

</body>
</html>
```

This confirmed:

```text
Linux VM
   |
   v
Nginx running
   |
   v
HTTP service
   |
   v
index.html
   |
   v
Successful response
```

---

# 15. External HTTP Testing

The application was successfully validated on browser and also locally on the Azure VM using:

```bash
curl localhost
```

This confirmed that Nginx was running and successfully serving the custom webpage.

The Azure NSG was also configured with the required HTTP rule for TCP port 80.

This distinction is important when troubleshooting because a connectivity problem can occur at different layers.

```text
Application working locally
          |
          v
Check VM service
          |
          v
Check listening port
          |
          v
Check Azure NSG
          |
          v
Check client/corporate firewall
          |
          v
Internet connectivity
```

---

# 16. Basic Troubleshooting Approach

One of the key learnings from this lab was how to troubleshoot a web server systematically.

If the webpage cannot be accessed:

```text
Is the VM running?
        |
        v
Can I SSH into the VM?
        |
        v
Is Nginx running?
        |
        v
Is port 80 listening?
        |
        v
Does curl localhost work?
        |
        v
Does the NSG allow TCP 80?
        |
        v
Is the client/network firewall blocking HTTP?
```

Useful commands:

Check Nginx:

```bash
sudo systemctl status nginx
```

Test locally:

```bash
curl localhost
```

Check listening ports:

```bash
sudo ss -tulpn
```

Check IP configuration:

```bash
ip addr
```

This helped distinguish between:

```text
Application issue
Linux/service issue
Azure networking issue
Client/corporate network restriction
```

---

# 17. Azure CLI Verification

The VM can also be inspected using Azure CLI.

```bash
az vm list \
  --resource-group az900-hands-on-rg \
  --show-details \
  --output table
```

This reinforced the ability to manage and inspect Azure resources using both:

```text
Azure Portal
     +
Azure CLI
```

---

# 18. Cost Management

A cloud VM can generate costs while resources remain provisioned.

During the lab, I learned the importance of:

```text
Selecting an appropriate VM size
        |
        v
Using resources only when required
        |
        v
Configuring auto-shutdown where appropriate
        |
        v
Deleting lab resources after completion
```

After completing the lab and collecting the required evidence, the lab resources were deleted to avoid unnecessary Azure costs.

---

# What I Learned

This lab provided hands-on experience with:

* Azure Virtual Machines
* Infrastructure as a Service (IaaS)
* Linux VM deployment
* Ubuntu Server
* VM images
* VM sizing
* Azure Network Interfaces
* Private IP addresses
* Public IP addresses
* Network Security Groups
* SSH
* SSH key-based authentication
* TCP port 22
* HTTP port 80
* Linux package management
* Linux service management
* Nginx installation and configuration
* Hosting a custom webpage
* `curl`
* `systemctl`
* `ss`
* `ip addr`
* Basic network troubleshooting
* Azure CLI
* Azure resource cleanup
* Cloud cost awareness

---

# Complete Request Flow

The intended HTTP request flow for the deployed architecture is:

```text
User
 |
 | HTTP :80
 v
Internet
 |
 v
Azure Public IP
 |
 v
Network Security Group
 |
 | Allow TCP 80
 v
Network Interface
 |
 v
web-subnet
 |
 v
az900-vnet
 |
 v
Linux VM
 |
 v
Nginx
 |
 v
index.html
```

For administration:

```text
Administrator
      |
      | SSH :22
      v
Internet
      |
      v
Public IP
      |
      v
NSG
      |
      | Allow TCP 22
      v
Linux VM
```

---

# Screenshots / Evidence

Recommended evidence for this lab:

```text
screenshots/
|
+-- 01-vm-overview.png
+-- 02-vm-networking.png
+-- 03-ssh-connection.png
+-- 04-linux-ip-address.png
+-- 05-nginx-status.png
+-- 06-nginx-listening-port.png
+-- 07-curl-custom-page.png
```

Before publishing screenshots publicly, sensitive or unnecessary information such as subscription IDs, tenant IDs, public IP addresses, and private key information should be removed or redacted.

---

# Interview Takeaway

After completing this lab, I can explain how Azure compute and networking work together to host a basic web application.

I deployed an Ubuntu Linux VM inside an Azure VNet and subnet, connected to the VM securely using SSH key authentication, installed Nginx, and hosted a custom HTML page.

The VM used a private IP for Azure network communication and a Public IP for external connectivity. An NSG controlled inbound access using TCP port 22 for SSH and TCP port 80 for HTTP.

I verified the web server directly from the VM using `curl localhost` and used Linux commands such as `systemctl`, `ss`, and `ip addr` to validate the service and network configuration.

This lab helped connect Azure concepts such as **IaaS, Virtual Machines, VNets, subnets, NSGs, public/private IP addressing, SSH, Linux, and web hosting** into one practical implementation.

---

# Lab Status

**Lab 4 — Azure Linux VM + SSH + Nginx: Completed ✅**

This lab completes the compute portion of the first AZ-900 hands-on project:

```text
Lab 1
Azure Fundamentals & Resource Organization
        |
        v
Lab 2
Azure Management Tools
        |
        v
Lab 3
Azure Networking
        |
        v
Lab 4
Azure Linux VM + Nginx
        |
        v
POST 1
Azure Infrastructure & Networking
```
