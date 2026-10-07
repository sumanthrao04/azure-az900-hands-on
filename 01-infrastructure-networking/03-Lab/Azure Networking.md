# Lab 3 — Azure Networking

## Overview

In this lab, I learned the fundamental networking concepts used in Microsoft Azure by creating a Virtual Network, subnet, and Network Security Group.

The objective was to understand how Azure resources communicate inside a private network and how network traffic can be controlled using NSG rules.

---

## Architecture

```text
                    Internet
                       |
                       |
                 Network Traffic
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
                 Azure Resources
```

---

# What I Learned

## 1. Azure Virtual Network (VNet)

An Azure Virtual Network provides a private network environment for Azure resources.

For this lab, I created:

```text
VNet Name: az900-vnet
Address Space: 10.0.0.0/16
```

The VNet provides the overall IP address space from which smaller subnet address ranges can be created.

### Key Learning

A VNet can contain multiple subnets.

Example:

```text
VNet
10.0.0.0/16

    |
    +-- Web Subnet
    |     10.0.1.0/24
    |
    +-- App Subnet
    |     10.0.2.0/24
    |
    +-- Database Subnet
          10.0.3.0/24
```

This allows applications to be separated into different network segments.

---

# 2. CIDR

I learned how CIDR notation is used to define network address ranges.

For example:

```text
10.0.0.0/16
```

was used as the VNet address space.

The subnet used:

```text
10.0.1.0/24
```

The subnet address range must be contained within the VNet address space.

### Lab Example

```text
VNet
10.0.0.0/16

        |
        +-- web-subnet
              10.0.1.0/24
```

CIDR allows us to divide a larger network into smaller network segments.

---

# 3. Azure Subnet

A subnet is a smaller network created inside a VNet.

For this lab, I created:

```text
Subnet Name: web-subnet
Address Range: 10.0.1.0/24
```

The subnet will contain the web-server resources used in the next lab.

### Key Learning

Instead of placing every application component in the same network segment, we can create separate subnets.

Example:

```text
Azure VNet
10.0.0.0/16

      |
      +-- Web Subnet
      |
      +-- Application Subnet
      |
      +-- Database Subnet
```

This helps organize and isolate different application tiers.

---

# 4. Private IP Address

Resources inside an Azure VNet can communicate using private IP addresses.

Example:

```text
10.0.1.x
```

Private IP addresses are used for internal communication inside the Azure network.

Example:

```text
VM-1
10.0.1.4

   |
   | Private communication
   |
   v

VM-2
10.0.1.5
```

Private IP addresses are not directly reachable from the public internet.

---

# 5. Public IP Address

A Public IP allows an Azure resource to communicate with or be reachable from the internet when the required network security rules and service configuration permit it.

Example architecture:

```text
User
 |
Internet
 |
Public IP
 |
Azure Resource
```

In the following VM lab, a Public IP was used to establish SSH connectivity to the Linux VM.

---

# 6. Network Security Group (NSG)

A Network Security Group is used to filter inbound and outbound network traffic using security rules.

For this lab, I created:

```text
NSG Name:

az900-web-nsg
```

The NSG was associated with:

```text
web-subnet
```

Architecture:

```text
Network Traffic
       |
       v
+---------------+
|      NSG      |
|               |
| Security      |
| Rules         |
+-------+-------+
        |
        v
   web-subnet
```

---

# 7. Inbound Traffic

Inbound traffic refers to network traffic entering resources protected by the NSG.

For example:

```text
Internet
    |
    | Inbound
    v
Azure Resource
```

I configured inbound rules for:

```text
SSH  -> TCP 22
HTTP -> TCP 80
```

---

# 8. SSH — Port 22

SSH is commonly used to remotely administer Linux systems.

The network flow is:

```text
Administrator
      |
      | SSH
      | TCP 22
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

For better security, SSH access should be restricted to trusted source IP addresses where possible instead of allowing access from any internet address.

---

# 9. HTTP — Port 80

HTTP commonly uses TCP port 80.

The network flow for a web application is:

```text
User
 |
 | HTTP
 | TCP 80
 v
Public IP
 |
 v
NSG
 |
 | Allow TCP 80
 v
Web Server
```

The NSG therefore needs an appropriate inbound rule if the web server must receive HTTP traffic.

---

# 10. Outbound Traffic

Outbound traffic refers to traffic leaving an Azure resource.

Example:

```text
Azure VM
   |
   | Outbound
   v
