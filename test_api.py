import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
API_KEY = "CWA-4C4F1581-B51C-4E32-8673-84ACBCAE6B08"

url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={API_KEY}"

response = requests.get(url, verify=False)

if response.status_code == 200:
    data = response.json()
    print('Get data successfully')

    locations = data["records"]["location"]
    
    target_city = "臺中市"
    found_index = -1

    for i in range(len(locations)):
        if locations[i]['locationName'] == target_city:
            found_index = i
            break
    if found_index != -1 :
        print(f'找到{target_city}了, found_index = {found_index}')

        target_weather_elements = locations[i]['weatherElement']

        for element in target_weather_elements:
            name = element['elementName']

            mapping = {
                'Wx': '天氣現象',
                'PoP': '降雨機率',
                'MinT':'最低溫',
                'CI':'體感',
                'MaxT':'最高溫'
            }

            chinese_name = mapping.get(name, name)
            value = element['time'][0]['parameter']['parameterName']
            print(f'elementName:{name}({chinese_name}) -> {value}')
    
    else:
        print('Not Found')


