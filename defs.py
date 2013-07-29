from recordtype import recordtype
import json

def json(self):
    """Return a json representation of the object"""
    return json.dumps(self.dict(), cls=JSONRestEncoder) 

recordtype.json = json

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
