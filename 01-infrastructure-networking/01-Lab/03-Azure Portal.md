Exactly. For **AZ-900**, Azure Portal is mainly about understanding **what it is, why we use it, and where common services are located**. You do not need to memorize every menu.

# 4. Azure Portal

## 1. What is Azure Portal?

**Azure Portal** is Microsoft's web-based graphical interface for creating, configuring, monitoring, and managing Azure resources.

Think of it as:

```text
Azure Portal
     ↓
Graphical interface for Azure
     ↓
Create → Configure → Monitor → Manage
```

For example, instead of using CLI commands, you can create a VM through:

```text
Azure Portal
   ↓
Virtual Machines
   ↓
Create
   ↓
Azure Virtual Machine
```

For AZ-900, know that Azure resources can also be managed through tools such as **Azure CLI, Azure PowerShell, ARM/Bicep, and APIs**.

---

# 2. Home

The Azure Portal home page is your starting point.

You'll commonly see recently used or commonly accessed Azure services.

You can also use the search bar at the top.

For example, search:

```text
Resource groups
Virtual machines
Storage accounts
Virtual networks
Monitor
Cost Management
```

### Lab habit

Don't spend time hunting through menus.

Use:

```text
Search → Resource Groups
Search → Virtual Machines
Search → Monitor
```

This is how you'll work faster during the labs.

---

# 3. Subscriptions

Navigate/search for:

```text
Subscriptions
     ↓
Your Azure Subscription
```

Here you can see information about the subscription you're currently using.

Remember from the previous lesson:

```text
Subscription
     ↓
Billing + management boundary
```

During your labs, always verify you're deploying into the correct subscription.

---

# 4. Resource Groups

Search:

```text
Resource groups
```

This is going to be one of your most-used screens.

For Lab 1, we'll eventually create something like:

```text
az900-hands-on-rg
```

Inside it you might later see:

```text
az900-hands-on-rg
│
├── VNet
├── VM
├── Public IP
├── NSG
└── Storage Account
```

From the Resource Group page, you can view resources, deployments, access control, tags and other management information.

---

# 5. All Resources

Search:

```text
All resources
```

This gives you a consolidated view of resources you can access.

For example:

```text
Name                 Type
---------------------------------------
az900-vm01           Virtual machine
az900-vnet           Virtual network
az900-storage        Storage account
az900-public-ip      Public IP address
```

The important distinction is:

```text
Resource Groups
→ Resources organized by logical container

All Resources
→ View resources across accessible resource groups
```

Filters are very useful here.

---

# 6. Virtual Machines

Search:

```text
Virtual machines
```

Azure Virtual Machines provide **Infrastructure as a Service (IaaS)** compute.

You'll eventually encounter things like:

```text
VM
├── Operating System
├── Size
├── Disk
├── Network Interface
├── VNet
├── NSG
└── Public IP
```

For AZ-900, you don't need to become a VM administrator yet.

Understand:

> **Azure VM = virtual server running in Azure.**

---

# 7. Virtual Networks

Search:

```text
Virtual networks
```

A **Virtual Network (VNet)** provides private networking for Azure resources.

Example:

```text
Azure VNet
10.0.0.0/16
      │
      ├── Web Subnet
      │     └── VM
      │
      └── DB Subnet
            └── Database resources
```

Think:

> **VNet = private network in Azure.**

We'll learn networking separately rather than going deep during Portal navigation.

---

# 8. Storage Accounts

Search:

```text
Storage accounts
```

A Storage Account provides access to Azure storage services.

You'll encounter services such as:

```text
Storage Account
│
├── Blob
├── Files
├── Queues
└── Tables
```

A simple example:

```text
Storage Account
      ↓
Blob Container
      ↓
image.jpg
backup.zip
logs.txt
```

For AZ-900, understand what the major storage services are used for. We'll cover them separately.

---

# 9. Microsoft Entra ID

Search:

```text
Microsoft Entra ID
```

This relates to **identity and access management**.

You'll encounter:

```text
Microsoft Entra ID
│
├── Users
├── Groups
├── Applications
└── Roles / identity features
```

Simple mental model:

```text
Authentication
"Who are you?"

        +

Authorization
"What are you allowed to do?"
```

Don't confuse **Microsoft Entra roles** with **Azure RBAC roles**; they're related to access management but govern different scopes.

---

# 10. Azure Monitor

Search:

```text
Monitor
```

Azure Monitor is Azure's monitoring/observability platform.

At the fundamentals level, think:

```text
Azure Resources
     ↓
Metrics / Logs / Activity
     ↓
Azure Monitor
     ↓
Observe
Analyze
Alert
Troubleshoot
```

For example:

```text
VM
 ↓
CPU metric
 ↓
Azure Monitor
 ↓
Alert when threshold is reached
```

Given your DevOps background, you'll later be able to relate this to observability concepts you've already been learning.

---

# 11. Cost Management

Search:

```text
Cost Management
```

This is very important when practicing Azure.

It helps you understand and manage cloud spending.

You'll encounter concepts such as:

```text
Cost Analysis
Budgets
Cost alerts
Recommendations / optimization features
```

For example:

```text
Monthly Budget
     ↓
₹1,000
     ↓
Actual spending
     ↓
₹800
     ↓
Budget threshold/alert
```

For labs, make it a habit to check costs and delete resources you no longer need.

---

# 12. One important menu: Access Control (IAM)

When you open resources, resource groups or subscriptions, you'll frequently see:

```text
Access control (IAM)
```

This is where **Azure RBAC** becomes relevant.

Example:

```text
Resource Group
     ↓
Access Control (IAM)
     ↓
Role Assignment
     ↓
User
     ↓
Reader
```

Meaning the user can view resources within the assigned scope, subject to the role's permissions.

Remember:

> **IAM/RBAC → Who can do what at a particular scope?**

---

# 13. Another important area: Activity Log

You'll also encounter:

```text
Activity log
```

It records control-plane events involving Azure resources.

For example:

```text
VM created
VM deleted
Resource updated
Role assignment changes
```

This becomes useful when troubleshooting:

> "Who changed this Azure resource?"

---

# 14. Your hands-on navigation exercise

Before moving forward, spend **15–20 minutes** navigating your Azure account.

Don't create anything yet.

Use the search bar and open these areas:

```text
1. Subscriptions
       ↓
   Open your subscription

2. Resource Groups
       ↓
   See existing resource groups

3. All Resources
       ↓
   Check existing resources

4. Virtual Machines

5. Virtual Networks

6. Storage Accounts

7. Microsoft Entra ID

8. Monitor

9. Cost Management
```

While navigating, ask yourself:

```text
What is this service?

What problem does it solve?

Where does it fit in Azure?

Is it Compute?
Networking?
Storage?
Identity?
Monitoring?
Cost/Governance?
```

That approach is much more useful than memorizing where buttons are.

## AZ-900 notes

Write this in your notes:

```text
AZURE PORTAL

Azure Portal
→ Web-based GUI for managing Azure.

Subscription
→ Billing/management boundary.

Resource Groups
→ Logical containers for resources.

All Resources
→ View Azure resources I can access.

Virtual Machines
→ IaaS compute.

Virtual Networks
→ Private Azure networking.

Storage Accounts
→ Azure storage services.

Microsoft Entra ID
→ Identity and access management.

Azure Monitor
→ Monitoring, metrics, logs and alerts.

Cost Management
→ Analyze and control Azure spending.

Access Control (IAM)
→ Azure RBAC / permissions.

Activity Log
→ Records Azure control-plane activities.
```