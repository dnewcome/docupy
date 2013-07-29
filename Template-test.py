import sys, requests, json, unittest

from docuconfig import username, password, integratorKey 
from Docusign import Docusign
from Mime import Mime
import defs
from recordtype import recordtype

docusign = Docusign(username, password, integratorKey)
loginInfo = docusign.login( )

accountId = loginInfo['accountId'];

class JSONRestEncoder(json.JSONEncoder):
    """JSON encoder that can handle RestObjects"""
    def default(self, obj):
        try:
            return obj._asdict()
        except:
            return json.JSONEncoder.default(self, obj)


def createAnchorRadioTab(y):
     return defs.RadioTab (
         anchorString = "Radio-" + str(y),
         anchorXOffset = 0,
         anchorYOffset = 0,
         pageNumber = "1",
         value = "Radio" + str(y),
         xPosition = 0,
         yPosition = 0 
     )

def createEnvelopeTemplateDefinition():
    return defs.EnvelopeTemplateDefinition() 

def createAnchorRadioTabs():
    retval = []
    for x in range(0,1):
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
        )

def createInitialTabs():
    retval = []
    for x in range(0,30):
        retval.append(createInitialTab(x*20))
    return retval

def createAnchorInitialTabs():
    retval = []
    for x in range(0,1):
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
        ) ],
        "initialHereTabs": createAnchorInitialTabs()
    }

#--- display results
print ("accountId = %s" % accountId);


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
    }, cls=JSONRestEncoder)


class TestSendTemplate(unittest.TestCase):

    def test_send_template(self):
        # convert the file into a string and add to the request body
        fileContents = open("radios.txt", "r").read();

        mime = Mime("BOUNDARY")
        mime.addSection(
            { 
                "Content-Type": "application/json",
                "Content-Disposition": "form-data"
            },
            envelopeDef 
        )
        mime.addSection(
            { 
                "Content-Type": "application/txt",
                "Content-Disposition": ['file', 'filename="radios.txt"', 'documentId=1']
            },
            fileContents
        )
        print mime.write()

        envId = docusign.sendTemplate(mime.write()).get('envelopeId')

        #--- display results
        print ("Document sent! EnvelopeId is: %s\n" % envId);
        self.assertTrue(True)

    def test_send_templatePdf(self):
        # convert the file into a string and add to the request body
        fileContents = open("radios.pdf", "r").read();

        mime = Mime("BOUNDARY")
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
                "Content-Transfer-Encoding": "binary",
                "Content-Disposition": ['file', 'filename="radios.pdf"', 'documentId=1']
            },
            fileContents
        )
        print mime.write()

        envId = docusign.sendTemplate(mime.write()).get('envelopeId')

        #--- display results
        print ("Document sent! EnvelopeId is: %s\n" % envId);
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
