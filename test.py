# DocuSign API Walkthrough 04 (PYTHON) - Add Signature Request to Document and Send
import sys, httplib2, json
import Docusign

# Enter your info:
username = "dnewcome@circleup.com";
password = "9a2UpOoBtZC";
integratorKey = "CIRC-701b9303-d868-488b-9db0-d561dd5eb9c0";

data = Docusign.login( username, password, integratorKey )

loginInfo = data.get('loginAccounts');
D = loginInfo[0];
baseUrl = D['baseUrl'];
accountId = D['accountId'];

def createRadioTab(y):
     return {
         "anchorString": None,
         "anchorXOffset": None,
         "anchorYOffset": None,
         "anchorIgnoreIfNotPresent": None,
         "anchorUnits": None,
         "pageNumber": "1",
         "selected": None,
         "value": "Radio" + str(y),
         "xPosition": "204",
         "yPosition": str(y)
     }

def createAnchorRadioTab(y):
     return {
         "anchorString": "Radio-" + str(y),
         "anchorXOffset": 0,
         "anchorYOffset": 0,
         "anchorIgnoreIfNotPresent": None,
         "anchorUnits": None,
         "pageNumber": "1",
         "selected": None,
         "value": "Radio" + str(y),
         "xPosition": 0,
         "yPosition": 0 
     }

def createEnvelopeTemplateDefinition():
    return {
        "description": "Investment documents for Danco", 
        "name": "Danco"
    }


def createRadioTabs():
    retval = []
    for x in range(0,30):
        retval.append(createRadioTab(x*20))
    return retval

def createAnchorRadioTabs():
    retval = []
    for x in range(0,4):
        retval.append(createAnchorRadioTab(x))
    return retval

def createInitialTab(y):
    return {
          "anchorString": None,
          "anchorXOffset": None,
          "anchorYOffset": None,
          "anchorIgnoreIfNotPresent": None,
          "anchorUnits": None,
          "conditionalParentLabel": "Radio Group 1",
          "conditionalParentValue": "Radio" + str(y),
          "documentId": "1",
          "pageNumber": "1",
          "recipientId": "1",
          "templateLocked": False ,
          "templateRequired": False,
          "xPosition": "249",
          "yPosition": str(y),
          "name": "Initial Here",
          "optional": False,
          "scaleValue": 1,
          "tabLabel": "Initial 5"
        }

def createAnchorInitialTab(y):
    return {
          "anchorString": "Radio-" + str(y),
          "anchorXOffset": 30,
          "anchorYOffset": 25,
          "anchorIgnoreIfNotPresent": None,
          "anchorUnits": None,
          "conditionalParentLabel": "Radio Group 1",
          "conditionalParentValue": "Radio" + str(y),
          "documentId": "1",
          "pageNumber": "1",
          "recipientId": "1",
          "templateLocked": False ,
          "templateRequired": False,
          "xPosition": 0,
          "yPosition": 0,
          "name": "Initial Here",
          "optional": False,
          "scaleValue": 1,
          "tabLabel": "Initial 5"
        }

def createInitialTabs():
    retval = []
    for x in range(0,30):
        retval.append(createInitialTab(x*20))
    return retval

def createAnchorInitialTabs():
    retval = []
    for x in range(0,4):
        retval.append(createAnchorInitialTab(x))
    return retval


def getTabs():
    return {
        "radioGroupTabs": [{
        "conditionalParentLabel": None,
        "conditionalParentValue": None,
        "documentId": "1",
        "groupName": "Radio Group 1",
        #"radios": createRadioTabs(),
        "radios": createAnchorRadioTabs(),
        "recipientId": "1",
        "requireInitialOnSharedChange": False,
        "shared": False,
        "templateLocked": False,
        "templateRequired": False
        }],
        #"initialHereTabs": createInitialTabs()
        "initialHereTabs": createAnchorInitialTabs()
    }

#--- display results
print ("baseUrl = %s\naccountId = %s" % (baseUrl, accountId));


#construct the body of the request in JSON format
envelopeDef = json.dumps(
    {
        "envelopeTemplateDefinition": createEnvelopeTemplateDefinition(),
        "emailBlurb":"This comes from Python",
        "emailSubject":"API Call for adding signature request to document and sending",
        "documents":[{
            "documentId":"1",
            "name":"test.txt"
        }],
        "recipients":{
            "signers":[{
                "email": username,
                "name":"Name",
                "recipientId":"1",
                "tabs": getTabs(),
                "signHereTabs":[{
                    "xPosition":"100",
                    "yPosition":"100",
                    "documentId":"1",
                    "pageNumber":"1"
                }]
            }]
        },
        "status":"sent"
    })


print envelopeDef


# convert the file into a string and add to the request body
fileContents = open("radios.txt", "r").read();

requestBody = "\r\n\r\n--BOUNDARY\r\n" + \
"Content-Type: application/json\r\n" + \
"Content-Disposition: form-data\r\n" + \
"\r\n" + \
envelopeDef + "\r\n\r\n--BOUNDARY\r\n" + \
"Content-Type: text/plain\r\n" + \
"Content-Disposition: file; filename=\"radios.txt\"; documentId=1\r\n" + \
"\r\n" + \
fileContents + "\r\n" + \
"--BOUNDARY--\r\n\r\n";


# envId = Docusign.sendEnvelope( baseUrl, requestBody, username, password, integratorKey ).get('envelopeId')
envId = Docusign.sendTemplate( baseUrl, requestBody, username, password, integratorKey ).get('envelopeId')

#--- display results
print ("Document sent! EnvelopeId is: %s\n" % envId);
