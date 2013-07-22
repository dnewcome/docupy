from recordtype import recordtype

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
        ("anchorXOffset", None), 
        ("anchorYOffset", None), 
        ("anchorIgnoreIfNotPresent", None),
        ("anchorUnits", None),
        ("pageNumber", None),
        ("selected", None),
        ("value", None), 
        ("xPosition", None), 
        ("yPosition", None)
    ]
)

"""
# implementation using namedtuple
RadioTab = namedtuple("RadioTab",
    "anchorString anchorXOffset anchorYOffset anchorIgnoreIfNotPresent \
    anchorUnits pageNumber selected value xPosition yPosition"
)
"""

InitialTab = recordtype("InitialTab",
    [
        ("anchorString", None),
        ("anchorXOffset", None),
        ("anchorYOffset", None),
        ("anchorIgnoreIfNotPresent", None),
        ("anchorUnits", None),
        ("conditionalParentLabel", None),
        ("conditionalParentValue", None),
        ("documentId", None),
        ("pageNumber", None),
        ("recipientId", None),
        ("templateLocked", None),
        ("templateRequired", None),
        ("xPosition", None),
        ("yPosition", None),
        ("name", None),
        ("optional", None),
        ("scaleValue", None),
        ("tabLabel", None)
    ]
)
