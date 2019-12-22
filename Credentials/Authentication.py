from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pandas as pd
import os

SPREADSHEET_ID ='1upfym2fXB8Wwnq2jdsDUmwcu9ruRbhwc8oihYDJKYoY'
RANGE_NAME = "Munkalap1"

autPath=os.path.dirname(__file__)+"/"



def get_google_sheet(spreadsheet_id, range_name):
    """ Retrieve sheet data using OAuth credentials and Google Python API. """
    scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    # Setup the Sheets API
    store = file.Storage(autPath + 'credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(autPath + 'client_secret.json', scopes)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    gsheet = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    return gsheet



