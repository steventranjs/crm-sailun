from fastapi import FastAPI
import requests
import os

from espo_api import EspoAPI
import json

app = FastAPI()

CRM_URL = os.getenv("CRM_URL")

@app.post("/submit-lead")
def submit_lead(data: dict):
    client = EspoAPI(CRM_URL, os.getenv("CRM_API_KEY"))
    # data = {
    #     'title': 'Giam Doc',
    #     'salutationName': 'Mr.',
    #     'firstName': 'John',
    #     'middleName': 'string',
    #     'lastName': 'string',
    #     'status': 'New',
    #     'phoneNumber': '+11111-22222-33333',
    #     'emailAddress': 'test@abc.com',
    #     'description': 'Toi muon mua 1000 cai banh xe',
    #     'source': 'Web Site',
    #     'opportunityAmount': 1000,
    #     'opportunityAmountCurrency': 'USD',
    #     'website': 'vinhome.vn',
    #     'addressStreet': 'Nguyen Huu Canh',
    #     'addressCity': "Ho Chi Minh",
    #     'addressState': 'Ho Chi Minh',
    #     'addressCountry': 'Vietnam',
    #     'addressPostalCode': '123',
    # }

    response = client.request('POST', 'Lead', data)
    return response