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

    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

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

    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

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

    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def _asdict(self):
        return self._to_json_dict()

class RadioTab(JsonObject):
    anchorString = json_field("anchorString", None, True)
    anchorXOffset = json_field("anchorXOffset", 0, True) 
    anchorYOffset = json_field("anchorYOffset", 0, True)
    anchorIgnoreIfNotPresent = json_field("anchorIgnoreIfNotPresent", None, True)
    anchorUnits = json_field("anchorUnits", None, True)
    pageNumber = json_field("pageNumber", None, True)
    selected = json_field("selected", None, True)
    value = json_field("value", None, True)
    xPosition = json_field("xPosition", 0, True)
    yPosition = json_field("yPosition", 0, True)

    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def _asdict(self):
        return self._to_json_dict()

class InitialTab(JsonObject):
    anchorString = json_field("anchorString", None, True)
    anchorXOffset = json_field("anchorXOffset", 0, True)
    anchorYOffset = json_field("anchorYOffset", 0, True)
    anchorIgnoreIfNotPresent = json_field("anchorIgnoreIfNotPresent", None, True)
    anchorUnits = json_field("anchorUnits", None, True)
    conditionalParentLabel = json_field("conditionalParentLabel", None, True)
    conditionalParentValue = json_field("conditionalParentValue", None, True)
    documentId = json_field("documentId", None, True)
    pageNumber = json_field("pageNumber", None, True)
    recipientId = json_field("recipientId", None, True)
    templateLocked = json_field("templateLocked", None, True)
    templateRequired = json_field("templateRequired", None, True)
    xPosition = json_field("xPosition", 0, True)
    yPosition = json_field("yPosition", 0, True)
    name = json_field("name", None, True)
    optional = json_field("optional", None, True)
    scaleValue = json_field("scaleValue", None, True)
    tabLabel = json_field("tabLabel", None, True)

    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def _asdict(self):
        return self._to_json_dict()

class SignHereTab(JsonObject):
    anchorString = json_field("anchorString", None, True)
    anchorXOffset = json_field("anchorXOffset", 0, True)
    anchorYOffset = json_field("anchorYOffset", 0, True)
    anchorIgnoreIfNotPresent = json_field("anchorIgnoreIfNotPresent", None, True)
    anchorUnits = json_field("anchorUnits", None, True)
    conditionalParentLabel = json_field("conditionalParentLabel", None, True)
    conditionalParentValue = json_field("conditionalParentValue", None, True)
    documentId = json_field("documentId", None, True)
    pageNumber = json_field("pageNumber", None, True)
    recipientId = json_field("recipientId", None, True)
    templateLocked = json_field("templateLocked", None, True)
    templateRequired = json_field("templateRequired", None, True)
    xPosition = json_field("xPosition", 0, True)
    yPosition = json_field("yPosition", 0, True)
    name = json_field("name", None, True)
    optional = json_field("optional", None, True)
    scaleValue = json_field("scaleValue", None, True)
    tabLabel = json_field("tabLabel", None, True)

    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def _asdict(self):
        return self._to_json_dict()


"""
# implementation using namedtuple
RadioTab = namedtuple("RadioTab",
    "anchorString anchorXOffset anchorYOffset anchorIgnoreIfNotPresent \
    anchorUnits pageNumber selected value xPosition yPosition"
)
"""
