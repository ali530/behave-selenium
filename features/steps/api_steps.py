import requests
from behave import given, when, then
from dotenv import load_dotenv
import os
import logging

load_dotenv()

# -------------------- Given --------------------

# Valid login scenario
@given('I login with correct credentials')
def step_set_valid_login_payload(context):
    context.payload = {
        "username": os.getenv("Api_Auth_Username1"),
        "password": os.getenv("Api_Auth_Password1")
    }

# Invalid login scenario
@given('I login with wrong credentials')
def step_set_invalid_login_payload(context):
    context.payload = {
        "username": "wrong username",
        "password": "wrong p@ssw0rd"
    }

# Access protected resource scenario
@given('I login and get a valid token')
def step_login_and_store_token(context):
    url = "https://dummyjson.com/auth/login"
    payload = {
        "username": os.getenv("Api_Auth_Username2"),
        "password": os.getenv("Api_Auth_Password2")
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    context.token = response.json()["accessToken"]

# -------------------- When --------------------

# All scenarios
@when('I send POST request to the login endpoint')
def step_send_login_request(context):
    url = "https://dummyjson.com/auth/login"
    context.response = requests.post(url, json=context.payload)

# Access protected resource scenario
@when('I access the protected products endpoint')
def step_access_protected_endpoint(context):
    url = "https://dummyjson.com/auth/products"
    headers = {
        "Authorization": f"Bearer {context.token}"
    }
    context.protected_response = requests.get(url, headers=headers)

# -------------------- Then --------------------

# Valid login & Access protected resource scenario
@then('I should receive a 200 response')
def step_verify_200_response(context):
    if hasattr(context, "response"):
        assert context.response.status_code == 200
        logging.info("Responded with 200 OK")
    elif hasattr(context, "protected_response"):
        assert context.protected_response.status_code == 200
        logging.info("Responded with 200 OK")

# Valid login scenario
@then('I should see a token in the response')
def step_verify_token_in_response(context):
    data = context.response.json()
    assert "accessToken" in data
    logging.info("Acces Token Recived")
    
# Invalid login scenario
@then('I should receive a 400 response')
def step_verify_400_response(context):
    assert context.response.status_code == 400
    logging.info("Responded with 400 Bad Request")

# Access protected resource scenario
@then('I should see a list of products')
def step_verify_products_list(context):
    data = context.protected_response.json()
    assert isinstance(data.get("products"), list)
    logging.info("List Verified Successfully")

