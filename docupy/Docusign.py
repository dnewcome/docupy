import requests, json, sys
from docupy.Mime import Mime

# TRACE = False 
TRACE = True 

def trace(msg):
    if TRACE:
        print msg

class Docusign:

    def __init__(self, username, password, integratorKey):
        self.authString = self._authString( username, password, integratorKey )
        self.headers = {'X-DocuSign-Authentication': self.authString, 'Content-Type': 'multipart/form-data; boundary=BOUNDARY', 'Accept': 'application/json'};

    def login(self):
        """Docusign API call for authenticating and fetching API endpoints"""

        # API entry point is a well-known url
        url = 'https://demo.docusign.net/restapi/v2/login_information'

        headers = {
            'X-DocuSign-Authentication': self.authString,
            'Accept': 'application/json'
        }

        response = requests.get(url, headers=headers)

        if (response.status_code != 200):
            raise Exception("Error logging in, status is: %s" % response.status_code)

        # get the baseUrl and accountId from the response body
        loginInfo = response.json().get('loginAccounts')[0]
        self.baseUrl = loginInfo['baseUrl']
        trace("accountId = %s" % loginInfo['accountId'])
        return loginInfo


    def sendEnvelope(self, file_name, file_data, content_type, envelope_def, document_id):
        """Docusign API call for sending a signature envelope"""
        return self._makeFileRequest(file_name, file_data, content_type, envelope_def, document_id, self.baseUrl + "/envelopes")

    def sendTemplate(self, file_name, file_data, content_type, envelope_def, document_id):
        """Docusign API call for sending a signature template"""
        return self._makeFileRequest(file_name, file_data, content_type, envelope_def, document_id, self.baseUrl + "/envelopes")
        return self._makeFileRequest(file_name, file_data, content_type, envelope_def, document_id, self.baseUrl + "/templates")

    def _authString(self, username, password, integratorKey ):
        return json.dumps({
        'Username': username,
        'Password': password,
        'IntegratorKey': integratorKey
    })


    def _buildMime(self, file_name, file_data, content_type, envelope_def, document_id):
        mime = Mime()
        mime.addSection(
            { 
                "Content-Type": "application/json",
                "Content-Disposition": "form-data"
            },
            envelope_def 
        )
        mime.addSection(
            { 
                "Content-Type": content_type,
                "Content-Disposition": ['file', 'filename="' + file_name + '"', 'documentId=' + str(document_id)]
            },
            file_data
        )
        trace(mime.write())
        return mime.write()

    def _makeFileRequest(self, file_name, file_data, content_type, envelope_def, document_id, url):
        """internal method servicing api calls that send a file as multipart mime"""
        request_body = self._buildMime(file_name, file_data, content_type, envelope_def, document_id)
        response = requests.post(url, data = request_body, headers = self.headers)

        if (response.status_code != 201):
            raise Exception("Error sending file, status is: %s\nError description - %s" % (response.status_code, response))

        return response.json();
