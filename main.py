from instagrapi import Client

from config import INST_USERNAME, INST_PASSWORD
from get_followers import followers_info
from get_profile_info import google_sheet_parse

cl = Client()
cl.login(INST_USERNAME, INST_PASSWORD)


followers_info.get_followers_info(cl, google_sheet_parse.get_table_values_info())


