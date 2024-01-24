"""Gets a video from the internet and uploads it"""

import urllib.request

import upload

FILENAME = "upload.mp4"

if __name__ == "__main__":

    # upload video to TikTok
    upload.upload_video(FILENAME,
                 description="This is a video I just downloaded",
                 cookies="cookies.txt")
