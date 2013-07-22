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
        return json.loads(content).get('loginAccounts')[0]

    def sendEnvelope(self, baseUrl, requestBody ):
        authenticateStr = self.authString
        url = baseUrl + "/envelopes";
        #url = baseUrl + "/templates";
        headers = {'X-DocuSign-Authentication': authenticateStr, 'Content-Type': 'multipart/form-data; boundary=BOUNDARY', 'Accept': 'application/json'};
        http = httplib2.Http();
        response, content = http.request(url, 'POST', headers=headers, body=requestBody);
        status = response.get('status');
        if (status != '201'):
            print("Error calling webservice, status is: %s\nError description - %s" % (status, content)); sys.exit();
        return json.loads(content);

    def sendTemplate(self, baseUrl, requestBody, username, password, integratorKey ):
        authenticateStr = self.authString
        url = baseUrl + "/templates";
        headers = {'X-DocuSign-Authentication': authenticateStr, 'Content-Type': 'multipart/form-data; boundary=BOUNDARY', 'Accept': 'application/json'};
        http = httplib2.Http();
        response, content = http.request(url, 'POST', headers=headers, body=requestBody);
        status = response.get('status');
        if (status != '201'):
            print("Error calling webservice, status is: %s\nError description - %s" % (status, content)); sys.exit();
        return json.loads(content);

