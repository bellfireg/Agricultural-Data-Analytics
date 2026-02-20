# 🔑 How to Get a GitHub Personal Access Token (PAT)

Since I am running in the terminal, I cannot "click" the buttons in VS Code. I need a **Personal Access Token** to push code on your behalf.

## Step 1: Generate the Token
1.  Go to **[GitHub Developer Settings > Personal Access Tokens (Tokens (classic))](https://github.com/settings/tokens/new)**.
2.  **Note**: Give it a name like "Antigravity Agent".
3.  **Expiration**: Set to **"No expiration"** (or 30 days if you prefer).
4.  **Select Scopes** (Permissions):
    *   ✅ **repo** (Full control of private repositories) - *This is the most important one.*
    *   ✅ **workflow** (Update GitHub Action workflows).
5.  Scroll down and click **Generate token**.

## Step 2: Copy and Share
1.  **Copy the token immediately**. It starts with `ghp_...`.
2.  Paste it in the chat for me.

---
**Why do I need this?**
VS Code handles its own login, but I operate in the command line. This token acts like a password for the terminal.
