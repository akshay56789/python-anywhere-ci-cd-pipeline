# Python Anywhere CI/CD pipeline POC



I have created CI/CD pipelines to automatically deploy code updates on Github repository to pythonanywhere web application. 

Automating Code Deployment from GitHub to PythonAnywhere

Overview

This document provides a step-by-step guide to automatically deploy code updates from a GitHub repository to a PythonAnywhere web application using GitHub Actions and the PythonAnywhere API.

1. Prerequisites

Before setting up automation, ensure you have:

A PythonAnywhere account (Free or Paid)

A GitHub repository with your project

API access enabled on PythonAnywhere (for Free users)

A web app running on PythonAnywhere

2. Enable API Access on PythonAnywhere

To use the PythonAnywhere API:

Go to PythonAnywhere Account Settings

Scroll to API Token and click "Create API Token" (if not already created).

Copy the API Token, as it will be needed later.

3. Clone Your GitHub Repository on PythonAnywhere

Open the Bash console on PythonAnywhere.

Run the following command to clone your repository:

git clone https://github.com/yourusername/yourrepository.git

Navigate to your project directory:

cd yourrepository

4. Automate Deployment Using GitHub Actions

GitHub Actions will automatically update your PythonAnywhere code whenever you push changes.

Step 1: Add API Token as a GitHub Secret

Go to your GitHub repository → Settings → Secrets and variables → Actions

Click "New Repository Secret"

Add the API Token:

Name: PA_API_TOKEN

Value: Paste your PythonAnywhere API token

Click "Save".

Step 2: Create a GitHub Actions Workflow

In your GitHub repository, create a file:
📄 .github/workflows/deploy.yml

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
        
Step 3: Modify the Workflow File

Replace your_username with your PythonAnywhere username.

Replace yourrepository with your GitHub repository name.

Replace your_console_id (Find it by listing consoles via API: https://www.pythonanywhere.com/api/v0/user/your_username/consoles/).

Ensure the correct branch (main) is specified in the workflow.

5. Testing the Deployment

Push a change to your GitHub repository.

Go to GitHub → Actions and verify the workflow execution.

If successful, check your PythonAnywhere project for the updated code.

The web app will automatically reload after deployment.

6. Manual Deployment (If Needed)

If GitHub Actions is not used, you can manually pull updates:

cd yourrepository
git pull origin main

To reload the web app manually:

touch /var/www/your_username_pythonanywhere_com_wsgi.py

7. Troubleshooting

Issue

Solution

Authentication error

Ensure the API token is correctly added in GitHub Secrets.

Changes not reflecting

Verify git pull works in the PythonAnywhere console.

Console ID issue

Use API to list active consoles and find the correct console_id.

Conclusion

This guide helps automate deployment from GitHub to PythonAnywhere using API calls. Once set up, every push to GitHub updates the PythonAnywhere project automatically and reloads the web app. 🚀



This should start the server on http://127.0.0.1:8000/ or http://localhost:8000/.

Nice work
