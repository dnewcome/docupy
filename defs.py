from recordtype import recordtype
import json

def json(self):
    """Return a json representation of the object"""
    return json.dumps(self.dict(), cls=JSONRestEncoder) 

recordtype.json = json

EnvelopeTemplateDefinition = recordtype("RadioGroupTab",
    [
        ("description", "Investment documents for Danco"), 
        ("name", "Danco")
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

InitialTab = recordtype("InitialTab",
    [
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
)

"""
# implementation using namedtuple
RadioTab = namedtuple("RadioTab",
    "anchorString anchorXOffset anchorYOffset anchorIgnoreIfNotPresent \
    anchorUnits pageNumber selected value xPosition yPosition"
)
"""
