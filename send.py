import requests
import os

url = "http://192.168.29.8:5000/index/"
file_path = "photos/plant1.jpg"
dabsp=os.path.abspath(file_path)
print(dabsp)
data = {
    "plantname": "tulasi",  
    "humidity": 65,
    "temperature": 45,
    "moisture": 70
}

with open(file_path, "rb") as file:
    files = {"image": file}
    response = requests.post(url, data=data, files=files)

print("Status Code:", response.status_code)
try:
    print("Response JSON:", response.json())
except requests.exceptions.JSONDecodeError:
    print("Response Text:", response.text)