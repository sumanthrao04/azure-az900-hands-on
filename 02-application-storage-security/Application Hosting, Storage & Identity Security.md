# 🔐 Lab 07 — Microsoft Entra ID & Azure RBAC

## Phase 2: Azure Application, Storage & Security

You've completed **Lab 5 — Azure Storage** and **Lab 6 — Azure App Service**.

Now we'll start **Lab 7 — Microsoft Entra ID & Azure Role-Based Access Control (RBAC)**.

This is the final lab in Phase 2. After completing it, we'll prepare your **second LinkedIn post**, combining all three labs.

Since you're preparing for **AZ-900 certification**, we'll focus on understanding identity, authentication, authorization, and Azure security through hands-on practice.

We'll also cover real-world DevOps scenarios and interview questions.

---

# 1. Lab Overview

| Details        | Description                                               |
| -------------- | --------------------------------------------------------- |
| Lab            | 07 — Microsoft Entra ID & Azure RBAC                      |
| Certification  | AZ-900                                                    |
| Phase          | 2 — Application, Storage & Security                       |
| Difficulty     | Beginner                                                  |
| Estimated Time | 60–90 minutes                                             |
| Platform       | Azure Portal + Azure CLI                                  |
| Subscription   | Pluralsight Azure Sandbox                                 |
| Cost           | Usually no additional resource cost for basic exploration |
| LinkedIn       | Combine with Labs 5 and 6 for Post 2                      |

### What we'll learn

1. Microsoft Entra ID
2. Azure tenants
3. Users and groups
4. Authentication vs authorization
5. Azure RBAC
6. Built-in Azure roles
7. Role assignments
8. RBAC scopes
9. Principle of least privilege
10. Multifactor authentication (MFA)
11. Single Sign-On (SSO)
12. Conditional Access
13. Zero Trust security
14. Managed identities
15. Azure CLI identity and RBAC verification

**Important:** Your Pluralsight sandbox may restrict creating users, groups, or role assignments. We'll start with read-only exercises and perform write operations only if permissions allow.

---

# 2. Architecture — Identity and Access Management

First, understand how identity and access management works in Azure.

```text
                  Microsoft Entra ID
                          |
                    Authentication
                          |
                          v
                     Azure RBAC
                          |
                    Authorization
                          |
                          v
                  Azure Subscription
                          |
                          v
                    Resource Group
                          |
                  +-------+-------+
                  |               |
                  v               v
             Storage Account   App Service
```

### Real-world example

Imagine a company has three teams:

```text
                  Microsoft Entra ID
                          |
                 +--------+--------+
                 |        |        |
               DevOps  Developers  Auditors
                 |        |        |
                 v        v        v
             Contributor Reader  Reader
                 |        |        |
                 +--------+--------+
                          |
                    Azure Resources
```

This is only an example. Actual role assignments depend on what each team needs to do.

For example, a developer who needs to deploy applications may require more than Reader permissions.

---

# PART 1 — Understand Microsoft Entra ID

## Step 1 — What is Microsoft Entra ID?

Microsoft Entra ID, previously called Azure Active Directory, is Microsoft's cloud-based identity and access management service.

It helps organizations manage:

* Users
* Groups
* Applications
* Authentication
* Single Sign-On
* Multifactor authentication
* Identity security

### Example

An employee wants to access the Azure Portal.

```text
Employee
    |
    | Username + Authentication
    v
Microsoft Entra ID
    |
    | Identity verified
    v
Azure Portal
    |
    | RBAC authorization
    v
Azure Resources
```

**AZ-900 exam point:**

Microsoft Entra ID handles identity and authentication.

Azure RBAC controls authorization to Azure resources.

---

# PART 2 — Explore Microsoft Entra ID

## Step 2 — Open Microsoft Entra ID

Log in to the Azure Portal.

Search:

```text
Microsoft Entra ID
```

Open the service.

You should see an overview containing information such as:

```text
Tenant Name
Tenant ID
Primary Domain
License
Users
Groups
```

### What is a tenant?

A Microsoft Entra tenant is a dedicated identity directory representing an organization.

For example:

```text
Organization
      |
      v
Microsoft Entra Tenant
      |
      +-- Users
      |
      +-- Groups
      |
      +-- Applications
      |
      +-- Service Principals
```

