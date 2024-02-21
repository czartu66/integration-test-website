from apitest.src.util.genericUtil import generate_random_email_and_password_and_username
from apitest.src.util.requestsUtil import RequestsUtil


class CustomerHelper(object):

    def __init__(self):
        self.requests_util = RequestsUtil()

    def create_customer(self, email=None, username=None, **kwargs):

        if not email:
            ep = generate_random_email_and_password_and_username()
            email = ep['email']
        if not username:
            username = 'user1'

        payload = dict()
        payload['email'] = email
        payload['username'] = username
        payload.update(kwargs)

        create_user_json = self.requests_util.post('customers', payload=payload, expected_status_code=201)

        return True
