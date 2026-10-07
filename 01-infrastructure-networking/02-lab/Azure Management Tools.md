# Lab 2 — Azure Management Tools

For **AZ-900**, the main goal is to understand that Azure gives you multiple ways to perform the same management operation.

The four you should know are:

```text
Azure Management Tools

├── Azure Portal      → GUI
├── Azure CLI         → Command line
├── Azure PowerShell  → PowerShell cmdlets
└── Azure Cloud Shell → Browser-based shell
```

One important point:

> **Cloud Shell is the environment where you can run Azure CLI or Azure PowerShell.**

So Cloud Shell isn't really a competing command language to CLI/PowerShell.

---

# 1. Azure Portal

Azure Portal is the **web-based graphical interface** for Azure.

Example:

```text
Browser
   ↓
Azure Portal
   ↓
Resource Groups
   ↓
Create
   ↓
az900-hands-on-rg
```

You select values through forms:

```text
Subscription: Azure Subscription
Resource Group: az900-hands-on-rg
Region: Central India

        ↓

Review + Create
```

### When is Portal useful?

Portal is especially useful for:

* Learning Azure
* Exploring services
* Visualizing resources
* Monitoring resources
* Troubleshooting
* Performing occasional/manual operations

But imagine you had to create:

```text
100 Resource Groups
100 VNets
100 VMs
```

Doing everything manually through the Portal would become repetitive.

That's where command-line tools and Infrastructure as Code become valuable.

---

# 2. Azure CLI

**Azure CLI** is Microsoft's cross-platform command-line tool for managing Azure resources.

Instead of:

```text
Portal
 ↓
Resource Groups
 ↓
Create
 ↓
Fill form
 ↓
Create
```

you can run:

```bash
az group create \
  --name az900-hands-on-rg \
  --location centralindia
```

Both approaches ultimately ask Azure to perform the same kind of resource-management operation.

## Understanding CLI syntax

Look at:

```bash
az group create --name az900-hands-on-rg --location centralindia
```

Break it down:

```text
az
│
└── Azure CLI

group
│
└── Resource Group commands

create
│
└── Operation

--name
│
└── Resource Group name

--location
│
└── Azure region
```

So:

```text
az + resource/service + action + parameters
```

is a useful mental model.

---

# 3. Important Azure CLI commands

You don't need to memorize hundreds of commands for AZ-900. Understand these basic examples.

### Login

```bash
az login
```

Purpose:

```text
Your computer
      ↓
Authentication
      ↓
Microsoft Entra ID
      ↓
Azure
```

---

### Check current subscription/account

```bash
az account show
```

Very useful before creating anything.

You want to know:

> **Which subscription am I currently working with?**

---

### List subscriptions

```bash
az account list --output table
```

You might have:

```text
Name                 State     IsDefault
------------------------------------------------
Azure Training       Enabled   True
Development          Enabled   False
Production           Enabled   False
```

---

### Switch subscription

Another useful command to recognize:

```bash
az account set --subscription "<subscription-name-or-id>"
```

This becomes important when an engineer has access to multiple subscriptions.

---

### List Resource Groups

```bash
az group list --output table
```

---

### Show one Resource Group

```bash
az group show --name az900-hands-on-rg
```

---

### Create Resource Group

```bash
az group create \
  --name az900-hands-on-rg \
  --location centralindia
```

---

### Delete Resource Group

Eventually you'll use:

```bash
az group delete \
  --name az900-hands-on-rg
```

Be careful with this command because deleting the resource group also initiates deletion of the resources it contains.

---

# 4. What does `--output table` mean?

You'll frequently see:

```bash
--output table
```

Azure CLI normally returns structured output, commonly JSON.

For example:

```bash
az group list
```

may produce JSON-style output.

Using:

```bash
az group list --output table
```

makes the output easier for humans to read.

You may also encounter formats such as:

```text
json
table
tsv
yaml
```

You don't need to memorize these for AZ-900.

---

# 5. Why DevOps engineers use Azure CLI

CLI becomes particularly useful for **automation and scripting**.

For example:

```text
Script
  │
  ├── Create Resource Group
  ├── Create VNet
  ├── Create VM
  └── Configure resources
```

Instead of manually clicking through the Portal each time, commands can be incorporated into repeatable workflows.

As you progress beyond AZ-900, you'll see Azure CLI used in scripts and CI/CD pipelines.

---

# 6. Azure Cloud Shell

This distinction is important.

## Azure CLI installed locally

You can install Azure CLI on your machine.

Architecture:

```text
Your Laptop
     │
     ▼
Azure CLI
     │
     ▼
Internet
     │
     ▼
Azure
```

You typically authenticate:

```bash
az login
```

and then run commands.

---

## Azure Cloud Shell

Cloud Shell gives you a **browser-accessible shell environment managed by Microsoft**.

Conceptually:

```text
Browser
   │
   ▼
Azure Cloud Shell
   │
   ├── Bash
   │     └── Azure CLI
   │
   └── PowerShell
         └── Azure PowerShell
   │
   ▼
Azure
```

This is the key concept.

### Don't think:

```text
Portal
CLI
PowerShell
Cloud Shell
```

as four completely separate languages.

Think:

```text
Management interfaces/tools
│
├── Azure Portal
│
├── Azure CLI
│
└── Azure PowerShell

Execution environment
│
└── Azure Cloud Shell
      ├── Bash / CLI
      └── PowerShell
```

