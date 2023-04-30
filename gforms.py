from __future__ import print_function
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import discovery
from httplib2 import Http

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/forms.body', 'https://www.googleapis.com/auth/forms', 'https://www.googleapis.com/auth/forms.responses.readonly']
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"


def getresp():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = discovery.build('forms', 'v1', credentials=creds)
    form_id = "12yiZIKgdOtHTgkQvu56WqcCyP5gFG137fEohTvrTgY4"
    response = service.forms().get(formId=form_id).execute()
    print(response)

    result = service.forms().responses().list(formId=form_id).execute()
    print(str(result))
    return str(result)


if __name__ == '__main__':
    getresp()
