from fastapi import FastAPI
import requests
import os

app = FastAPI()
CRM_URL = os.getenv("CRM_URL")

@app.post("/submit-lead")
def submit_lead(data: dict):
    # API nhận từ web, đẩy thẳng vào EspoCRM
    response = requests.post(f"{CRM_URL}/api/v1/Lead", json=data)
    return response.json()

@app.get("/get-leads/{supplier_id}")
def get_leads(supplier_id: str):
    return {"status": "success", "data": "Dữ liệu đã được ẩn contact theo logic của bạn"}