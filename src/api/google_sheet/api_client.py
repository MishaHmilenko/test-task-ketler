import os

from dotenv import load_dotenv

from src.interafaces.external_api_interfaces.api_client import InterfaceAPIClient

load_dotenv()


class GoogleSheetTableAPIClient(InterfaceAPIClient):

    def __init__(self):
        self.spreadsheet_id = os.getenv('SPREADSHEET_ID')

    def get_headers(self) -> dict:
        return {
            'Authorization': f'Bearer {os.getenv("AUTHORIZATION_GOOGLE_API_TOKEN")}',
            'Content-Type': 'application/json'
        }

    def get_url(self, **kwargs) -> str:
        range_name = kwargs.get('range_name')

        if range_name is None:
            raise ValueError('Parameter \'range_name\' must be provided.')

        return f'https://sheets.googleapis.com/v4/spreadsheets/{self.spreadsheet_id}/values/{range_name}'

    def get_body(self, **kwargs) -> dict:
        range_name = kwargs.get('range_name')

        if range_name is None:
            raise ValueError('Parameter \'range_name\' must be provided.')

        values = kwargs.get('values')

        if values is None:
            raise ValueError('Parameter \'values\' must be provided.')

        return {
            'range': range_name,
            'majorDimension': 'ROWS',
            'values': [[values]] if type(values) is not list else [values]
        }