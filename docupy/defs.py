from recordtype import recordtype
import json
from JSONRecordEncoder import JSONRecordEncoder 
from jsonprop import JsonObject, json_field


"""
Incomplete definition for Document
TODO: find rest of fields from docs
"""
class Document(JsonObject):
    documentId = json_field('documentId')
    name = json_field('name')

"""
Incomplete definition for Signer 
TODO: find rest of fields from docs
"""
class Signer(JsonObject):
    email = json_field("email", None, False)
    name = json_field("name", None, False)
    recipientId = json_field("recipientId", None, False)
    tabs = json_field("tabs", None, False)

class Template(JsonObject): 
    accessiblity = json_field("accessiblity", None, False)
    allowMarkup = json_field("allowMarkup", None, False)
    allowReassign = json_field("allowReassign", None, False)
    allowRecipientRecursion = json_field("allowRecipientRecursion", None, False)
    asynchronous = json_field("asynchronous", None, False)
    authoritativeCopy = json_field("authoritativeCopy", None, False)
    autoNavigation = json_field("autoNavigation", None, False)
    brandId = json_field("brandId", None, False)
    emailBlurb = json_field("emailBlurb", None, False)
    emailSubject = json_field("emailSubject", None, False)
    enableWetSign = json_field("enableWetSign", None, False)
    enforceSignerVisibility = json_field("enforceSignerVisibility", None, False)
    envelopeIdStamp = json_field("envelopeIdStamp", None, False)
    eventNotification = json_field("eventNotification", None, False)
    messageLock = json_field("messageLock", None, False)
    signingLocation = json_field("signingLocation", None, False)
    customFields = json_field("customFields", None, False)
    templateId = json_field("templateId", None, False)
    documents = json_field("documents", None, False)
    recipients = json_field("recipients", None, False)
    envelopeTemplateDefinition = json_field("envelopeTemplateDefinition", None, False)

class EnvelopeTemplateDefinition(JsonObject):
    description = json_field("description", None, False)
    name = json_field("name", None, False)

    #docusign will fail if null pagecount is sent,
    #field must be omitted completely if null
    pageCount = json_field("pageCount", None, False), 

    password = json_field("password", None, False), 
    shared = json_field("shared", None, False), 

class RadioGroupTab(JsonObject):
    conditionalParentLabel = json_field("conditionalParentLabel", None, False)
    conditionalParentValue = json_field("conditionalParentValue", None, False)
    documentId = json_field("documentId", None, False)
    groupName = json_field("groupName", None, False)
    radios = json_field("radios", None, False)
    recipientId = json_field("recipientId", None, False)
    requireInitialOnSharedChange = json_field("requireInitialOnSharedChange", False, False)
    shared = json_field("shared", False, False)
    templateLocked = json_field("templateLocked", False, False)
    templateRequired = json_field("templateRequired", False, False)

class RadioTab(JsonObject):
    anchorString = json_field("anchorString", None, False)
    anchorXOffset = json_field("anchorXOffset", 0, False) 
    anchorYOffset = json_field("anchorYOffset", 0, False)
    anchorIgnoreIfNotPresent = json_field("anchorIgnoreIfNotPresent", None, False)
    anchorUnits = json_field("anchorUnits", None, False)
    pageNumber = json_field("pageNumber", None, False)
    selected = json_field("selected", None, False)
    value = json_field("value", None, False)
    xPosition = json_field("xPosition", 0, False)
    yPosition = json_field("yPosition", 0, False)

class InitialTab(JsonObject):
    anchorString = json_field("anchorString", None, False)
    anchorXOffset = json_field("anchorXOffset", 0, False)
    anchorYOffset = json_field("anchorYOffset", 0, False)
    anchorIgnoreIfNotPresent = json_field("anchorIgnoreIfNotPresent", None, False)
    anchorUnits = json_field("anchorUnits", None, False)
    conditionalParentLabel = json_field("conditionalParentLabel", None, False)
    conditionalParentValue = json_field("conditionalParentValue", None, False)
    documentId = json_field("documentId", None, False)
    pageNumber = json_field("pageNumber", None, False)
    recipientId = json_field("recipientId", None, False)
    templateLocked = json_field("templateLocked", None, False)
    templateRequired = json_field("templateRequired", None, False)
    xPosition = json_field("xPosition", 0, False)
    yPosition = json_field("yPosition", 0, False)
    name = json_field("name", None, False)
    optional = json_field("optional", None, False)
    scaleValue = json_field("scaleValue", None, False)
    tabLabel = json_field("tabLabel", None, False)

class SignHereTab(JsonObject):
    anchorString = json_field("anchorString", None, False)
    anchorXOffset = json_field("anchorXOffset", 0, False)
    anchorYOffset = json_field("anchorYOffset", 0, False)
    anchorIgnoreIfNotPresent = json_field("anchorIgnoreIfNotPresent", None, False)
    anchorUnits = json_field("anchorUnits", None, False)
    conditionalParentLabel = json_field("conditionalParentLabel", None, False)
    conditionalParentValue = json_field("conditionalParentValue", None, False)
    documentId = json_field("documentId", None, False)
    pageNumber = json_field("pageNumber", None, False)
    recipientId = json_field("recipientId", None, False)
    templateLocked = json_field("templateLocked", None, False)
    templateRequired = json_field("templateRequired", None, False)
    xPosition = json_field("xPosition", 0, False)
    yPosition = json_field("yPosition", 0, False)
    name = json_field("name", None, False)
    optional = json_field("optional", None, False)
    scaleValue = json_field("scaleValue", None, False)
    tabLabel = json_field("tabLabel", None, False)