A tenant can be associated with multiple Azure subscriptions.

### Hands-on task

Explore the following:

| Property                | What to understand                        |
| ----------------------- | ----------------------------------------- |
| Tenant name             | Name of the identity directory            |
| Tenant ID               | Unique identifier for the tenant          |
| Primary domain          | Default domain associated with the tenant |
| Users                   | Identities in the directory               |
| Groups                  | Collections of identities                 |
| Enterprise applications | Applications represented in the tenant    |

📸 **Screenshot 1**

Save as:

`01-entra-id-overview.png`

Redact tenant IDs and other unnecessary identifiers before publishing.

---

# PART 3 — Explore Users

## Step 3 — Open Users

Navigate to:

**Microsoft Entra ID → Users → All users**

You'll see the users available in your tenant, subject to your permissions.

### What is a user?

A user represents an identity that can authenticate to Microsoft Entra ID.

Example:

```text
Microsoft Entra ID
       |
       +-- user1@company.com
       |
       +-- user2@company.com
       |
       +-- user3@company.com
```

### Types of users

| User type | Description                             |
| --------- | --------------------------------------- |
| Member    | User belonging to the organization      |
| Guest     | External user invited for collaboration |

### Hands-on exercise

Explore an existing user and inspect:

* Display name
* User principal name
* User type
* Group memberships, if visible
* Assigned roles, if visible

Do not modify existing sandbox users.

### Optional exercise — Create a user

**Only perform this exercise in a tenant you own or where you have explicit permission to manage identities.**

If permitted:

1. Open **Users**.
2. Select **New user**.
3. Choose **Create new user**.
4. Enter a test username.
5. Configure the required properties.
6. Create the user.

Example:

```text
Display Name: AZ900 Test User
Username: az900-test-user@<your-tenant-domain>
```

In a Pluralsight sandbox, this operation may be restricted. If so, skip it.

📸 **Screenshot 2**

`02-entra-id-users.png`

---

# PART 4 — Explore Groups

## Step 4 — Open Groups

Navigate to:

**Microsoft Entra ID → Groups → All groups**

### What is a group?

A group allows administrators to manage multiple identities together.

Instead of assigning permissions individually:

```text
User 1 → Reader
User 2 → Reader
User 3 → Reader
```

You can assign permissions to a group:

```text
             Azure RBAC
                 |
              Reader
                 |
             Dev-Team
                 |
          +------+------+
          |      |      |
        User1  User2  User3
```

This makes access management easier.

### Group types

| Group type          | Purpose                                             |
| ------------------- | --------------------------------------------------- |
| Security group      | Manage access to resources                          |
| Microsoft 365 group | Support collaboration across Microsoft 365 services |

### Optional hands-on

If permissions allow, create:

```text
Group Name:
az900-readers
```

Add a test user you created.

Do not add or modify unrelated users.

### Key learning

Groups simplify access management by allowing permissions to be assigned collectively.

📸 **Screenshot 3**

`03-entra-id-groups.png`

---

# PART 5 — Authentication vs Authorization

This is extremely important for AZ-900.

## Step 5 — Understand the difference

### Authentication

Authentication answers:

**Who are you?**

Example:

```text
User
  |
  | Login
  v
Microsoft Entra ID
  |
  | Verify Identity
  v
Authenticated
```

### Authorization

Authorization answers:

**What are you allowed to do?**

Example:

```text
Authenticated User
        |
        v
Azure RBAC
        |
        v
Check Assigned Role
        |
        +-- Reader
        |
        +-- Contributor
        |
        +-- Owner
```

### Comparison

| Authentication                              | Authorization                             |
| ------------------------------------------- | ----------------------------------------- |
| Verifies identity                           | Determines permissions                    |
| Who are you?                                | What can you do?                          |
| Uses credentials and authentication methods | Uses roles and access policies            |
| Microsoft Entra ID                          | Azure RBAC for Azure resource permissions |

### AZ-900 exam question

**Q: A user successfully signs in to Azure but cannot create a virtual machine. Why?**

**Answer:**

The user has authenticated successfully but may not have sufficient Azure RBAC permissions to create a VM.

---

# PART 6 — Understand Azure RBAC

## Step 6 — What is Azure RBAC?

