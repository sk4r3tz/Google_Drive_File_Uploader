Google Drive File Upload GUI (Python)
Short Description

A simple Python desktop application that allows users to select a file from their computer and upload it directly to a specific Google Drive folder using OAuth 2.0 authentication.

Features

OAuth 2.0 authentication with Google Drive

Secure token storage (token.json) for future sessions

File selection via native file dialog (Tkinter)

Upload files directly to a specific Google Drive folder

Automatic MIME type detection

Resumable uploads for reliability

User-friendly success and error message popups

Environment variable support for secure folder configuration

Tech Stack

Python 3.x

Tkinter – GUI file dialog and message boxes

Google Drive API v3

google-auth

google-auth-oauthlib

google-api-python-client

python-dotenv

Installation Instructions
1. Clone the Repository
git clone https://github.com/your-username/google-drive-upload-gui.git
cd google-drive-upload-gui
2. Create a Virtual Environment (Recommended)
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3. Install Dependencies
pip install google-auth google-auth-oauthlib google-api-python-client python-dotenv
Google Cloud Setup

Go to Google Cloud Console.

Create a new project.

Enable Google Drive API.

Go to APIs & Services → Credentials.

Create OAuth 2.0 Client ID (Desktop App).

Download the credentials.json file.

Place credentials.json in the root project directory.

Environment Variables

Create a .env file in the root directory:

FOLDER_ID=your_google_drive_folder_id_here
How to Get Folder ID

Open your target Google Drive folder in the browser:

https://drive.google.com/drive/folders/1aBcDeFgHiJkLmNoPqRsTuVwXyZ

The folder ID is:

1aBcDeFgHiJkLmNoPqRsTuVwXyZ
Usage Instructions

Run the script:

python main.py
Workflow

The app starts authentication.

A browser window opens (first time only) for Google login.

After authentication, a file selection dialog appears.

Choose a file.

The file uploads to the configured Google Drive folder.

A success or error popup appears.

Project Structure
google-drive-upload-gui/
│
├── main.py              # Main application script
├── credentials.json     # Google OAuth credentials (manual download)
├── token.json           # Auto-generated OAuth token (after first login)
├── .env                 # Environment variables (contains FOLDER_ID)
├── venv/                # Virtual environment (optional)
└── README.md
Authentication Flow

Checks for token.json

If valid → use existing token

If expired → refresh token

If missing → start OAuth local server flow

Saves token for future use

Builds Google Drive API service instance

Scope used:

https://www.googleapis.com/auth/drive.file

This scope allows the app to access and manage only files it creates.

Example Console Output
Starting Google Drive Upload Script...
Authentication successful.
Uploading 'example.pdf' to Google Drive...
Successfully uploaded! File ID: 1AbCdEfGhIjKlMnOpQrStUvWxYz

Popup:

File successfully uploaded to Google Drive!

File: example.pdf
Error Handling

The application handles:

Missing credentials.json

Expired or invalid token.json

Google API errors

File selection cancellation

Non-existent file paths

Upload failures

All major errors show a GUI message box and log details to the console.

Future Improvements

Drag-and-drop support

Progress bar for upload status

Multi-file upload

Folder selection from Drive UI

Logging system

Packaging as executable (.exe)

GUI redesign using PyQt or CustomTkinter

Security Notes

Do not expose credentials.json

Do not commit token.json

Keep .env private

Consider adding .gitignore:

token.json
credentials.json
.env
venv/
License

This project is licensed under the MIT License.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
