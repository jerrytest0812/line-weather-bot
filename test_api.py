import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
API_KEY = "CWA-4C4F1581-B51C-4E32-8673-84ACBCAE6B08"

url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={API_KEY}"

response = requests.get(url, verify=False)

if response.status_code == 200:
    data = response.json()
    print('Get data successfully')
    