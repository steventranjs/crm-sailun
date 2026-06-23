# CRM Sailun

- Generate a new lead
```
curl -X POST 'http://localhost:8000/submit-lead' \
  -H 'Content-Type: application/json' \
  -d '{ "title": "Giam Doc", "salutationName": "Mr.", "firstName": "Tuan", "middleName": "Le", "lastName": "Tran", "status": "New", "phoneNumber": "+849067888", "emailAddress": "tedst@abc.com", "description": "Toi muon mua 1000 cai banh xe", "source": "Web Site", "opportunityAmount": 1000, "opportunityAmountCurrency": "USD", "website": "vinhome.vn", "addressStreet": "Nguyen Huu Canh", "addressCity": "Ho Chi Minh", "addressState": "Ho Chi Minh", "addressCountry": "Vietnam", "addressPostalCode": "123" }'
```