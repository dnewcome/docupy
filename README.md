# About

Docupy is a Docusign client library for Python.

# Usage

    from docupy.Docusign import Docusign
    from docupy.defs import Template, EnvelopeTemplateDefinition, Document

    filedata = open("tests/radios.txt", "r").read();
    template = Template(
        envelopeTemplateDefinition = EnvelopeTemplateDefinition(),
        documents = [ Document( 
            documentId = 1, 
            name = "radios.txt" )
        ]
    )
    response = docusign.sendTemplate("radios.txt", filedata, "plain/txt", template.json(), 1)
    print response.get('envelopeId')

# Design

Using jsonprop for conicse definition of Docusign data types and JSON serialization control. 

# Hacking

Copy config.template.py to config.py and add your docusign credentials.
Run tests with runtests.sh. Docusign data types are defined in defs.py.

# TODO

Add logging
Add rest of fields to some defs 
Add rest of unimplemented Docusign data types
package system is totally non-standard. Need to understand how this is supposed to work
refactor method names to be more pythonic
