import datetime
from google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

request_body  = {
    'snippet': {
        'categoryI': 20,
        'title': 'Upload Testing',
        'description': 'word.exe description',
        'tags': ['Valorant', 'Sheesh']
    },
}
