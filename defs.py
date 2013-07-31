from recordtype import recordtype
import json

"""
patch recordtype with json() method
"""
def json(self):
    """Return a json representation of the object"""
    return json.dumps(self.dict(), cls=JSONRestEncoder) 

recordtype.json = json


"""
Incomplete definition for Document
TODO: find rest of fields from docs
"""
Document = recordtype("Document",
    [
        #"documentId":"1",
        ("documentId", None),
        ("name", None)
    ]
)

"""
Incomplete definition for Signer 
TODO: find rest of fields from docs
"""
Signer = recordtype("Signer",
    [
        ("email", None),
        ("name", None),
        ("recipientId", None),
        ("tabs", None) 
    ]
)

Template = recordtype('Template', 
    [
        ("accessiblity", None),
        ("allowMarkup", None),
        ("allowReassign", None),
        ("allowRecipientRecursion", None),
        ("asynchronous", None),
        ("authoritativeCopy", None),
        ("autoNavigation", None),
        ("brandId", None),
        ("emailBlurb", None),
        ("emailSubject", None),
        ("enableWetSign", None),
        ("enforceSignerVisibility", None),
        ("envelopeIdStamp", None),
        ("eventNotification", None),
        ("messageLock", None),
        ("signingLocation", None),
        ("customFields", None),
        ("templateId", None),
        ("documents", None),
        ("recipients", None),
        ("envelopeTemplateDefinition", None)
    ]
)

EnvelopeTemplateDefinition = recordtype("EnvelopeTemplateDefinition",
    [
        # these fields are all optional
        ("description", None), 
        ("name", None),

        #docusign will fail if null pagecount is sent,
        #field must be omitted completely if null
        #("pageCount", None)

        ("password", None),
        ("shared", None)
    ]
)

RadioGroupTab = recordtype("RadioGroupTab",
    [
        ("conditionalParentLabel", None),
        ("conditionalParentValue", None),
        ("documentId", None),
        ("groupName", None),
        ("radios", None),
        ("recipientId", None),
        ("requireInitialOnSharedChange", False),
        ("shared", False),
        ("templateLocked", False),
        ("templateRequired", False)
    ]
)

RadioTab = recordtype("RadioTab",
    [
        ("anchorString", None), 
        ("anchorXOffset", 0), 
        ("anchorYOffset", 0), 
        ("anchorIgnoreIfNotPresent", None),
        ("anchorUnits", None),
        ("pageNumber", None),
        ("selected", None),
        ("value", None), 
        ("xPosition", 0), 
        ("yPosition", 0)
    ]
)

signatureFields = [
    ("anchorString", None),
    ("anchorXOffset", 0),
    ("anchorYOffset", 0),
    ("anchorIgnoreIfNotPresent", None),
    ("anchorUnits", None),
    ("conditionalParentLabel", None),
    ("conditionalParentValue", None),
    ("documentId", None),
    ("pageNumber", None),
    ("recipientId", None),
    ("templateLocked", None),
    ("templateRequired", None),
    ("xPosition", 0),
    ("yPosition", 0),
    ("name", None),
    ("optional", None),
    ("scaleValue", None),
    ("tabLabel", None)
]

InitialTab = recordtype("InitialTab", signatureFields)
SignHereTab = recordtype("SignHereTab", signatureFields)

"""
# implementation using namedtuple
RadioTab = namedtuple("RadioTab",
    "anchorString anchorXOffset anchorYOffset anchorIgnoreIfNotPresent \
    anchorUnits pageNumber selected value xPosition yPosition"
)
"""
