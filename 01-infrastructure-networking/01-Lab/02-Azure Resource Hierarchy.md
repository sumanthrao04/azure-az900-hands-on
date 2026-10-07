For **AZ-900 + your Lab 1**, you don't need deep administration knowledge here. You should understand the hierarchy, what each level controls, and a few common scenarios Microsoft can ask in the exam.

# 2. Azure Resource Hierarchy

Start with this mental model:

```text
Microsoft Entra Tenant
        │
        ▼
Management Groups
        │
        ▼
Subscriptions
        │
        ▼
Resource Groups
        │
        ▼
Resources
```

Think of a company:

```text
Company / Entra Tenant
│
├── Management Group: Production
│    │
│    ├── Subscription: Production-App
│    │     │
│    │     ├── Resource Group: prod-web-rg
│    │     │      ├── Virtual Machine
│    │     │      ├── VNet
│    │     │      └── Public IP
│    │     │
│    │     └── Resource Group: prod-db-rg
│    │            └── Azure SQL
│
└── Management Group: Development
     │
     └── Subscription: Dev-App
           │
           └── Resource Group: dev-web-rg
                  ├── VM
                  ├── VNet
                  └── Storage Account
```

## 1. Microsoft Entra tenant

A **Microsoft Entra tenant** is the identity and access-management boundary for an organization.

Microsoft Entra ID was previously called **Azure Active Directory (Azure AD)**.

It manages identities such as:

```text
Users
Groups
Applications
Service principals
Managed identities
```

For example:

```text
Company: ABC
       │
       ▼
Microsoft Entra Tenant
       │
       ├── Sumanth
       ├── DevOps-Team
       ├── Developers
       └── Administrators
```

Think:

> **Entra ID = Who are you?**

It provides authentication and is also involved in authorization to Azure resources through mechanisms such as Azure RBAC.

---

# 2. Management Groups

A **Management Group** sits above subscriptions.

Its main purpose is to manage **multiple Azure subscriptions at scale**.

```text
Tenant
  │
  └── Management Group
        │
        ├── Subscription A
        ├── Subscription B
        └── Subscription C
```

Why is this useful?

Imagine a company has:

```text
50 Azure subscriptions
```

Instead of configuring governance independently on all 50 subscriptions, the organization can organize them under management groups.

For example:

```text
Company
│
├── Production
│    ├── Prod Subscription 1
│    └── Prod Subscription 2
│
└── Non-Production
     ├── Dev Subscription
     ├── QA Subscription
     └── Test Subscription
```

Organizations can apply governance at higher levels using things such as:

* Azure Policy
* Azure RBAC

The configuration can then be inherited by lower levels.

### Remember

> **Management Group = organize and govern multiple subscriptions.**

---

# 3. Azure Subscription

This is one of the most important concepts for AZ-900.

A **subscription** is a logical Azure account/container associated with billing and resource management.

```text
Subscription
    │
    ├── Resource Group A
    ├── Resource Group B
    └── Resource Group C
```

A subscription provides important boundaries around areas such as:

* Billing
* Access control
* Resource/service quotas and limits
* Organization of Azure environments

For example, a company might create:

```text
Company
│
├── Production Subscription
├── Development Subscription
└── Testing Subscription
```

This makes it easier to separate environments, costs and permissions.

### Billing example

Suppose:

```text
Production Subscription
Monthly cost = ₹100,000

Development Subscription
Monthly cost = ₹30,000
```

Azure can track costs at the subscription level, helping the organization understand which subscription is generating charges.

### Remember

> **Subscription = billing and management boundary containing Azure resources/resource groups.**

---

# 4. Resource Group

You'll actually create one of these in your lab.

A **Resource Group (RG)** is a logical container for related Azure resources.

For your AZ-900 lab:

```text
Subscription
      │
      ▼
az900-hands-on-rg
      │
      ├── Virtual Network
      ├── Virtual Machine
      ├── Public IP
      └── Storage Account
```

The resources don't have to be the same type.

For example:

```text
az900-webapp-rg

├── VM
├── VNet
├── Network Interface
├── Public IP
└── Storage Account
```

They're grouped because they belong to the same application/project/lifecycle.

### Important exam concept

Resources inside a resource group **can be in different Azure regions**.

For example:

```text
Resource Group: demo-rg

VM              → Central India
Storage Account → South India
```

The **resource group itself also has a location**, which primarily determines where its metadata is stored. It doesn't force every resource inside it into that same region.

---

# 5. Azure Resource

A **resource** is an actual instance of an Azure service that you create and manage.

Examples:

| Azure service          | Example resource  |
| ---------------------- | ----------------- |
| Azure Virtual Machines | `az900-vm01`      |
| Virtual Network        | `az900-vnet`      |
| Storage Account        | `az900storage01`  |
| Public IP              | `az900-public-ip` |
| Azure SQL Database     | `az900-db`        |

So:

```text
Azure Virtual Machines
        ↓
Service

az900-vm01
        ↓
Resource
```

That's an important distinction.

---

# 6. Parent-child hierarchy

For AZ-900, memorize:

