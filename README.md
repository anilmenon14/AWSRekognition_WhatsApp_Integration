# AWSRekognition_WhatsApp_Integration
Serverless project to send and receive media files for image recognition by AWS Rekognition

## Workflow overview:

1. User initiates a message ‘E.g ‘Hello’ or ‘Hi’ or anything.
2. Serverless call to lambda function that checks in a database if this is the first interaction or if an existing conversation is open (Existing conversation = One active in past 1 hour).
2.  a) If user is new or returning, the service asks back ‘ Hi, do you want to do 1…… , 2……. Or 3……’ with each one being a service offering
    b) If active user, will continue conversation in previous context
3. Based on valid option provided, response is provided back asking for image or URL .
4. If image meets the required spec (i.e. extension or valid URL) , provide response back mentioning that image analysis is being processed.
5. Once complete, a WhatsApp message is sent back in with the response based on the request.
6. The existing connection is closed and next message from user will initiate from step 1.
