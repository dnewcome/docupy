import requests, json, sys
from src.Mime import Mime


# TRACE = False 
TRACE = True 

def trace(msg):
    if TRACE:
        print msg

class Docusign:


    def __init__(self, username, password, integratorKey):
        self.authString = self._authString( username, password, integratorKey )
        self.headers = {'X-DocuSign-Authentication': self.authString, 'Content-Type': 'multipart/form-data; boundary=BOUNDARY', 'Accept': 'application/json'};

    def _authString(self, username, password, integratorKey ):
        return json.dumps({
        'Username': username,
        'Password': password,
        'IntegratorKey': integratorKey
    })

    def login(self):

        # API entry point is a well-known url
        url = 'https://demo.docusign.net/restapi/v2/login_information'

        headers = {
            'X-DocuSign-Authentication': self.authString,
            'Accept': 'application/json'
        }

        response = requests.get(url, headers=headers)

        if (response.status_code != 200):
            print("Error logging in, status is: %s" % response.status_code); sys.exit()

        # get the baseUrl and accountId from the response body
        loginInfo = response.json().get('loginAccounts')[0]
        self.baseUrl = loginInfo['baseUrl']
        trace("accountId = %s" % loginInfo['accountId'])
        return loginInfo

    def buildMime(self, file_name, file_data, content_type, envelope_def, document_id):
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

    def sendEnvelope(self, requestBody ):
        url = self.baseUrl + "/envelopes";
        headers = {
            'X-DocuSign-Authentication': self.authString, 
            'Content-Type': 'multipart/form-data; boundary=BOUNDARY', 'Accept': 'application/json'
        };
        response = requests.post(url, data=requestBody, headers=headers)

        if (response.status_code != 201):
            print("Error sending envelope, status is: %s\nError description - %s" % (response.status_code, response)); sys.exit();
        return response.json();

    def sendTemplate(self, file_name, file_data, content_type, envelope_def, document_id):
        url = self.baseUrl + "/templates";
        request_body = self.buildMime(file_name, file_data, content_type, envelope_def, document_id)
        response = requests.post(url, data = request_body, headers = self.headers)

        if (response.status_code != 201):
            print("Error sending template, status is: %s\nError description - %s" % (response.status_code, response)); sys.exit();
        return response.json();

