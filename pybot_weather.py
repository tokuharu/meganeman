#python3
import requests

def weather_command():
    base_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    #鳥取のシティコードを用意
    city_code = '310010'
    #URLを作成
    url = '{}?city={}'.format(base_url, city_code)
    #天気予報データを取得
    r = requests.get(url)
    weather_data = r.json()
    #都市名を取得
    city = weather_data['location']['city']
    #日付を取得
    label = weather_data['forecasts'][0]['dateLabel']
    #天気を取得
    telop = weather_data['forecasts'][0]['telop']

    response = '{}ノ{}ノ天気ハ「{}」デス'.format(city, label, telop)
    #結果を返す
    return response
