import requests
API_KEY = "pk_b7a8c4f513b246919edb92e1558c4dbf"
response_company_info = requests.get(f"https://api.iex.cloud/v1/data/core/company/GOOGL?token={API_KEY}")
json_data_company_info = response_company_info.json()
# print(json_data_company_info)
for i in json_data_company_info:
    print(i)
print(json_data_company_info[0]["marketcap"])