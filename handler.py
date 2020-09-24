import os
from pathlib import Path
import shutil
import requests

from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
#from googletrans import Translator
import boto3

rekogClient = boto3.client('rekognition')



def httpWebHooktoTwilioURL(event, context):
    print(event) #To have event come up in cloudwatchLogs
    numMedia = int(event['body']['NumMedia'])
    if (numMedia == 1):
        if (event['body']['MediaContentType0']=='image/jpeg'):
            image_url = event['body']['MediaUrl0']
            filename = os.path.join(os.getcwd(),Path("../../tmp/{}.jpg".format(event['body']['MessageSid'])))
            retrieveContent = requests.get(image_url, stream = True)
            if retrieveContent.status_code == 200:
                retrieveContent.raw.decode_content = True #Required to ensure file size is not zero
                with open(filename,'wb') as f: #writing into file
                    shutil.copyfileobj(retrieveContent.raw, f)

            with open(filename,'rb') as image:
                response = rekogClient.recognize_celebrities(Image={'Bytes': image.read()})
            print(response)
            bodyContent = "{} celebrities found".format(len(response['CelebrityFaces']))
        else:
            bodyContent = "Image type is not JPEG or PNG. Please send only one of these."
    elif (numMedia > 1) :
        bodyContent = "Please only send one image at a time "
    elif (numMedia == 0) :
        bodyContent = "Hi, please attach a JPEG or PNG image for facial recognition of celebrities."
    try:
        #translator = Translator()
        response = MessagingResponse()
        message = Message()
        #message.body(translator.translate(event['body']['Body'],dest='hi').text) # Pre-tested on googletrans
        message.body(bodyContent)
        response.append(message)
        return response.to_xml()
    except:
        return "An Error has occured. Please contact support."