Azure Role-Based Access Control is an authorization system that controls access to Azure resources.

An RBAC role assignment combines three elements:

```text
WHO?
 |
 v
Security Principal
(User / Group / Service Principal / Managed Identity)

WHAT PERMISSIONS?
 |
 v
Role Definition
(Reader / Contributor / Owner)

WHERE?
 |
 v
Scope
(Subscription / Resource Group / Resource)
```

### Example

```text
User: DevOps Engineer
        |
        v
Role: Contributor
        |
        v
Scope: Resource Group
        |
        v
Can manage resources in that RG
```

**Important:** Contributor cannot assign Azure RBAC roles simply because they have Contributor access.

---

# PART 7 — Understand Built-in RBAC Roles

## Step 7 — Learn the common roles

| Role                      | Permissions                                       | Example              |
| ------------------------- | ------------------------------------------------- | -------------------- |
| Reader                    | View resources                                    | Auditor              |
| Contributor               | Manage resources, but not assign Azure RBAC roles | Developer            |
| Owner                     | Manage resources and assign roles                 | Administrator        |
| User Access Administrator | Manage user access to Azure resources             | Access administrator |

### Reader

```text
Reader
   |
   +-- View VM
   +-- View VNet
   +-- View Storage Account configuration
   |
   X-- Create VM
   X-- Delete VM
```

Reader does not automatically grant access to private Blob Storage data.

### Contributor

```text
Contributor
   |
   +-- Create VM
   +-- Modify VM
   +-- Delete VM
   +-- Manage VNet
   |
   X-- Assign Azure RBAC Roles
```

### Owner

```text
Owner
   |
   +-- Manage Resources
   +-- Delete Resources
   +-- Assign Roles
```

### AZ-900 exam point

Remember:

**Reader → Read**

**Contributor → Manage resources**

**Owner → Manage resources and access**

---

# PART 8 — Understand RBAC Scopes

## Step 8 — Learn the scope hierarchy

Azure RBAC permissions can be assigned at different scopes.

```text
Management Group
       |
       v
Subscription
       |
       v
Resource Group
       |
       v
Resource
```

### Example

Imagine:

```text
Subscription
      |
      +-- RG-Development
      |
      +-- RG-Production
```

If a user receives Reader access at the subscription level, the assignment is inherited by resource groups and resources within that subscription.

If a user receives Reader access only at `RG-Development`, the assignment does not automatically provide access to `RG-Production`.

### Important concept

**RBAC permissions are inherited from parent scopes to child scopes.**

---

# PART 9 — Hands-on Azure RBAC

Now we'll inspect the permissions in your existing sandbox Resource Group.

## Step 9 — Open Resource Group IAM

Navigate to:

**Azure Portal → Resource groups → Your sandbox Resource Group**

Select:

**Access control (IAM)**

You should see options such as:

```text
Check access
Role assignments
Roles
Deny assignments
```

### Exercise 1 — Explore Roles

Open:

**Access control (IAM) → Roles**

Search for:

```text
Reader
Contributor
Owner
User Access Administrator
```

Open each role and review its permissions.

### What to observe

Reader is primarily for viewing resources.

Contributor can manage resources.

Owner includes resource management and access delegation capabilities.

📸 **Screenshot 4**

`04-azure-rbac-roles.png`

---

## Step 10 — Inspect existing role assignments

Navigate to:

**Access control (IAM) → Role assignments**

Inspect existing assignments.

Look for:

```text
Principal
Role
Scope
```

Do not change existing assignments.

### Exercise 2 — Check your own access

Select:

**Check access**

Search for your signed-in identity.

Inspect the roles available to you.

You may discover that your sandbox account has restricted permissions.

This is expected in managed training environments.

📸 **Screenshot 5**

`05-rbac-role-assignments.png`

Redact personal information and account identifiers.

---

# PART 10 — Optional RBAC Assignment Lab

This is the most useful hands-on exercise if your permissions allow it.

## Step 11 — Assign Reader access

**Only perform this step using a test identity or group that you are authorized to manage.**

Navigate to:

**Resource Group → Access control (IAM) → Add → Add role assignment**

Select:

```text
Role:
Reader
```

Select:

```text
Members:
az900-readers
```

Scope:

