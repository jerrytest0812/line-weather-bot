import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
API_KEY = "CWA-4C4F1581-B51C-4E32-8673-84ACBCAE6B08"

url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={API_KEY}"

response = requests.get(url, verify=False)

if response.status_code == 200:
    data = response.json()
    print('Get data successfully')

    location = data["records"]["location"][0]
    city_name = location['locationName']
    weather_elements = location['weatherElement']

    print(f'-----{city_name} 36 小時天氣預報-----')

    for element in weather_elements:
        element_name = element['elementName']
        element_value = element['time'][0]['parameter']['parameterName']
        

        
        if element_name == 'Wx':
            startTime = element['time'][0]['startTime']
            print(f'時間{startTime}')
            print(f'天氣現象:{element_value}')
        elif element_name == 'PoP':
            print(f'降雨機率:{element_value}%')
        elif element_name == 'MinT':
            print(f'最低溫:{element_value}°C')
    