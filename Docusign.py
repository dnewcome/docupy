import httplib2, json

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

        http = httplib2.Http()
        response, content = http.request(url, 'GET', headers=headers)

        status = response.get('status')

        if (status != '200'):
            print("Error calling webservice, status is: %s" % status); sys.exit()

        # get the baseUrl and accountId from the response body
        loginInfo = json.loads(content).get('loginAccounts')[0]
        self.baseUrl = loginInfo['baseUrl']
        return loginInfo

    def sendEnvelope(self, requestBody ):
        authenticateStr = self.authString
        url = self.baseUrl + "/envelopes";
        #url = baseUrl + "/templates";
        headers = {'X-DocuSign-Authentication': authenticateStr, 'Content-Type': 'multipart/form-data; boundary=BOUNDARY', 'Accept': 'application/json'};
        http = httplib2.Http();
        response, content = http.request(url, 'POST', headers=headers, body=requestBody);
        status = response.get('status');
        if (status != '201'):
            print("Error calling webservice, status is: %s\nError description - %s" % (status, content)); sys.exit();
        return json.loads(content);

    def sendTemplate(self, requestBody):
        authenticateStr = self.authString
        url = self.baseUrl + "/templates";
        headers = {'X-DocuSign-Authentication': authenticateStr, 'Content-Type': 'multipart/form-data; boundary=BOUNDARY', 'Accept': 'application/json'};
        http = httplib2.Http();
        response, content = http.request(url, 'POST', headers=headers, body=requestBody);
        status = response.get('status');
        if (status != '201'):
            print("Error calling webservice, status is: %s\nError description - %s" % (status, content)); sys.exit();
        return json.loads(content);

