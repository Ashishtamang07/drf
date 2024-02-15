import requests
import json

URL= " http://127.0.0.1:8000/stu/"

data= {
    'name':'tamang',
    'roll': 12,
    'city':'kathmandu'
    
}
#dumps() converts python objects or dict to json
json_data= json.dumps(data)

r=requests.post(url = URL, data=json_data)
data= r.headers.get('Content_Type')
print(data)