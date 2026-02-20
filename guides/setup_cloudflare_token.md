# 🔐 How to Create Your Cloudflare API Token

Based on the screenshots you provided, here is the exact configuration you need for the **Agri-Data Factory**.

## Step 1: Choose the Template
*From your first screenshot:*
1.  In the "API token templates" list.
2.  Find **"Edit Cloudflare Workers"**.
3.  Click the blue **Use template** button next to it.
    *   *Why? This template pre-fills 80% of what we need for the backend.*

## Step 2: Configure Permissions (The "Create Token" Form)
*From your second screenshot:*
You need to ensure the following permissions are set in the **"Permissions"** box.
The template will add some defaults, but **verify** and **add** these extra ones for our Data Factory (Storage):

| Group | Resource | Permission Level | Why? |
| :--- | :--- | :--- | :--- |
| `Account` | **Workers Scripts** | **Edit** | To deploy your API. |
| `Account` | **Workers KV Storage** | **Edit** | To save simple data. |
| `Account` | **Workers R2 Storage** | **Edit** | **CRITICAL**: For storing satellite images/maps. |
| `Account` | **Cloudflare Pages** | **Edit** | To deploy the frontend dashboard. |
| `User` | **User Details** | **Read** | To verify your identity. |
| `Account` | **Account Settings** | **Read** | To find your Account ID. |

**👉 Action:**
1.  Look at the list.
2.  If **Workers R2 Storage** or **Cloudflare Pages** is missing, click `+ Add more` at the bottom of the permission box.
3.  Select `Account` -> `Workers R2 Storage` -> `Edit`.

## Step 3: Account Resources
*From your third screenshot:*
1.  Under **"Account Resources"**:
2.  Select **Include** -> **All accounts** (or select your specific account name if accessible).

## Step 4: Finish
1.  Click **"Continue to summary"**.
2.  Click **"Create Token"**.
3.  🚨 **COPY THE TOKEN IMMEDIATELY.** You will never see it again.
