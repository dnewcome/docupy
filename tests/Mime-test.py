import Mime, unittest

class TestMime(unittest.TestCase):

    def test_mime(self):
        part = Mime.Part("BOUNDARY")
        fileContents = open("radios.txt", "r").read();
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

if __name__ == '__main__':
    unittest.main()