```text
Microsoft Entra Tenant
        │
        ▼
Management Group
        │
        ▼
Subscription
        │
        ▼
Resource Group
        │
        ▼
Resource
```

A simple memory trick:

```text
Tenant
   ↓
Company identity

Management Group
   ↓
Organize subscriptions

Subscription
   ↓
Billing / management boundary

Resource Group
   ↓
Organize related resources

Resource
   ↓
Actual Azure service instance
```

---

# 7. Understand inheritance

This is particularly important.

Azure governance/access settings can be applied at different scopes.

Conceptually:

```text
Management Group
       │
       │ Policy / RBAC
       ▼
Subscription
       │
       ▼
Resource Group
       │
       ▼
Resource
```

Permissions assigned at a parent scope can be inherited by child scopes.

For example, if someone receives an appropriate RBAC role at:

```text
Subscription
```

that assignment normally applies to resource groups and resources underneath that subscription.

Similarly:

```text
Resource Group
     │
     ├── VM
     ├── Storage
     └── VNet
```

A role assignment at the resource-group scope can apply to the resources within it.

This leads directly into another important AZ-900 topic: **Azure RBAC**.

---

# 8. Resource lifecycle

Another useful reason for resource groups is **lifecycle management**.

Suppose your lab contains:

```text
az900-lab-rg
│
├── az900-vm
├── az900-vnet
├── az900-nsg
├── az900-public-ip
└── az900-storage
```

After finishing the lab, deleting:

```text
az900-lab-rg
```

can delete the resources contained within that resource group as part of the deletion operation.

This is very useful for labs because it helps you clean up resources and avoid unnecessary charges.

---

# 9. Resources belong to one resource group

An Azure resource is associated with **one resource group at a time**.

You can't have:

```text
VM-01
├── RG-A
└── RG-B
```

Instead:

```text
RG-A
  │
  └── VM-01
```

Many resource types can later be moved between resource groups/subscriptions, subject to Azure's move support and restrictions.

---

# 10. Tags

You should also know **Azure Tags**.

Tags are key-value metadata used to organize resources.

For example:

```text
VM: az900-vm01

Environment = Development
Project     = AZ900-Lab
Owner       = DevOps-Team
CostCenter  = Training
```

Think:

```text
Resource Groups → organize resources

Tags → label/classify resources
```

Tags become especially useful when organizations have thousands of resources.

---

# 11. Resource Locks

Know the basic idea of **Resource Locks**.

Two important lock types are:

```text
Delete
ReadOnly
```

For example:

```text
Production VM
     │
     ▼
Delete Lock
     │
     ▼
Protection against accidental deletion
```

This is useful for critical production resources.

---

# 12. Azure Policy vs RBAC

You'll encounter these repeatedly during AZ-900.

The easiest distinction is:

### Azure RBAC

Controls:

> **Who can do what?**

Example:

```text
DevOps Engineer
      │
      ▼
Contributor Role
      │
      ▼
Resource Group
```

### Azure Policy

Controls:

> **What configurations/resources are allowed or required?**

Example:

Company requirement:

```text
Resources must only be deployed in
Central India
```

Azure Policy can help enforce that governance requirement.

So remember:

```text
RBAC
→ WHO can perform actions?

Policy
→ WHAT configurations are allowed/required?

Resource Lock
→ Protect resources from accidental changes/deletion
```

---

# 13. AZ-900 scenarios you should be able to answer

**Scenario 1:** A company has 20 subscriptions and wants centralized governance.

```text
Answer → Management Groups
```

**Scenario 2:** The company wants separate billing/management boundaries for development and production.

```text
Answer → Separate Subscriptions
```

**Scenario 3:** You want to group the VM, VNet and storage belonging to one application.

```text
Answer → Resource Group
```

**Scenario 4:** You want to control who can manage a VM.

```text
Answer → Azure RBAC
```

**Scenario 5:** The company wants to prevent resources from being deployed outside approved regions.

```text
Answer → Azure Policy
```

**Scenario 6:** You want protection against accidental deletion of a production resource.

```text
Answer → Resource Lock
```

**Scenario 7:** You want to identify resources belonging to `Production`, `Development`, different owners or cost centers.

```text
Answer → Tags
```

---

# 14. Notes for your AZ-900 notebook

Write this compact version:

```text
AZURE RESOURCE HIERARCHY

Entra Tenant
↓
Identity boundary for organization.

Management Group
↓
Organizes multiple subscriptions.
Used for governance at scale.

Subscription
↓
Billing + management boundary.
Contains resource groups/resources.

Resource Group
↓
Logical container for related resources.
Helps organize/manage resource lifecycle.

Resource
↓
Actual Azure service instance.
Examples: VM, VNet, Storage Account.

----------------------------------

RBAC
→ Who can do what?

Azure Policy
→ What is allowed/required?

Tags
→ Organize/classify resources.

Resource Locks
→ Protect resources from accidental deletion/change.

----------------------------------

Hierarchy:

Tenant
  ↓
Management Groups
  ↓
Subscriptions
  ↓
Resource Groups
  ↓
Resources
```
