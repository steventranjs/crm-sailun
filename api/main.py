from fastapi import FastAPI
import requests
import os

from espo_api import EspoAPI

app = FastAPI()

CRM_URL = os.getenv("CRM_URL")

@app.post("/submit-lead")
def submit_lead(data: dict):
    client = EspoAPI(CRM_URL, os.getenv("CRM_API_KEY"))
    # data = {
    #     'title': 'Mr',
    #     'salutationName': 'John Tran',
    #     'firstName': 'John',
    #     'middleName': 'string',
    #     'lastName': 'string',
    #     'status': 'New',
    #     'phoneNumber': '+11111-22222-33333',
    #     'emailAddress': 'test@abc.com',
    #     'description': 'Toi muon mua 1000 cai banh xe',
    #     'source': 'xxx.com',
    #     'opportunityAmount': 1000,
    #     'opportunityAmountCurrency': 'USD',
    #     'website': 'some-website-client',
    #     'addressStreet': 'string',
    #     'addressCity': "string",
    #     'addressState': 'string',
    #     'addressCountry': 'string',
    #     'addressPostalCode': 'string',
    # }

    client.request('POST', 'Lead', data)
    return response.json()