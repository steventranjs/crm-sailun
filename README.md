# CRM Sailun

CRM quản lý khách hàng tiềm năng

## Quản Lý CRM
Login vào https://crm-beta.potensus.io/

## Tạo leads bằng CURL

1. Mở shell terminal trên macbook và execute lệnh:
```
curl -X POST 'http://api-beta.potensus.io/submit-lead' \
  -H 'Content-Type: application/json' \
  -d '{ "title": "Giam Doc", "salutationName": "Mr.", "firstName": "Tuan", "middleName": "Le", "lastName": "Tran", "status": "New", "phoneNumber": "+849067888", "emailAddress": "tedst@abc.com", "description": "Toi muon mua 1000 cai banh xe", "source": "Web Site", "opportunityAmount": 1000, "opportunityAmountCurrency": "USD", "website": "vinhome.vn", "addressStreet": "Nguyen Huu Canh", "addressCity": "Ho Chi Minh", "addressState": "Ho Chi Minh", "addressCountry": "Vietnam", "addressPostalCode": "123" }'
```

2. Vào lại CRM, verify lead được tạo ở đây: https://crm-beta.potensus.io/#Lead

3. Nếu execute curl 2 lần sẽ bị lỗi `duplicate (409)`. 

  - Vào lại [trang leads](https://crm-beta.potensus.io/#Lead)
  - Select lead mới tạo, click `Action` > `Remove` để delete lead. 
  - Sau đó sẽ execute tạo lead lại OK, ko bị lỗi duplicate nữa