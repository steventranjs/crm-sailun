from fastapi import FastAPI
import requests
import os

from espo_api import EspoAPI
import json

app = FastAPI()

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Hoặc liệt kê domain cụ thể: ["https://site-a.com", "https://site-b.com"]
    allow_credentials=True,
    allow_methods=["*"], # Cho phép tất cả phương thức (POST, OPTIONS, GET...)
    allow_headers=["*"], # Cho phép tất cả header
)

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