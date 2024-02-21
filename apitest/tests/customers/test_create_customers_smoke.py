import pytest
import logging as logger
from apitest.src.util.genericUtil import generate_random_email_and_password_and_username
from apitest.src.util.helpers.customer_helper import CustomerHelper


@pytest.mark.tcid29
def test_create_customer_only_email_password():

    logger.info("TEST: Create new customer with email and password.")

    rand_info = generate_random_email_and_password_and_username()
    logger.info(rand_info)
    email = rand_info['email']
    username = rand_info['username']
    # password = rand_info['password']

    # make the call
    customer_obj = CustomerHelper()
    customer_api_info = customer_obj.create_customer(email=email, username=username)

    # verify status code of the call

    # verify email in the response

    # verify customer is created in database
