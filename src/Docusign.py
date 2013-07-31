import requests, json, sys

class Docusign:

    def __init__(self, username, password, integratorKey):
        self.authString = self.authString( username, password, integratorKey )

    def authString(self, username, password, integratorKey ):
        return json.dumps({
        'Username': username,
        'Password': password,
        'IntegratorKey': integratorKey
    })

    def login(self):
        authenticateStr = self.authString

        # API entry point is a well-known url
        url = 'https://demo.docusign.net/restapi/v2/login_information'

        headers = {
            'X-DocuSign-Authentication': authenticateStr,
            'Accept': 'application/json'
        }

        response = requests.get(url, headers=headers)

        if (response.status_code != 200):
            print("Error logging in, status is: %s" % response.status_code); sys.exit()

        # get the baseUrl and accountId from the response body
        loginInfo = response.json().get('loginAccounts')[0]
        self.baseUrl = loginInfo['baseUrl']
        return loginInfo

    def sendEnvelope(self, requestBody ):
        authenticateStr = self.authString
        url = self.baseUrl + "/envelopes";
        headers = {
            'X-DocuSign-Authentication': authenticateStr, 
            'Content-Type': 'multipart/form-data; boundary=BOUNDARY', 'Accept': 'application/json'
        };
        response = requests.post(url, data=requestBody, headers=headers)

        if (response.status_code != 201):
            print("Error sending envelope, status is: %s\nError description - %s" % (response.status_code, response)); sys.exit();
        return response.json();

    def sendTemplate(self, requestBody):
        authenticateStr = self.authString
        url = self.baseUrl + "/templates";
        headers = {'X-DocuSign-Authentication': authenticateStr, 'Content-Type': 'multipart/form-data; boundary=BOUNDARY', 'Accept': 'application/json'};
        response = requests.post(url, data=requestBody, headers=headers)

        if (response.status_code != 201):
            print("Error sending template, status is: %s\nError description - %s" % (response.status_code, response)); sys.exit();
        return response.json();

