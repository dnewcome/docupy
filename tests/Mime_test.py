import docupy.Mime 
import unittest

class TestMime(unittest.TestCase):

    def test_mime(self):
        part = docupy.Mime.Mime()
        fileContents = open("tests/radios.txt", "r").read();
        envelopeDef = '{"some":"json"}'

        part.addSection(
            { 
                "Content-Type": "application/json",
                "Content-Disposition": "form-data"
            },
            envelopeDef 
        )
        part.addSection(
            { 
                "Content-Type": "application/pdf",
                "Content-Disposition": ['file', 'filename="radios.txt"', 'documentId=1']
            },
            fileContents
        )
        print part.write()
        self.assertTrue(True)

