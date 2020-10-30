import requests

url = "https://canvas.instructure.com:443/api/v1/courses?enrollment_state=active"

payload = {}
headers = {
  'Authorization': 'Bearer 13605~09L4zAm6VDfDts6IuWtNmrpfrFZDbq4OJhGRN6zlMH9qHI1bboDue3NEeIOBcBV9',
  'Cookie': '_csrf_token=uf6B5cBINHGax3rj2IeCMs%2BUJbw88Q9nrBjhVYG06TD8rdakoQ9wOKqhUaKwsOBGqfNx5kuJOArhdbAx%2BIWgew%3D%3D; log_session_id=d6904a33a415691644320e0d9cfa4388; _legacy_normandy_session=vBLrgRZmuED54AaC5MiMhQ.nC0QgMfRNT13HkfiCVV_Nsox5ZjGea340nfyFynKwZAbL8-I8pLqk5FhCFtfqNzRMustu8XlKVN0C1oKK0BfrMzylqHp3dV56mCZWqyZv4DmV2Tvcfk_fluCuOJISiV-.jbCruUFKRhicDMEoz8s9LY5QXOc.X5oXEQ; canvas_session=vBLrgRZmuED54AaC5MiMhQ.nC0QgMfRNT13HkfiCVV_Nsox5ZjGea340nfyFynKwZAbL8-I8pLqk5FhCFtfqNzRMustu8XlKVN0C1oKK0BfrMzylqHp3dV56mCZWqyZv4DmV2Tvcfk_fluCuOJISiV-.jbCruUFKRhicDMEoz8s9LY5QXOc.X5oXEQ'
}

response = requests.request("GET", url, headers=headers, data = payload)

jsonResponse = response.json()
print(type(jsonResponse))
for item in jsonResponse:
  if item["name"] != "Student Affairs Resources":
    print(item["name"])


# print(response.text.encode('utf8'))
