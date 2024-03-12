import requests

# URL của endpoint bạn muốn gửi yêu cầu POST đến
url = 'http://127.0.0.1:8000/login/'

# Dữ liệu bạn muốn gửi trong yêu cầu POST
data = {
    'username': '<img src =q onerror=prompt(8)>',
    'password': 'example_password'
}

# Tạo một yêu cầu POST
request = requests.Request('POST', url, json=data)

# Chuẩn bị yêu cầu
prepared_request = request.prepare()

# Gửi yêu cầu POST
response = requests.post(url, json=data)

# In ra  yêu cầu tương ứng
print("HTTP REQUEST: ")
print("\n----------------------------------------------------")
print("Request URL:", prepared_request.url)
print("Request Method:", prepared_request.method)
print("Request Headers:", prepared_request.headers)
print("Request Body:", prepared_request.body)

# In ra phản hồi
print("HTTP RESPONE: ")
print("\n----------------------------------------------------")
print("Response URL:", response.url)
print("Response Method:", response.request.method)
print("Response Headers:", response.headers)
print("Response Body:", response.text.encode('utf-8'))