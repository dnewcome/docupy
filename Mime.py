class Part:
    sections = []
    newline = "\r\n"
    blankline = "\r\n\r\n"
    
    def __init__(self, boundary):
        self.boundary = boundary

    def write(self):
        #return self.newline.join(self.sections) + self.generateBoundaryEnd()
        return "".join(self.sections) + self.generateBoundaryEnd()

    def addSection(self, headers, body):
        requestBody = self.generateBoundary() + \
        self.generateHeaders(headers) + \
        self.newline + '{1}' + self.blankline

        self.sections.append(requestBody.format(self.boundary, body))

    def generateHeaders(self, headers ):
        retval = ""
        for header in headers:
            retval += header + ": " + self.generateValues(headers[header])
            retval += self.newline
        return retval
            
    def generateValues(self, v):
        if isinstance(v, list):
            return "; ".join(v)
        else:
            return v
            
    def generateBoundary(self):
        return "--" + self.boundary + self.newline

    def generateBoundaryEnd(self):
        return "--" + self.boundary + "--" + self.newline + self.newline

def testMime():
    part = Part()
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
