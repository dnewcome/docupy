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


def createRadioTabs():
    retval = []
    for x in range(0,30):
        retval.append(createRadioTab(x*20))
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

def createInitialTabs():
    retval = []
    for x in range(0,30):
        retval.append(createInitialTab(x*20))
    return retval

#--- display results
print ("baseUrl = %s\naccountId = %s" % (baseUrl, accountId));

def getTabsJson ():
    return {
        "radioGroupTabs": [{
        "conditionalParentLabel": None,
        "conditionalParentValue": None,
        "documentId": "1",
        "groupName": "Radio Group 1",
        "radios": createRadioTabs(),
        "recipientId": "1",
        "requireInitialOnSharedChange": False,
        "shared": False,
        "templateLocked": False,
        "templateRequired": False
        }],
        "initialHereTabs": createInitialTabs()
    }

#construct the body of the request in JSON format
envelopeDef = json.dumps(
    {
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
                "tabs": getTabsJson(),
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
fileContents = open("test.txt", "r").read();

requestBody = "\r\n\r\n--BOUNDARY\r\n" + \
"Content-Type: application/json\r\n" + \
"Content-Disposition: form-data\r\n" + \
"\r\n" + \
envelopeDef + "\r\n\r\n--BOUNDARY\r\n" + \
"Content-Type: text/plain\r\n" + \
"Content-Disposition: file; filename=\"test.txt\"; documentId=1\r\n" + \
"\r\n" + \
fileContents + "\r\n" + \
"--BOUNDARY--\r\n\r\n";


envId = Docusign.sendEnvelope( baseUrl, requestBody, username, password, integratorKey ).get('envelopeId')

#--- display results
print ("Document sent! EnvelopeId is: %s\n" % envId);
