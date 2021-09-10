# YouTube Video Uploader
### Quick and conveinent youtube uploads for local mp4 files
<img src="https://i.gyazo.com/675df75e52dbf9490c1421981b2ce6e6.png" width="690">

![](https://i.gyazo.com/fcf3622ecb83797a0452c2ec45a96ec1.png)

## How it works
Python program connects to YouTube API via pickle file which must be enabled through a GCP project. OAuth 2.0 Client must also be created through GCP for successful authorization of API scopes. Including mp4 file and video details as JSON data following YouTube API documentation allows private uploads. Currently fixing error with pickle file.

## Public uploads
GCP projects after July 28, 2020 now require owners to submit an [audit request](https://support.google.com/youtube/contact/yt_api_form?hl=en) to allow public uploads.

## Scopes
`https://www.googleapis.com/auth/youtube.upload`  
`https://www.googleapis.com/auth/youtube`  
`https://www.googleapis.com/auth/youtubepartner`  
`https://www.googleapis.com/auth/youtube.force-ssl`

## Documentation
[YouTube API](https://developers.google.com/youtube/v3/docs/videos/insert)
