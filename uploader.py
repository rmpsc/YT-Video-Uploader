import datetime
from create import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

upload_date_time = datetime.datetime(2021, 5, 16, 12, 00, 0).isoformat() + '.000Z'

request_body  = {
    'snippet': {
        'categoryId': 20,
        'title': 'Word but Valorant',
        'description': 'word.exe description',
        'tags': ['Valorant', 'Sheesh']
    },
    'status': {
        'privacyStatus': 'private',
        'publishAt': upload_date_time,
        'selfDeclaredMadeForKids': False,
    },
    'notifySubscribers': False
}

mediaFile = MediaFileUpload('wordexe.mp4')

response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
).execute()

service.thumbnails().set(
    videoId=response_upload.get('id'),
    media_body=MediaFileUpload('jett_icon.png')
).execute()
