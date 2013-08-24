from recordtype import recordtype
import json
from JSONRecordEncoder import JSONRecordEncoder 
from jsonprop import JsonObject, json_field

"""
patch recordtype with json() method
"""
def json_dumps(self):
    """Return a json representation of the object"""
    return json.dumps(self._asdict(), cls=JSONRecordEncoder) 



"""
Incomplete definition for Document
TODO: find rest of fields from docs
"""
class Document(JsonObject):
    documentId = json_field('documentId')
    name = json_field('name')

    def __init__(self, *args, **kwargs):
        self.documentId = kwargs['documentId']
        self.name = kwargs['name']

    def _asdict(self):
        return self._to_json_dict()

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
Template.json = json_dumps


class EnvelopeTemplateDefinition(JsonObject):
    description = json_field("description", None, True), 
    name = json_field("name", None, True), 

    #docusign will fail if null pagecount is sent,
    #field must be omitted completely if null
    pageCount = json_field("pageCount", None, False), 

    password = json_field("password", None, True), 
    shared = json_field("shared", None, True), 

    def __init__(self, *args, **kwargs):
        print 'printing args'
        print kwargs
        self.description = kwargs['description']
        self.name = kwargs["name"]

        #docusign will fail if null pagecount is sent,
        #field must be omitted completely if null
        self.pageCount = kwargs["pageCount"]

        self.password = kwargs["password"]
        self.shared = kwargs["shared"]

    def _asdict(self):
        return self._to_json_dict()

class RadioGroupTab(JsonObject):
    conditionalParentLabel = json_field("conditionalParentLabel", None, True)
    conditionalParentValue = json_field("conditionalParentValue", None, True)
    documentId = json_field("documentId", None, True)
    groupName = json_field("groupName", None, True)
    radios = json_field("radios", None, True)
    recipientId = json_field("recipientId", None, True)
    requireInitialOnSharedChange = json_field("requireInitialOnSharedChange", False, True)
    shared = json_field("shared", False, True)
    templateLocked = json_field("templateLocked", False, True)
    templateRequired = json_field("templateRequired", False, True)

    def _asdict(self):
        return self._to_json_dict()
    
'''
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
'''

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
