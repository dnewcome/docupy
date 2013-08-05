class Mime:
    sections = []
    newline = "\r\n"
    #blankline = "\r\n\r\n"
    blankline = newline + newline 
    boundary = "BOUNDARY"
    
    def __init__(self):
        pass

    def write(self):
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

