"""Gets a video from the internet and uploads it"""

import urllib.request

import upload

FILENAME = "upload.mp4"

myList = ["cookies6.txt"]

if __name__ == "__main__":

    # upload video to TikTok
    for cookieFile in myList:
        upload.upload_video(FILENAME,
                    description="This is a video I just downloaded", username="justinabond13", password="justinabond@5")
