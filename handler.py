import json

from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from xml.etree import ElementTree



def httpWebHooktoTwilioURL(event, context):

    response = MessagingResponse()
    message = Message()
    message.body('Hi Ani ! Ani Ani Ani')
    response.append(message)

    return response.to_xml()

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