```text
Your test Resource Group
```

Review and assign.

### Architecture

```text
Microsoft Entra ID
        |
        v
az900-readers
        |
        v
Reader Role
        |
        v
Test Resource Group
        |
        +-- Storage Account
        |
        +-- App Service
```

### What should happen?

Members of the group receive Reader permissions at the assigned scope, subject to other applicable permissions.

They can view resources but cannot modify them solely through the Reader role.

### Important

Azure RBAC permissions are additive. If a user already has Contributor or Owner permissions through another assignment, adding Reader does not remove those permissions.

---

# PART 11 — Verify RBAC Using Azure CLI

Now let's inspect role assignments using Azure CLI.

## Step 12 — Open Azure Cloud Shell

Open:

**Azure Portal → Cloud Shell → Bash**

Run:

```bash
az account show --output table
```

This displays your current Azure subscription context.

### List role definitions

```bash
az role definition list \
  --query "[].{Role:roleName,Type:roleType}" \
  --output table
```

This command may return many roles.

To inspect Reader:

```bash
az role definition list \
  --name Reader \
  --output json
```

### List role assignments for your Resource Group

First, set your Resource Group name:

```bash
RG="<YOUR_RESOURCE_GROUP>"
```

Get the Resource Group ID:

```bash
RG_ID=$(az group show \
  --name "$RG" \
  --query id \
  --output tsv)
```

List role assignments at that scope:

```bash
az role assignment list \
  --scope "$RG_ID" \
  --output table
```

To include assignments inherited from parent scopes:

```bash
az role assignment list \
  --scope "$RG_ID" \
  --include-inherited \
  --output table
```

**Note:** Your sandbox identity may not have permission to enumerate every assignment.

📸 **Screenshot 6**

`06-rbac-cli-verification.png`

---

# PART 12 — Principle of Least Privilege

## Step 13 — Understand least privilege

The principle of least privilege means granting only the permissions necessary to perform a task.

### Example

A developer only needs to view production resources.

Bad approach:

```text
Developer
    |
    v
Owner Role
    |
    v
Production Subscription
```

Better approach:

```text
Developer
    |
    v
Reader Role
    |
    v
Required Production Resource Group
```

### Real-world DevOps scenario

Imagine your Jenkins pipeline needs to deploy an application to Azure.

Instead of assigning Owner at the subscription level, you should provide only the permissions required for deployment at the narrowest practical scope.

This reduces unnecessary access.

### AZ-900 exam point

**Least privilege = Minimum necessary permissions.**

---

# PART 13 — Multifactor Authentication (MFA)

## Step 14 — What is MFA?

MFA requires users to provide more than one authentication factor.

Common authentication factors include:

| Factor             | Example                           |
| ------------------ | --------------------------------- |
| Something you know | Password                          |
| Something you have | Authenticator app or security key |
| Something you are  | Fingerprint or facial recognition |

### Example

```text
User
 |
 | Password
 v
Microsoft Entra ID
 |
 | Additional Verification
 v
Authenticator App
 |
 v
Access Granted
```

### Why MFA?

If an attacker obtains a user's password, an additional authentication factor can help prevent unauthorized access.

### Hands-on exploration

Navigate to:

**Microsoft Entra ID → Protection**

Explore available authentication and security options.

Some features may require additional licensing or administrator permissions.

Do not change tenant-wide security settings in your sandbox.

---

# PART 14 — Single Sign-On (SSO)

## Step 15 — What is SSO?

Single Sign-On allows users to authenticate once and access multiple connected applications without signing in separately to each application.

### Example

```text
Employee
    |
    v
Microsoft Entra ID
    |
    | Authentication
    v
Single Sign-On
    |
    +-- Azure Portal
    |
    +-- Microsoft 365
    |
    +-- Enterprise Application
```

### Real-world example

A company integrates its applications with Microsoft Entra ID.

Employees authenticate through the organization's identity provider and access connected applications using SSO.

### AZ-900 exam point

**SSO improves user experience by reducing repeated authentication prompts across connected applications.**

---

# PART 15 — Conditional Access

## Step 16 — What is Conditional Access?

Microsoft Entra Conditional Access evaluates signals and applies access policies.

Signals can include:

* User or group
* Application
* Location
* Device state
* Sign-in risk

