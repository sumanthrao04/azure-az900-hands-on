# Lab 05 — Azure Storage: What I Learned (AZ-900 Exam Notes)

> **Learning track:** Microsoft Azure Fundamentals (AZ-900)  
> **Phase:** 2 — Application, Storage & Security  
> **Lab:** Azure Storage Account & Blob Storage  
> **Status:** Study notes; mark hands-on tasks complete only after verifying them.

## 1. Lab objective

Understand the major Azure Storage services, create a storage account and a private blob container, upload/download objects, explore secure access, and compare access tiers and redundancy options. These notes are designed for quick **AZ-900 exam revision** and DevOps interview recall.

## 2. Lab architecture

```text
Azure Subscription
└── Resource Group (lab sandbox)
    └── Storage Account (Standard, StorageV2, LRS)
        ├── Blob service
        │   └── Private container: az900-container
        │       ├── sample.txt
        │       └── application.log
        ├── Azure Files (explored)
        ├── Queue Storage (explored)
        └── Table Storage (explored)

Client ── HTTPS + authorized identity / SAS ──> Blob endpoint
```

**Note:** A storage account is an Azure resource; its containers and blobs are data objects inside it. Azure managed disks are a related storage offering but aren't created as containers in the Blob service.

## 3. Topic-by-topic learning and exam points

### 3.1 Azure Storage account

A **storage account** is the top-level Azure resource that provides a unique namespace and configuration for supported storage services. Its settings include region, performance tier, redundancy, security, and networking.

- **General-purpose v2 (StorageV2):** recommended general-purpose account for blobs, files, queues and tables.
- **Standard vs Premium:** Standard suits general-purpose workloads; Premium is optimized for particular performance-sensitive storage workloads and has service-specific account types.
- **Naming:** globally unique, 3–24 characters, lowercase letters and digits only.
- **Exam memory:** *Storage account = namespace + storage configuration; container = logical grouping of blobs.*

### 3.2 Azure storage services

| Service | What it stores / provides | Example | AZ-900 clue |
|---|---|---|---|
| **Blob Storage** | Unstructured object data | Images, logs, backups, videos | Object storage |
| **Azure Files** | Managed SMB/NFS file shares | Shared files for servers | File share / lift-and-shift |
| **Queue Storage** | Messages between components | Background job queue | Asynchronous messaging |
| **Table Storage** | Schemaless NoSQL key/attribute data | Metadata records | NoSQL key-value-style data |
| **Azure Managed Disks** | Block storage for Azure VMs | OS/data disks | VM disk storage |

**Exam trap:** Azure Files is not the same thing as Blob Storage. Azure Files exposes file shares; Blob Storage stores objects through blob APIs.

### 3.3 Blob containers and blobs

A **container** organizes blobs in a storage account. A **blob** is an individual object such as `sample.txt` or `application.log`.

```text
Storage Account
└── az900-container (private)
    ├── sample.txt
    └── application.log
```

Basic operations: create a container, upload, list, download, delete blobs. Private containers require authorized access.

**Exam memory:** *Blob = object; container = group of blobs; storage account = parent Azure resource.*

### 3.4 Blob types

| Blob type | Intended purpose |
|---|---|
| **Block blob** | Documents, images, log files, general objects |
| **Append blob** | Append-oriented workloads such as logging |
| **Page blob** | Random read/write workloads; historically associated with virtual hard disks |

For a basic upload of `sample.txt`, think **block blob**.

### 3.5 Access tiers: Hot, Cool, Cold, Archive

| Tier | Access pattern | Key trade-off |
|---|---|---|
| **Hot** | Frequently accessed | Higher storage cost, lower access cost |
| **Cool** | Infrequently accessed | Lower storage cost, higher access/retrieval cost; minimum retention charges may apply |
| **Cold** | Rarely accessed | Even lower storage cost, higher retrieval cost; minimum retention charges may apply |
| **Archive** | Long-term, rarely retrieved | Offline tier: rehydrate before normal reading; retrieval delay and charges |

**Exam scenarios:** Frequently downloaded images → **Hot**. Older reports occasionally retrieved → **Cool**. Very rarely accessed data that must remain online → **Cold**. Long-term records that can tolerate retrieval delays → **Archive**.

**Important:** Not every blob/account type supports every tier; check the account's available options. Tier changes and early deletion can generate charges.

### 3.6 Storage redundancy

