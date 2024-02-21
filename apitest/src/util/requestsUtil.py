import requests
from apitest.src.configs.hosts_config import API_HOSTS
import os
import json
from requests_oauthlib import OAuth1


class RequestsUtil(object):

    def __init__(self):
        self.status_code = None
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1('ck_3ca01e7ba13158360ce23a47daf790b2f8c2a0ad',
                           'cs_87e4a4f589cc31f656b4848020094db4de968cef')

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {
                'Content-Type': 'application/json'
            }
        url = self.base_url + endpoint
        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        assert self.status_code == int(expected_status_code), (f'Expected status code is {expected_status_code}, '
                                                               f'but got {self.status_code}')
        # import pdb; pdb.set_trace()

        return rs_api.json()

    def get(self):
        pass
