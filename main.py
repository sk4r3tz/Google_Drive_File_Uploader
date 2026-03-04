import os
import tkinter as tk
from dotenv import load_dotenv
from tkinter import filedialog, messagebox
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# ==========================================
# CONFIGURATION
# ==========================================

# If modifying these scopes, delete the file token.json.
# 'drive.file' scope allows the app to view and manage files it creates.
SCOPES =['https://www.googleapis.com/auth/drive.file']

# ==========================================
# ENVIRONMENT INITIALIZATION
# ==========================================

# Replace this with your actual Google Drive Folder ID
# You can find the Folder ID in the URL when you open the folder in Google Drive.
# Example URL: https://drive.google.com/drive/folders/1aBcDeFgHiJkLmNoPqRsTuVwXyZ
# FOLDER_ID = 'YOUR_FOLDER_ID_HERE'

load_dotenv()  # Load environment variables from .env file

# ==========================================
# FUNCTIONS
# ==========================================

def authenticate_google_drive():
    """
    Handles OAuth 2.0 authentication for Google Drive API.
    Reads credentials.json, authorizes the user, and saves a token.json 
    for future runs so you don't have to log in every time.
    """
    creds = None
    
    # The file token.json stores the user's access and refresh tokens.
    # It is created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        try:
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        except Exception as e:
            print(f"Error reading token.json: {e}")

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                # Refresh the token if it has expired
                creds.refresh(Request())
            except Exception as e:
                print(f"Error refreshing token: {e}")
                creds = None
                
        if not creds:
            # Check if credentials.json exists before attempting to authenticate
            if not os.path.exists('credentials.json'):
                raise FileNotFoundError(
                    "The 'credentials.json' file is missing. Please download it "
                    "from Google Cloud Console and place it in the same directory."
                )
            
            # Start the OAuth 2.0 local web server flow
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            
        # Save the credentials for the next run
        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())

    # Build and return the Drive API v3 service
    return build('drive', 'v3', credentials=creds)


def select_file():
    """
    Opens a Windows file explorer dialog using tkinter to let the user select a file.
    Returns the absolute path of the selected file.
    """
    # Initialize the tkinter root window
    root = tk.Tk()
    # Hide the main root window because we only want to see the file dialog
    root.withdraw()
    root.attributes('-topmost', True)
    root.update()
    
    # Open the file selection dialog
    file_path = filedialog.askopenfilename(
        title="Select a file to upload to Google Drive"
    )
    
    # Destroy the root window after selection to release resources
    root.destroy()
    
    return file_path


def upload_file_to_drive(service, file_path, folder_id):
    """
    Uploads a specified file to a specific Google Drive folder.
    """
    try:
        # Extract the filename from the full file path
        file_name = os.path.basename(file_path)
        
        # Define the metadata for the file (name and target folder)
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }
        
        # Define the media file upload (automatically guesses the mimetype)
        # resumable=True allows uploading larger files reliably
        media = MediaFileUpload(file_path, resumable=True)
        
        print(f"Uploading '{file_name}' to Google Drive...")
        
        # Execute the upload request via the Drive API
        uploaded_file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        file_id = uploaded_file.get('id')
        print(f"Successfully uploaded! File ID: {file_id}")
        return True


    except HttpError as error:
        # Handle errors specifically related to the Google Drive API
        print(f"An API error occurred: {error}")
        return False
    except Exception as e:
        # Handle any other general file or upload errors
        print(f"An unexpected error occurred during upload: {e}")
        return False


# ==========================================
# MAIN EXECUTION
# ==========================================

def main():
    print("Starting Google Drive Upload Script...")

    folder_id = os.getenv("FOLDER_ID")
    if not folder_id:
        raise ValueError("FOLDER_ID is not set in the .env file.")
    
    # Step 1: Authenticate and create the Drive service
    try:
        service = authenticate_google_drive()
        print("Authentication successful.")
    except Exception as e:
        # If authentication fails, display an error and stop execution
        tk.Tk().withdraw() # Hide root window for the error box
        messagebox.showerror("Authentication Error", f"Failed to authenticate with Google:\n{e}")
        return

    # Step 2: Open file dialog and get the chosen file path
    file_path = select_file()
    
    # Check if the user cancelled the file selection dialog (returns an empty string)
    if not file_path:
        print("No file was selected. Upload cancelled.")
        return
        
    # Check if the chosen file actually exists on the system
    if not os.path.exists(file_path):
        print("Error: The selected file does not exist.")
        return

    # Step 3: Upload the file
    success = upload_file_to_drive(service, file_path, folder_id)
    
    # Step 4: Show success or error message using tkinter messagebox
    # We initialize a hidden root again just for the messagebox
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    root.update()
    
    if success:
        messagebox.showinfo("Success", f"File successfully uploaded to Google Drive!\n\nFile: {os.path.basename(file_path)}")
    else:
        messagebox.showerror("Upload Failed", "An error occurred while uploading the file. Check the console for details.")  
    root.destroy()


# Run the main function if this script is executed directly
if __name__ == '__main__':
    main()