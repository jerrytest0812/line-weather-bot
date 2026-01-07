import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
API_KEY = "CWA-4C4F1581-B51C-4E32-8673-84ACBCAE6B08"


def get_weather_data(city_name, API_KEY):

    url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={API_KEY}"
    response = requests.get(url, verify=False)

    weather_data = {}
    if response.status_code == 200:
        data = response.json()
        print('Get data successfully')

        locations = data["records"]["location"]
        
        city_name = city_name
        found_index = -1

        for i in range(len(locations)):
            if locations[i]['locationName'] == city_name:
                found_index = i
                break
        if found_index != -1 :
            print(f'找到{city_name}了, found_index = {found_index}')

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
                # print(f'elementName:{name}({chinese_name}) -> {value}')
                weather_data[chinese_name]=value
        else:
            print('Not Found')
    return(f"{city_name} 天氣：{weather_data['天氣現象']}\n降雨機率:{weather_data['降雨機率']}\n氣溫:{weather_data['最低溫']}~{weather_data['最高溫']} ")


if __name__ == '__main__':
    print(get_weather_data('嘉義市',API_KEY))
