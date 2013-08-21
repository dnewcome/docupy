import sys, requests, json, unittest
from docupy.JSONRecordEncoder import JSONRecordEncoder

from config import username, password, integratorKey 
from docupy.Docusign import Docusign
from docupy.Mime import Mime
from docupy import defs
from docupy.defs import Template, EnvelopeTemplateDefinition, Document
from recordtype import recordtype

# TRACE = False 
TRACE = True 

docusign = Docusign(username, password, integratorKey)
loginInfo = docusign.login( )

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
    return defs.EnvelopeTemplateDefinition(
        description = None,
        name = None,
        pageCount = None,
        password = None,
        shared = None
    ) 

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

def createEnvelopeDef():
	#construct the body of the request in JSON format
	template = defs.Template(
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
	)

	return template.json()


class TestSendTemplate(unittest.TestCase):

    def test_send_template_txt(self):
        txtfile = open("tests/radios.txt", "r").read();
        self.send_template("tests/radios.txt", txtfile, "plain/txt", None)

    def test_send_template_pdf(self):
        pdffile = open("tests/radios.pdf", "r").read();
        self.send_template("tests/radios.pdf", pdffile, "application/pdf", None)
    
    def send_template(self, filename, filedata, content_type, metadata):
        # convert the file into a string and add to the request body
        fileContents = open(filename, "r").read();

        #file_name, file_data, content_type, envelope_def, document_id):
        document_id = 1
        envId = docusign.sendTemplate(filename, filedata, content_type, createEnvelopeDef(), document_id).get('envelopeId')


        #--- display results
        trace("Document sent! EnvelopeId is: %s\n" % envId);
        self.assertTrue(True)

    def test_send_template_minimal(self):
        filedata = open("tests/radios.txt", "r").read();

        template = Template(
            envelopeTemplateDefinition = createEnvelopeTemplateDefinition(),
            documents = [ defs.Document( 
                documentId = 1, 
                name = "test.txt" )
            ],
        )
        print "running minimal test"
        response = docusign.sendTemplate("radios.txt", filedata, "plain/txt", template.json(), 1)
        print response.get('envelopeId')