That's a much clearer understanding.

---

# 7. Azure PowerShell

Azure PowerShell provides **PowerShell cmdlets** for managing Azure.

For example, Azure CLI:

```bash
az group list
```

Azure PowerShell:

```powershell
Get-AzResourceGroup
```

Both can retrieve information about Resource Groups.

---

# 8. CLI vs PowerShell syntax

Azure CLI tends to look like:

```bash
az group list
```

PowerShell looks like:

```powershell
Get-AzResourceGroup
```

Another conceptual example:

```text
Azure CLI

az group create
     ↓
Create Resource Group


Azure PowerShell

New-AzResourceGroup
     ↓
Create Resource Group
```

PowerShell cmdlets commonly use a:

```text
Verb-Noun
```

pattern.

Examples:

```powershell
Get-AzResourceGroup
New-AzResourceGroup
Remove-AzResourceGroup
```

For AZ-900, recognizing the distinction is enough.

---

# 9. Portal vs CLI vs PowerShell vs Cloud Shell

This is the table I'd put in your AZ-900 notes.

| Tool                  | What it is                       | Good for                                                        |
| --------------------- | -------------------------------- | --------------------------------------------------------------- |
| **Azure Portal**      | Web GUI                          | Learning, visualization, manual management                      |
| **Azure CLI**         | Cross-platform command-line tool | Commands, scripts, automation                                   |
| **Azure PowerShell**  | PowerShell modules/cmdlets       | PowerShell-based administration and automation                  |
| **Azure Cloud Shell** | Browser-accessible shell         | Running CLI/PowerShell without maintaining a local installation |

---

# 10. Important exam distinction

Suppose Microsoft asks:

> You are using a computer where Azure CLI isn't installed. You need to run Azure management commands from your browser.

Think:

```text
Azure Cloud Shell
```

If the question says:

> You want to manage Azure using a graphical interface.

Think:

```text
Azure Portal
```

If it says:

> You want a cross-platform command-line tool.

Think:

```text
Azure CLI
```

If it mentions:

```text
Get-AzResourceGroup
New-AzResourceGroup
```

think:

```text
Azure PowerShell
```

---

# 11. The same operation using different tools

This is the most useful way to understand Lab 2.

Suppose we want:

```text
Create Resource Group
        ↓
az900-hands-on-rg
        ↓
Central India
```

### Portal

```text
Portal
 ↓
Resource Groups
 ↓
Create
 ↓
Name: az900-hands-on-rg
Region: Central India
 ↓
Create
```

### Azure CLI

```bash
az group create \
  --name az900-hands-on-rg \
  --location centralindia
```

### PowerShell

Conceptually:

```powershell
New-AzResourceGroup `
  -Name "az900-hands-on-rg" `
  -Location "Central India"
```

Different interfaces, same Azure resource-management goal.

---

# 12. Where does ARM fit?

This will make your understanding stronger.

Behind these management tools is Azure's resource-management/control plane.

Conceptually:

```text
                You
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
     Portal     CLI    PowerShell
       │         │         │
       └─────────┼─────────┘
                 ▼
       Azure Resource Manager
              (ARM)
                 │
                 ▼
          Azure Resources
```

This explains why you can create the same resource using different tools.

Later you'll also learn declarative Infrastructure as Code approaches such as:

```text
ARM templates
Bicep
Terraform
```

Given your Terraform experience, you'll find that part familiar.

---

# 13. Hands-on exercise for Lab 2

Don't just read this section. Practice it.

### Step 1 — Open Cloud Shell

In Azure Portal, launch **Cloud Shell** and select Bash if you're practicing Azure CLI.

Run:

```bash
az account show
```

Then:

```bash
az account list --output table
```

Check which subscription is active.

### Step 2 — Create Resource Group

```bash
az group create \
  --name az900-hands-on-rg \
  --location centralindia
```

### Step 3 — Verify using CLI

```bash
az group show \
  --name az900-hands-on-rg
```

Then:

```bash
az group list --output table
```

### Step 4 — Verify through Portal

Now go to:

```text
Azure Portal
      ↓
Resource Groups
      ↓
az900-hands-on-rg
```

This is an important learning moment:

```text
Created using CLI
        ↓
Visible in Portal
```

because both are managing the same Azure environment.

### Step 5 — Try PowerShell

Switch Cloud Shell to PowerShell and run:

```powershell
Get-AzResourceGroup
```

Find:

```text
az900-hands-on-rg
```

Now you've seen the same resource through **Portal + CLI + PowerShell**.

---

# What to remember for AZ-900

Put this in your notes:

```text
AZURE MANAGEMENT TOOLS

Azure Portal
→ Web-based GUI
→ Manual management and visualization

Azure CLI
→ Cross-platform command-line tool
→ Commands, scripting and automation
→ Commands start with "az"

Azure PowerShell
→ PowerShell-based Azure management
→ Uses Az cmdlets
→ Example: Get-AzResourceGroup

Azure Cloud Shell
→ Browser-accessible shell
→ No need to maintain CLI/PowerShell locally
→ Supports Bash and PowerShell

Important:
Cloud Shell is an execution environment.
Azure CLI and Azure PowerShell are management tools.

Portal / CLI / PowerShell
          ↓
Azure Resource Manager
          ↓
Azure Resources
```