Internet
```

A practical example is a Linux VM contacting Ubuntu package repositories when running:

```bash
sudo apt update
```

---

# 11. NSG Rules

An NSG rule can evaluate properties such as:

```text
Source
Destination
Protocol
Source Port
Destination Port
Priority
Action
```

Example:

```text
Source       : Trusted IP
Protocol     : TCP
Port         : 22
Action       : Allow
Purpose      : SSH
```

Another example:

```text
Source       : Internet
Protocol     : TCP
Port         : 80
Action       : Allow
Purpose      : HTTP
```

---

# 12. NSG Rule Priority

NSG rules have priorities.

Lower priority numbers are evaluated before higher priority numbers.

Example:

```text
Priority 100
Allow SSH

Priority 110
Allow HTTP
```

Understanding priority is important when troubleshooting situations where multiple network security rules exist.

---

# 13. Subnet-Level NSG

In this lab, the NSG was associated with the subnet.

```text
az900-vnet
      |
      v
web-subnet
      |
      +---- az900-web-nsg
```

This means network security rules associated with the subnet can control traffic for resources connected through that subnet.

---

# 14. Network Interface (NIC)

I also learned how the Network Interface connects a Virtual Machine to Azure networking.

The relationship can be visualized as:

```text
Azure VNet
     |
     v
Subnet
     |
     v
NIC
     |
     v
Virtual Machine
```

The NIC can have a private IP address and is the VM's connection to the Azure virtual network.

---

# 15. Network Traffic Flow

One of the most important concepts learned from this lab was understanding the complete traffic path.

For HTTP:

```text
Internet User
      |
      | HTTP :80
      v
Public IP
      |
      v
NSG
      |
      | Allow TCP 80
      v
NIC
      |
      v
Subnet
      |
      v
Virtual Machine
      |
      v
Web Server
```

For administration:

```text
Administrator
      |
      | SSH :22
      v
Public IP
      |
      v
NSG
      |
      | Allow TCP 22
      v
NIC
      |
      v
Linux VM
```

---

# Resources Created

| Resource               | Name              | Purpose                   |
| ---------------------- | ----------------- | ------------------------- |
| Resource Group         | az900-hands-on-rg | Organize lab resources    |
| Virtual Network        | az900-vnet        | Private Azure network     |
| Address Space          | 10.0.0.0/16       | VNet IP range             |
| Subnet                 | web-subnet        | Web workload network      |
| Subnet CIDR            | 10.0.1.0/24       | Subnet IP range           |
| Network Security Group | az900-web-nsg     | Network traffic filtering |
| SSH Rule               | TCP 22            | Linux administration      |
| HTTP Rule              | TCP 80            | Web traffic               |

---

# Verification

The VNet configuration was verified from the Azure Portal and Azure CLI.

Example:

```bash
az network vnet show \
  --resource-group az900-hands-on-rg \
  --name az900-vnet \
  --output table
```

Subnet verification:

```bash
az network vnet subnet list \
  --resource-group az900-hands-on-rg \
  --vnet-name az900-vnet \
  --output table
```

NSG verification:

```bash
az network nsg show \
  --resource-group az900-hands-on-rg \
  --name az900-web-nsg \
  --output table
```

NSG rule verification:

```bash
az network nsg rule list \
  --resource-group az900-hands-on-rg \
  --nsg-name az900-web-nsg \
  --output table
```

---

# Screenshots

Recommended screenshots for documenting this lab:

```text
screenshots/
|
+-- 01-vnet-overview.png
+-- 02-vnet-address-space.png
+-- 03-web-subnet.png
+-- 04-nsg-inbound-rules.png
+-- 05-nsg-subnet-association.png
```

---

# Key AZ-900 Concepts Covered

This lab provided hands-on understanding of:

* Azure Virtual Network
* Subnets
* CIDR
* Private IP addresses
* Public IP addresses
* Network Security Groups
* Inbound traffic
* Outbound traffic
* NSG security rules
* Rule priorities
* TCP ports
* SSH port 22
* HTTP port 80
* Network Interfaces
* Network segmentation
* Azure network traffic flow

---

# Interview Takeaway

After completing this lab, I can explain the basic Azure network flow as:

```text
Internet
   |
Public IP
   |
Network Security Group
   |
Azure Virtual Network
   |
Subnet
   |
Network Interface
   |
Virtual Machine
```

The **VNet** provides the private network, **subnets** divide that network into smaller segments, **NSGs** control allowed inbound and outbound traffic, and the **NIC** connects a Virtual Machine to the Azure network.

This networking foundation was then used in the next lab to deploy an Azure Linux Virtual Machine and host an Nginx web server.
