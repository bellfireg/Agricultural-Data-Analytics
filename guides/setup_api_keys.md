# 🔑 How to Get Your API Keys (USDA & Google)

Here is the exact step-by-step guide to get the missing keys.

---

## 1. USDA API Key (The "Quick Stats" Key)
The link you found (`apps.fas.usda.gov`) is for *Foreign* trade data. For US Field Data, we need **NASS Quick Stats**.

**Where to go:**
👉 **[https://quickstats.nass.usda.gov/api](https://quickstats.nass.usda.gov/api)**

**Steps:**
1.  Click the link above.
2.  Click **"Request API Key"**.
3.  Fill in:
    *   **Name**: (Your Name)
    *   **Email**: (Your Email) - *Must be valid, they email the key to you.*
    *   **Url**: (You can just put `https://github.com/StartYourLab/agri-data-factory` or even `http://localhost`).
4.  Check your email. Copy the key.
5.  Paste it into your `.env` file as `USDA_API_KEY`.

---

## 2. Google Cloud Credentials (for Login/Drive)
This is for `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`.

**Where to go:**
👉 **[https://console.cloud.google.com](https://console.cloud.google.com)**

**Steps:**
1.  **Create Project**:
    *   Click the dropdown at the top (next to "Google Cloud").
    *   Click **"New Project"**.
    *   Name it: `Agri-Data-Factory`. Click **Create**.

2.  **Configure Consent Screen** (Required first):
    *   Search for **"OAuth consent screen"** in the top search bar.
    *   Select **External** (if asked) -> **Create**.
    *   **App Name**: `Agri Data`
    *   **Email**: Select yours.
    *   Skip the rest (Scopes/Test Users) by clicking **Save and Continue**.

3.  **Get the Keys**:
    *   Go to **"Credentials"** (left sidebar).
    *   Click **+ CREATE CREDENTIALS** (top) -> **OAuth client ID**.
    *   **Application type**: `Desktop app` (since we run it locally) OR `Web application`.
        *   *Recommendation*: Choose **Desktop app** for simplest local testing.
    *   Name: `Agri CLI Client`.
    *   Click **Create**.

4.  **Copy-Paste**:
    *   Copy **Client ID** -> Update `.env` (`GOOGLE_CLIENT_ID`).
    *   Copy **Client Secret** -> Update `.env` (`GOOGLE_CLIENT_SECRET`).
