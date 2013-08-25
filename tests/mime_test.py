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

        expected = """--BOUNDARY\r
Content-Type: application/json\r
Content-Disposition: form-data\r
\r
{"some":"json"}\r
\r
--BOUNDARY\r
Content-Type: application/pdf\r
Content-Disposition: file; filename="radios.txt"; documentId=1\r
\r
Radio-0 item1

Radio-1 item1

Radio-2 item2

Radio-3 item2


\r
\r
--BOUNDARY--\r
\r
"""

        self.assertEquals(expected, part.write())

