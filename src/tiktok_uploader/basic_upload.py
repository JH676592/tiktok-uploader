"""Gets a video from the internet and uploads it"""

import urllib.request

import upload

FILENAME = "upload.mp4"

myList = ["cookies8.txt", "cookies7.txt"]
sessionIDS = ['80a2658c101a4694968fce71a8cdbcd5', '7db6bf898ad8d4edc52a4963713cc41e']

if __name__ == "__main__":

    # upload video to TikTok
    for ID in myList:
        
        upload.upload_video(FILENAME,
                    description="This is a video I just downloaded", cookies="cookies8.txt")
