# About

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

Using python recortypes for conicse definition of Docusign data types. 
It's possible that we'll need to just use plain python claseses anyway.

# Hacking

Copy config.template.py to config.py and add your docusign credentials.
Run tests with runtests.sh. Docusign data types are defined in defs.py.

# TODO

replace multiple trace definitions with one

Add rest of fields to existing recordtypes
Add rest of unimplemented Docusign data types

Find out how to handle fields that return errors when provided
with null values.

package system is totally non-standard. Need to understand how this is supposed to work

set up test runner correctly

refactor method names to be more pythonic
