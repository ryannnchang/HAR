from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

sheet_id = '1mxNVes5B-avw1c1A7nt9lWmTEBqib9RJTMMRL-icS2A'
scopes = ['https://www.googleapis.com/auth/spreadsheets']
creds = Credentials.from_service_account_file('GoogleSheets/creds.json', scopes=scopes)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

def update_values(range_name, value_input_option, values):
  """
  Creates the batch_update the user has access to.
  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  # pylint: disable=maybe-no-member
  spreadsheet_id = sheet_id
  
  try:
    body = {"values": values}
    result = (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption=value_input_option,
            body=body,
        )
        .execute()
    )
    return result
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error

def get_values(range_name):
  """
  Creates the batch_update the user has access to.
  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  # pylint: disable=maybe-no-member
  spreadsheet_id = sheet_id
  try:
    result = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range=range_name)
        .execute()
    )
    rows = result.get("values", [])
    return rows
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error

def clear_values():
  range_name = 'A3:F1000'
  spreadsheet_id = sheet_id

  """
  Clears the values in the specified range.
  """
  try:
    service = build("sheets", "v4", credentials=creds)
    result = (
        service.spreadsheets()
        .values()
        .clear(spreadsheetId=spreadsheet_id, range=range_name)
        .execute()
    )
    print(f"Cleared values in range: {range_name}")
    return result
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error


