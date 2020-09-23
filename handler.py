import os

from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
#from googletrans import Translator
import boto3

#session = boto3.Session(profile_name=os.environ.get('AWS_PROFILE_NAME'))



def httpWebHooktoTwilioURL(event, context):
    print(event) #To have event come up in cloudwatchLogs
    if int(event['body']['NumMedia'])> 0:
        bodyContent = event['body']['MediaUrl0']
    else:
        bodyContent = event['body']['Body']
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

#        "headers": {
#            'Content-Type' : 'text/xml'
#        },

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
