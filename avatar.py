from urllib import request
import requests
from PIL import Image

#CONFIG
userId="<YOUR ZOOM EMAIL>"
#token expires on ....
jwtToken="<YOUR JWT TOKEN>"

backgroundUrl="https://picsum.photos/200/243/?random" #bg should be same size or bigger than fg
foregroundFile="./foreground200x243.png"
backgroundFile="./.background.jpg"
mergedFile="./.merged.jpg"

def get_image():
    global backgroundUrl
    imgURL=backgroundUrl
    request.urlretrieve(imgURL, "./.background.jpg")

def merge_images():
    background = Image.open(backgroundFile)
    foreground = Image.open(foregroundFile)
    height_diff=background.size[1]-foreground.size[1]
    background.paste(foreground, (0, height_diff), foreground)  # this moves the fg to the bottom of the bg
    background.save(mergedFile, "JPEG", optimize=True, quality=80)
    
def upload_merged():
    token=jwtToken

    url = 'https://api.zoom.us/v2/users/{0}/picture'.format(userId)

    headers = {'Authorization': 'Bearer {}'.format(token),
            'Accept': 'application/json',
            }
    
    files = {'pic_file': open(mergedFile, 'rb')}

    response = requests.post(url, files=files, headers=headers)
    print (response.content)
    
get_image()
merge_images()
upload_merged()