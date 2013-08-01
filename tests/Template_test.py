import sys, requests, json, unittest

from config import username, password, integratorKey 
from src.Docusign import Docusign
from src.Mime import Mime
from src import defs
from recordtype import recordtype

# TRACE = False 
TRACE = True 

docusign = Docusign(username, password, integratorKey)
loginInfo = docusign.login( )


"""
TODO: move encoder
"""
class JSONRestEncoder(json.JSONEncoder):
    """JSON encoder that can handle RestObjects"""
    def default(self, obj):
        try:
            return obj._asdict()
        except:
            return json.JSONEncoder.default(self, obj)

def trace(msg):
    if TRACE:
        print msg

def createAnchorRadioTab(y):
     return defs.RadioTab (
         anchorString = "Radio-" + str(y),
         pageNumber = "1",
         value = "Radio" + str(y)
     )

def createEnvelopeTemplateDefinition():
    return defs.EnvelopeTemplateDefinition() 

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
          name = 'Initial Here',
          optional = False,
          scaleValue = 0.5,
          tabLabel = 'Initial 5'
        )

def getTabs():
    return {
        "radioGroupTabs": [ defs.RadioGroupTab(
            documentId = "1",
            groupName = "Radio Group 1",
            radios = [ createAnchorRadioTab(0) ],
            recipientId = "1",
            requireInitialOnSharedChange = False,
            shared = False,
            templateLocked = False,
            templateRequired = False
        ) ],
        "initialHereTabs": [ createAnchorInitialTab(0) ]
    }

#construct the body of the request in JSON format
envelopeDef = json.dumps( defs.Template(
    envelopeTemplateDefinition = createEnvelopeTemplateDefinition(),
    emailBlurb = "This comes from Python",
    emailSubject = "API Call for adding signature request to document and sending",
    documents = [ defs.Document( 
        documentId = 1, 
        name = "test.txt" )
    ],
    recipients = {
        "signers": [ defs.Signer(
            email = username, 
            name = "name", 
            recipientId = 1, 
            tabs = getTabs()
        ) ]
    }
    #status = "sent"
), cls=JSONRestEncoder )

class TestSendTemplate(unittest.TestCase):

    def test_send_template(self):
        self.send_template("tests/radios.txt", "plain/txt")
        self.send_template("tests/radios.pdf", "application/pdf")
    
    def send_template(self, filename, content_type):
        # convert the file into a string and add to the request body
        fileContents = open(filename, "r").read();

        mime = Mime()
        mime.addSection(
            { 
                "Content-Type": "application/json",
                "Content-Disposition": "form-data"
            },
            envelopeDef 
        )
        mime.addSection(
            { 
                "Content-Type": content_type,
                "Content-Disposition": ['file', 'filename="' + filename + '"', 'documentId=1']
            },
            fileContents
        )
        trace(mime.write())

        envId = docusign.sendTemplate(mime.write()).get('envelopeId')

        #--- display results
        trace("Document sent! EnvelopeId is: %s\n" % envId);
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()