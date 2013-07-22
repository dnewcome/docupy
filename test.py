import sys, httplib2, json
import Docusign
import Mime, defs
from docuconfig import username, password, integratorKey 

# different lightweight container classes
from collections import namedtuple
from recordtype import recordtype

loginInfo = Docusign.login( username, password, integratorKey )

baseUrl = loginInfo['baseUrl'];
accountId = loginInfo['accountId'];

def createAnchorRadioTab(y):
     return defs.RadioTab (
         anchorString = "Radio-" + str(y),
         anchorXOffset = 0,
         anchorYOffset = 0,
         pageNumber = "1",
         value = "Radio" + str(y),
         xPosition = 0,
         yPosition = 0 
     )._asdict()

def createEnvelopeTemplateDefinition():
    return defs.EnvelopeTemplateDefinition()._asdict() 

def createAnchorRadioTabs():
    retval = []
    for x in range(0,4):
        retval.append(createAnchorRadioTab(x))
    return retval

def createAnchorInitialTab(y):
    return defs.InitialTab (
          anchorString = 'Radio-' + str(y),
          anchorXOffset = 30,
          anchorYOffset = 25,
          conditionalParentLabel = 'Radio Group 1',
          conditionalParentValue = 'Radio' + str(y),
          documentId = 1,
          pageNumber = 1,
          recipientId = 1,
          templateLocked = False,
          templateRequired = False,
          xPosition = 0,
          yPosition = 0,
          name = 'Initial Here',
          optional = False,
          scaleValue = 1,
          tabLabel = 'Initial 5'
        )._asdict()

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
        "radioGroupTabs": [ defs.RadioGroupTab(
            documentId = "1",
            groupName = "Radio Group 1",
            radios = createAnchorRadioTabs(),
            recipientId = "1",
            requireInitialOnSharedChange = False,
            shared = False,
            templateLocked = False,
            templateRequired = False
        )._asdict() ],
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

#"Content-Type: text/plain\r\n" + \

# convert the file into a string and add to the request body
fileContents = open("radios.txt", "r").read();

mime = Mime.Part("BOUNDARY")
mime.addSection(
    { 
        "Content-Type": "application/json",
        "Content-Disposition": "form-data"
    },
    envelopeDef 
)
mime.addSection(
    { 
        "Content-Type": "application/pdf",
        "Content-Disposition": ['file', 'filename="radios.txt"', 'documentId=1']
    },
    fileContents
)
print mime.write()

#envId = Docusign.sendEnvelope( baseUrl, requestBody, username, password, integratorKey ).get('envelopeId')
envId = Docusign.sendTemplate( baseUrl, mime.write(), username, password, integratorKey ).get('envelopeId')

#--- display results
print ("Document sent! EnvelopeId is: %s\n" % envId);
