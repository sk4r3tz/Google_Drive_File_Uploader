# Google Drive File Upload GUI (Python)

A lightweight desktop application built with Python that allows users to select a file from their computer and upload it directly to a specified Google Drive folder using secure OAuth 2.0 authentication.

---

## Features

- Secure OAuth 2.0 authentication with Google Drive
- Token persistence (`token.json`) to avoid repeated logins
- Native file selection dialog (Tkinter)
- Upload files to a specific Google Drive folder
- Automatic MIME type detection
- Resumable uploads for improved reliability
- GUI-based success and error notifications
- Environment variable configuration support

---

## Tech Stack

- Python 3.x  
- Tkinter (GUI)  
- Google Drive API v3  
- google-auth  
- google-auth-oauthlib  
- google-api-python-client  
- python-dotenv  

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/google-drive-upload-gui.git
cd google-drive-upload-gui
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install google-auth google-auth-oauthlib google-api-python-client python-dotenv
```

---

## Google Cloud Setup

1. Go to Google Cloud Console.
2. Create a new project.
3. Enable **Google Drive API**.
4. Navigate to **APIs & Services → Credentials**.
5. Create **OAuth 2.0 Client ID** (Desktop Application).
6. Download `credentials.json`.
7. Place `credentials.json` in the project root directory.

---

## Environment Variables

Create a `.env` file in the root directory:

```env
FOLDER_ID=your_google_drive_folder_id_here
```

### How to Get Folder ID

Open your target Google Drive folder in your browser:

```
https://drive.google.com/drive/folders/<FOLDER_ID>
```

Copy the value after `/folders/`.

---

## Usage

Run the application:

```bash
python main.py
```

### Execution Flow

1. The app authenticates with Google Drive.
2. If no valid token exists, a browser window opens for login.
3. A file selection dialog appears.
4. Select a file.
5. The file uploads to the configured Drive folder.
6. A success or error popup is displayed.

---

## Project Structure

```
google-drive-upload-gui/
│
├── main.py              # Main application script
├── credentials.json     # OAuth credentials (manual download)
├── token.json           # Auto-generated access token
├── .env                 # Environment variables (contains FOLDER_ID)
├── venv/                # Virtual environment (optional)
└── README.md
```

---

## Example Console Output

```
Starting Google Drive Upload Script...
Authentication successful.
Uploading 'example.pdf' to Google Drive...
Successfully uploaded! File ID: 1AbCdEfGhIjKlMnOpQrStUvWxYz
```

Popup message:

```
File successfully uploaded to Google Drive!

File: example.pdf
```

---

## Security Best Practices

Add the following to your `.gitignore`:

```
token.json
credentials.json
.env
venv/
__pycache__/
```

- Never commit `credentials.json`
- Never commit `token.json`
- Keep `.env` private

---

## Scope Used

```
https://www.googleapis.com/auth/drive.file
```

This scope allows the application to access and manage only the files it creates.

---

## Future Improvements

- Upload progress indicator
- Drag-and-drop support
- Multiple file upload support
- Select Drive folder from UI
- Logging system
- Packaging into executable (.exe)
- Modern GUI redesign (PyQt / CustomTkinter)

---

# LICENSE (MIT)

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