### Example

```text
User Login
    |
    v
Microsoft Entra ID
    |
    v
Conditional Access Policy
    |
    +-- Trusted Device?
    |
    +-- Allowed Location?
    |
    +-- MFA Required?
    |
    v
Grant or Block Access
```

### Example scenario

A company requires MFA when employees access a sensitive application.

Conditional Access can enforce that requirement.

### Hands-on exploration

Navigate to:

**Microsoft Entra ID → Protection → Conditional Access**

Review the available interface and existing policies if permitted.

**Do not create or enable tenant-wide policies in a shared training environment.**

Conditional Access policy management generally requires appropriate licensing and permissions.

---

# PART 16 — Zero Trust Security

## Step 17 — What is Zero Trust?

Zero Trust is a security approach based on three principles:

1. Verify explicitly.
2. Use least-privilege access.
3. Assume breach.

### Example

Traditional assumption:

```text
Inside Corporate Network
         |
         v
      Trusted
```

Zero Trust approach:

```text
Access Request
      |
      v
Verify Identity
      |
      v
Evaluate Device and Context
      |
      v
Apply Least Privilege
      |
      v
Allow or Deny Access
```

### AZ-900 exam point

**Zero Trust does not automatically trust a request simply because it originates inside a corporate network.**

---

# PART 17 — Managed Identities

## Step 18 — What is a managed identity?

A managed identity provides an identity for an Azure resource that can authenticate to supported services using Microsoft Entra ID.

It helps applications avoid storing credentials in application code.

### Example

```text
Azure App Service
        |
        v
Managed Identity
        |
        v
Microsoft Entra ID
        |
        v
Azure Storage
```

### Real-world DevOps scenario

Imagine a Python application running in Azure App Service needs to access Azure Blob Storage.

Instead of storing an account key in the application, you can configure a managed identity and assign the appropriate Blob data role.

### Types of managed identities

| Type            | Description                                                                  |
| --------------- | ---------------------------------------------------------------------------- |
| System-assigned | Identity tied to one Azure resource                                          |
| User-assigned   | Standalone identity that can be associated with multiple supported resources |

### AZ-900 key learning

Managed identities reduce the need to manage application credentials manually.

This is a conceptual exercise for Lab 7. You do not need to recreate your deleted Lab 6 application.

---

# PART 18 — RBAC vs Microsoft Entra Roles

This distinction is useful for AZ-900.

| Azure RBAC                         | Microsoft Entra Roles                                    |
| ---------------------------------- | -------------------------------------------------------- |
| Controls access to Azure resources | Controls directory administration                        |
| Example: VM permissions            | Example: User administration                             |
| Reader, Contributor, Owner         | Global Administrator, User Administrator                 |
| Assigned at Azure resource scopes  | Assigned at supported directory or administrative scopes |

### Example

An Azure subscription Owner does not automatically become a Microsoft Entra Global Administrator.

Similarly, a Microsoft Entra Global Administrator does not automatically have Owner permissions on every Azure subscription.

---

# PART 19 — Troubleshooting Scenarios

## Scenario 1 — User can log in but cannot create a VM

**Possible cause:** Insufficient Azure RBAC permissions.

Troubleshooting:

```text
User Authenticated
       |
       v
Check Azure RBAC
       |
       v
Check Assigned Role
       |
       v
Check Assignment Scope
       |
       v
Verify Required Permissions
```

---

## Scenario 2 — Reader cannot upload a blob

**Possible cause:** Reader grants management-plane read access but not Blob data write access.

A suitable data-plane role, such as **Storage Blob Data Contributor**, may be required.

---

## Scenario 3 — User has Reader but can modify resources

**Possible cause:** The user has another role assignment that grants additional permissions.

Azure RBAC allows permissions to be combined across applicable role assignments.

---

## Scenario 4 — User cannot see a role assignment

Possible causes include:

* Insufficient permission to read role assignments.
* Incorrect subscription.
* Incorrect scope.
* Recently changed permissions that have not fully propagated.

---

# PART 20 — Lab 7 Screenshots

Create this directory:

