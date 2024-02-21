import requests
from apitest.src.configs.hosts_config import API_HOSTS
import os
import json
from requests_oauthlib import OAuth1


class RequestsUtil(object):

    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1('ck_3ca01e7ba13158360ce23a47daf790b2f8c2a0ad',
                           'cs_87e4a4f589cc31f656b4848020094db4de968cef')

    def post(self, endpoint, payload=None, headers=None):

        if not headers:
            headers = {
                'Content-Type': 'application/json'
            }
        url = self.base_url + endpoint
        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)

        # import pdb; pdb.set_trace()

    def get(self):
        pass
