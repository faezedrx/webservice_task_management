# 📋 webservice_task_management

**Overview**

This repository contains a simple Task Management web application built with Streamlit. The app allows users to manage tasks by adding, editing, completing, and deleting tasks stored in a Google Sheet.

## 🗂️Files

- app.py: Main application file containing the Streamlit app code.
- credentials.json: JSON file containing Google API credentials.
- requirements.txt: File listing the required Python packages.
  
## ⚙️Setup Instructions

### Prerequisites

- 🐍 Python 3.6 or higher
- 📊 A Google account with access to Google Sheets

### Installation

**Clone the repository:**

`git clone https://github.com/yourusername/webservice_task_management.git`
`cd webservice_task_management`

**Create a virtual environment and activate it:**

`python -m venv venv`
`source venv/bin/activate  # On Windows, use `venv\Scripts\activate``

**Install the required packages:**

`pip install -r requirements.txt`


**Set up Google API credentials:**

- Go to the Google Cloud Console.
- Create a new project or select an existing project.
- Enable the Google Sheets API and Google Drive API.
- Create a service account and download the JSON key file.
- Rename the JSON key file to credentials.json and place it in the repository directory.

**Update the Google Sheet URL in app.py:**

- Open your Google Sheet and copy the URL.
- Replace the value of spreadsheet_url in app.py with your Google Sheet URL.

**Running the Application**

Run the Streamlit app:

`streamlit run app.py`

## 🚀Usage
1- Open the app in your web browser (Streamlit will provide a local URL).
2- Use the form to add new tasks.
3- View, edit, complete, and delete tasks using the provided buttons and checkboxes.
4- The tasks and their statuses will be reflected in the linked Google Sheet.

## 🗂️Files Description

**`app.py`**
Contains the main code for the Streamlit application:
- 🔐 Authenticates and connects to the Google Sheet.
- 🛠️ Provides functions to read, add, complete, delete, and edit tasks.
- 🖥️ Displays tasks in a user-friendly interface with options to manage them.
- 
**`credentials.json`**
Contains the service account credentials for accessing the Google Sheets API. Ensure this file is not exposed publicly.

**`requirements.txt`**
Lists the Python packages required to run the application:

- `streamlit`: Web framework for the app.
- `gspread`: Library to interact with Google Sheets.
- `oauth2client`: Library to handle OAuth2 authentication.
- `pandas`: Library for data manipulation and analysis.

## 📝License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🛠️Acknowledgements
This project uses the following libraries and services:

- `Streamlit`
- `gspread`
- `oauth2client`
- `pandas`
- `Google Sheets API`
Feel free to contribute to this project by submitting issues or pull requests. For any questions, contact your.faezedrx@gmail.com.
