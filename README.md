# Python Anywhere CI/CD pipeline POC

# Automating Code Deployment from GitHub to PythonAnywhere

## Overview

This document provides a step-by-step guide to automatically deploy code updates from a GitHub repository to a PythonAnywhere web application using GitHub Actions and the PythonAnywhere API.

## 1. Prerequisites

Before setting up automation, ensure you have:

- A PythonAnywhere account (Free or Paid)
- A GitHub repository with your project
- API access enabled on PythonAnywhere (for Free users)
- A web app running on PythonAnywhere

## 2. Enable API Access on PythonAnywhere

To use the PythonAnywhere API:

1. Go to **PythonAnywhere Account Settings**
2. Scroll to **API Token** and click **"Create API Token"** (if not already created).
3. Copy the API Token, as it will be needed later.

## 3. Clone Your GitHub Repository on PythonAnywhere

Open the Bash console on PythonAnywhere and run the following commands:

```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
```
First of all, ensure that your web app runs without any issues.

## 4. Automate Deployment Using GitHub Actions

GitHub Actions will automatically update your PythonAnywhere code whenever you push changes.

### Step 1: Add API Token as a GitHub Secret

1. Go to **GitHub repository → Settings → Secrets and variables → Actions**
2. Click **"New Repository Secret"**
3. Add the API Token:
   - **Name:** `PA_API_TOKEN`
   - **Value:** Paste your PythonAnywhere API token
4. Click **"Save"**.

### Step 2: Create a GitHub Actions Workflow

In your GitHub repository, create a file:

📄 `.github/workflows/deploy.yml`

```yaml
name: Deploy to PythonAnywhere

on:
  push:
    branches:
      - master

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Update code on PythonAnywhere
      run: |
        curl -s -X POST \
        "https://www.pythonanywhere.com/api/v0/user/${{ secrets.PA_USERNAME }}/consoles/38366532/send_input/" \
        -H "Authorization: Token ${{ secrets.PA_API_TOKEN }}" \
        -d '{"input": "git pull origin master\n"}' \
        -H "Content-Type: application/json"

    - name: Reload PythonAnywhere Web App
      run: |
        curl -s -X POST \
        "https://www.pythonanywhere.com/api/v0/user/${{ secrets.PA_USERNAME }}/webapps/${{ secrets.PA_USERNAME }}.pythonanywhere.com/reload/" \
        -H "Authorization: Token ${{ secrets.PA_API_TOKEN }}"
```

### Step 3: Modify the Workflow File

- Replace **your_username** with your PythonAnywhere username.
- Replace **yourrepository** with your GitHub repository name.
- Replace **your_console_id** (Find it by listing consoles via API: `https://www.pythonanywhere.com/api/v0/user/your_username/consoles/`).
- Ensure the correct branch (**main** or **master**) is specified in the workflow.

## 5. Testing the Deployment

1. Push a change to your GitHub repository.
2. Go to **GitHub → Actions** and verify the workflow execution.
3. If successful, check your PythonAnywhere project for the updated code.
4. The web app will automatically reload after deployment.
5. **If your web app does not reflect the changes you made, then check the bash console by opening your pythonAnywhere dashboard and check whether the directory is correct. for eg./your_repo_name (master)$. Again run the workflow.

## 6. Manual Deployment (If Needed)

If GitHub Actions is not used, you can manually pull updates:

```bash
cd yourrepository
git pull origin main
```

To reload the web app manually:

```bash
touch /var/www/your_username_pythonanywhere_com_wsgi.py
```

## 7. Troubleshooting

| Issue | Solution |
|--------|----------|
| **Authentication error** | Ensure the API token is correctly added in GitHub Secrets. |
| **Changes not reflecting** | Verify `git pull` works in the PythonAnywhere console. |
| **Console ID issue** | Use API to list active consoles and find the correct `console_id`. |

## Conclusion

This guide helps automate deployment from GitHub to PythonAnywhere using API calls. Once set up, every push to GitHub updates the PythonAnywhere project automatically and reloads the web app. 🚀

Testing the CI/CD pipeline:
Edit this line and the changes will be reflected in website's python anywhere repository code.