| Option | Copies / location | Protects against |
|---|---|---|
| **LRS** | Three synchronous copies in one physical location in the primary region | Local hardware failure |
| **ZRS** | Synchronous copies across availability zones in the primary region | Zone failure |
| **GRS** | LRS in primary + asynchronous replication to a secondary region | Regional disaster, subject to failover |
| **GZRS** | ZRS in primary + asynchronous replication to a secondary region | Zone failure and regional disaster |
| **RA-GRS / RA-GZRS** | GRS/GZRS plus read access to secondary endpoint | Read access to replicated secondary data |

**Exam memory:** *L = local; Z = zones; G = geo; RA = read-access secondary.*

**Exam trap:** Geo-replication is asynchronous, so secondary data may lag the primary. GRS doesn't mean writes automatically happen in both regions.

### 3.7 Public endpoint vs anonymous access

A storage account can have a **public network endpoint** without allowing **anonymous public reading** of its blobs.

- **Public network access:** determines which networks can reach the endpoint.
- **Authorization:** determines whether the request can read/write data.
- **Private container:** anonymous requests should not retrieve the blobs.
- **Private endpoint:** connects privately through an Azure VNet; conceptually different from making a container private.

**Exam trap:** *Public network access enabled ≠ blobs are public.*

### 3.8 Authentication and authorization

- **Microsoft Entra ID + Azure RBAC:** preferred for many Azure Storage data-access scenarios; applications can use managed identities.
- **Shared Key:** account key authorizes broad access and must be protected.
- **SAS (Shared Access Signature):** delegates specific permissions to storage resources for a limited period.
- **Management plane vs data plane:** permission to manage a storage account does **not** necessarily grant permission to read blobs. Data roles such as **Storage Blob Data Reader** or **Storage Blob Data Contributor** may be required.

**Exam memory:** *RBAC = who can do what at which scope; SAS = delegated, scoped, time-limited access.*

### 3.9 Shared Access Signature (SAS)

A SAS token can specify permissions (e.g. **Read**), resource scope, start/expiry time, and protocol restrictions. A SAS URL acts like a credential: anyone holding a valid one may exercise its permissions.

```text
Without authorization: client -> private blob -> denied
With valid read SAS:   client -> private blob -> read allowed
```

SAS varieties to recognize:

- **User delegation SAS:** secured with Microsoft Entra credentials; preferred where supported for Blob Storage.
- **Service SAS:** access to a specific storage service using Shared Key authorization.
- **Account SAS:** access across supported services and operations using Shared Key authorization.

**Security:** Prefer HTTPS, minimal permissions, short expiry, and never commit SAS URLs or account keys to GitHub.

### 3.10 Secure transfer and encryption

- **Secure transfer required:** enforces HTTPS for supported requests.
- **TLS:** protects data in transit.
- **Encryption at rest:** Azure Storage encrypts data at rest by default.
- **Network controls:** firewalls and private endpoints can restrict network paths.

**Exam memory:** *TLS/HTTPS = in transit; Storage Service Encryption = at rest.*

### 3.11 Azure CLI basics

Replace placeholders with actual lab resource names:

```bash
# Management-plane: inspect accounts
az storage account list --output table
az storage account show --name <account-name> --resource-group <resource-group> --output table

# Data-plane: requires appropriate blob data permissions
az storage container list --account-name <account-name> --auth-mode login --output table
az storage blob list --account-name <account-name> --container-name az900-container --auth-mode login --output table
```

If a data command fails with `AuthorizationPermissionMismatch` or another authorization error, check **Blob data-plane RBAC** and networking rather than assuming the storage account is missing.

### 3.12 Costs and lifecycle management

Azure Storage cost depends on capacity, tier, redundancy, operations, retrieval, and data transfer. Lifecycle management policies can automatically transition eligible blobs between tiers or delete them based on rules.

**Exam scenario:** To reduce cost for old, infrequently accessed blobs, evaluate **access tiers** and **lifecycle management** rather than immediately adding more storage accounts.

### 3.13 Related AZ-900 topics worth recognizing

- **AzCopy:** command-line utility for copying data to/from Azure Storage.
- **Azure Storage Explorer:** GUI tool for working with Azure Storage data.
- **Azure File Sync:** centralizes file shares in Azure Files while caching files on Windows Servers.
- **Azure Data Box:** physical data transfer option for very large offline data migrations.

