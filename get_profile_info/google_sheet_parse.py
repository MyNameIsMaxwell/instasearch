import os
import re

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


# Файл, полученный в Google Developer Console
if __name__ == '__main__':
    CREDENTIALS_FILE = os.path.abspath(os.path.join('creds.json'))
else:
    CREDENTIALS_FILE = os.path.abspath(os.path.join('get_profile_info\creds.json'))
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1ZzvLN-fxpvBr8NWaNnTS64zgZxe2jhdS5ju2_puMA14'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


def get_table_values_info() -> list:
    """
    Функция чтения информации из таблицы и выбирающая имена аккаунтов.
    :return: users_account_names: список с именами инстаграм-аккаунтов из таблицы.
    """
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='Лист1!A2:B9',
        majorDimension='COLUMNS'
    ).execute()
    users_account_number = values['values'][0]
    users_account_links = values['values'][1]
    users_account_names = []
    for user_link in users_account_links:
        user_name = re.findall(r'https://www.instagram.com/(.+)/', user_link)[0]
        users_account_names.append(user_name)

    return users_account_names


def post_table_values_info(ids_info: str) -> None:
    """
    Функция записи информации об id аккаунтов в таблицу.
    :param ids_info: str-запись всех id подписчиков
    """
    values = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": "Лист2!C2:C10",
                 "majorDimension": "COLUMNS",
                 "values": [[ids_info]]}
                ]
        }
    ).execute()