```text
lab-07-entra-id-rbac/
│
├── README.md
│
└── screenshots/
    ├── 01-entra-id-overview.png
    ├── 02-entra-id-users.png
    ├── 03-entra-id-groups.png
    ├── 04-azure-rbac-roles.png
    ├── 05-rbac-role-assignments.png
    ├── 06-rbac-cli-verification.png
    └── 07-conditional-access-overview.png
```

Only include screenshots for exercises you actually completed.

Redact personal identities, tenant IDs, subscription IDs, and other sensitive details.

---

# PART 21 — AZ-900 Practice Questions

Try answering these without looking at the explanations.

| #  | Question                                                                             |
| -- | ------------------------------------------------------------------------------------ |
| 1  | What is Microsoft Entra ID?                                                          |
| 2  | What is an Azure tenant?                                                             |
| 3  | What is the difference between authentication and authorization?                     |
| 4  | What is Azure RBAC?                                                                  |
| 5  | What is the difference between Reader, Contributor, and Owner?                       |
| 6  | What are the four main Azure RBAC scopes?                                            |
| 7  | What happens when Reader is assigned at the subscription level?                      |
| 8  | What is the principle of least privilege?                                            |
| 9  | What is MFA?                                                                         |
| 10 | What is Single Sign-On?                                                              |
| 11 | What is Conditional Access?                                                          |
| 12 | What are the three principles of Zero Trust?                                         |
| 13 | What is a managed identity?                                                          |
| 14 | What is the difference between system-assigned and user-assigned managed identities? |
| 15 | What is the difference between Azure RBAC and Microsoft Entra roles?                 |

---

# PART 22 — Lab Completion Checklist

| Task                                          | Status |
| --------------------------------------------- | ------ |
| Explore Microsoft Entra ID                    | ⬜      |
| Understand tenants                            | ⬜      |
| Explore users                                 | ⬜      |
| Explore groups                                | ⬜      |
| Understand authentication vs authorization    | ⬜      |
| Explore Azure RBAC roles                      | ⬜      |
| Inspect Resource Group IAM                    | ⬜      |
| Check your own role assignments               | ⬜      |
| Verify roles using Azure CLI                  | ⬜      |
| Understand least privilege                    | ⬜      |
| Explore MFA concepts                          | ⬜      |
| Explore SSO concepts                          | ⬜      |
| Explore Conditional Access                    | ⬜      |
| Understand Zero Trust                         | ⬜      |
| Understand managed identities                 | ⬜      |
| Save screenshots                              | ⬜      |
| Remove optional test assignments/users/groups | ⬜      |

---

# PART 23 — Cleanup

Unlike Lab 6, most Lab 7 activities are read-only.

If you only explored Entra ID and Azure RBAC, **there are no resources to delete**.

If you created a test user, group, or role assignment, remove only those objects you created and are authorized to manage.

Do not delete or modify existing Pluralsight sandbox identities, groups, or role assignments.

---

# What You'll Learn for AZ-900

By the end of Lab 7, you should be able to explain:

| Topic              | Key understanding                                                |
| ------------------ | ---------------------------------------------------------------- |
| Microsoft Entra ID | Cloud identity and access management                             |
| Tenant             | Dedicated identity directory                                     |
| Users              | Individual identities                                            |
| Groups             | Collections of identities                                        |
| Authentication     | Verifying identity                                               |
| Authorization      | Determining permissions                                          |
| Azure RBAC         | Authorization for Azure resources                                |
| Reader             | Read-only management access                                      |
| Contributor        | Manage resources                                                 |
| Owner              | Manage resources and access                                      |
| RBAC Scope         | Where permissions apply                                          |
| Least Privilege    | Minimum required access                                          |
| MFA                | Multiple authentication factors                                  |
| SSO                | Access multiple applications through a shared sign-in experience |
| Conditional Access | Apply policies based on signals and conditions                   |
| Zero Trust         | Verify explicitly, least privilege, assume breach                |
| Managed Identity   | Azure-managed workload identity                                  |

---

## Your Phase 2 Progress

| Lab       | Topic                                | Status         |
| --------- | ------------------------------------ | -------------- |
| Lab 5     | Azure Storage Account & Blob Storage | ✅ Completed    |
| Lab 6     | Azure App Service (PaaS)             | ✅ Completed    |
| **Lab 7** | **Microsoft Entra ID & Azure RBAC**  | 🔄 In progress |