These are conceptual study topics; they were **not all deployed** in this lab.

## 4. Hands-on verification checklist

- [ ] Storage account created (Standard / StorageV2 / LRS)
- [ ] Private blob container created
- [ ] `sample.txt` and `application.log` uploaded
- [ ] Blob downloaded and contents verified
- [ ] Anonymous blob URL tested (access denied)
- [ ] Short-lived read-only SAS tested **if permitted**
- [ ] Access tiers inspected (optional Hot → Cool test)
- [ ] Redundancy options reviewed
- [ ] CLI management-plane commands tested
- [ ] CLI blob commands tested **if RBAC permits**
- [ ] Screenshots saved with credentials redacted
- [ ] Lab storage account deleted after evidence collected

**Restricted lab note:** If sandbox permissions block SAS, RBAC, or data-plane CLI operations, document the limitation instead of claiming successful verification.

## 5. Suggested screenshots

```text
screenshots/
├── 01-storage-account-overview.png
├── 02-private-blob-container.png
├── 03-uploaded-blobs.png
├── 04-anonymous-access-denied.png
├── 05-sas-settings-redacted.png
├── 06-access-tier.png
├── 07-redundancy-settings.png
└── 08-cli-verification.png
```

**Never show:** SAS query strings, storage keys, secrets, or other credentials.

## 6. AZ-900 exam practice questions (with answers)

1. **Which service stores images and log files as objects?** **Azure Blob Storage.**
2. **Which service provides a managed SMB file share?** **Azure Files.**
3. **Which storage tier is designed for frequent access?** **Hot.**
4. **Which tier requires rehydration before normal reading?** **Archive.**
5. **Which redundancy option replicates across availability zones in one region?** **ZRS.**
6. **Which options provide replication to a secondary region?** **GRS and GZRS** (including their read-access variants).
7. **What does RA-GRS add to GRS?** **Read access to the secondary region's replicated data.**
8. **What grants limited-time access to a private blob?** **A valid SAS token** (or other authorized credentials).
9. **Does a public storage endpoint mean anonymous users can read blobs?** **No.** Network reachability and authorization are separate.
10. **Can a user manage a storage account but lack permission to read its blobs?** **Yes.** Management-plane and data-plane RBAC are distinct.
11. **Which Azure service is suitable for asynchronous message storage?** **Queue Storage.**
12. **What protects storage traffic in transit?** **HTTPS/TLS.**
13. **What is the purpose of a blob container?** **To logically group blobs in a storage account.**
14. **What tool can automatically move older blobs between access tiers?** **Azure Blob lifecycle management.**
15. **What is the preferred authorization approach for many Azure-hosted applications?** **Microsoft Entra ID with RBAC/managed identity.**

## 7. Common exam confusions

| Don't confuse | Correct distinction |
|---|---|
| Blob Storage vs Azure Files | Object storage vs file shares |
| Hot vs Archive | Online frequent access vs offline archival |
| LRS vs ZRS | One physical location vs multiple zones |
| ZRS vs GRS | Zone protection vs secondary-region replication |
| Public endpoint vs public blob | Network reachability vs anonymous data access |
| Account key vs SAS | Broad shared secret vs delegated access token |
| RBAC Reader vs Storage Blob Data Reader | Management resource visibility vs blob data reading |
| Storage account vs blob container | Azure resource vs logical grouping inside Blob service |

## 8. Interview-ready summary

> In Lab 5, I studied Azure Storage and practiced storing unstructured files in a private Blob container. I learned how storage accounts organize services, how access tiers influence cost and retrieval, and how LRS, ZRS, GRS and GZRS address different resiliency requirements. I also explored the difference between network access and data authorization, including Microsoft Entra RBAC and SAS. I used Azure Portal and Azure CLI to inspect storage resources, subject to sandbox permissions.

Adjust the paragraph above to reflect only the operations you actually completed.

## 9. Lab cleanup

Delete **only the disposable storage account created for this lab**. Do not delete the shared sandbox resource group unless the lab provider explicitly instructs you to do so. Storage account deletion removes its contained data.

## 10. Next step

**Lab 6 — Azure App Service (PaaS)**, followed by **Lab 7 — Microsoft Entra ID and RBAC**. Combine Labs 5–7 into LinkedIn **Post 2**.

---

**Official study reference:** [Microsoft AZ-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) · [Azure Storage overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)
