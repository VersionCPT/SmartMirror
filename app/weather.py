# coding:utf-8
import datetime
import pytz
import urllib.request
import json
import time

class Weather:

    def __init__(self):
        self.data = {}

    def closeEvent(self, event):
        self.deleteLater()

    def get_api_date(self):
        standard_time = [2, 5, 8, 11, 14, 17, 20, 23]
        time_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%H')
        check_time = int(time_now) - 1
        day_calibrate = 0

        """
        while not check_time in standard_time:
            check_time -= 1
            if check_time < 2:
                day_calibrate = 1
                check_time = 23
                break
        """

        date_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%Y%m%d')
        check_date = int(date_now) - day_calibrate

        return (str(check_date), "0200")
        """
        if check_time < 10:
            return (str(check_date), '0' + (str(check_time) + '00'))
        return (str(check_date), (str(check_time) + '00'))
        """

    @property
    def get_weather_data(self):
        api_date, api_time = self.get_api_date()
        url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
        key = "serviceKey=" + '6h85ymiuerjoMWrN4hcNYKw9WKoakFovGEvoZgvspK11p37pFe1mAF1cFftuaPkM2wBrDBxvMuFj7a%2B%2BSNrPSw%3D%3D'
        date = "&base_date=" + api_date
        time = "&base_time=" + api_time
        nx = "&nx=97"
        ny = "&ny=76"
        numOfRows = "&numOfRows=100"
        type = "&_type=json"
        api_url = url + key + date + time + nx + ny + numOfRows + type

        data = urllib.request.urlopen(api_url).read().decode('utf8')
        data_json = json.loads(data)

        parsed_json = data_json['response']['body']['items']['item']

        target_date = parsed_json[0]['fcstDate']  # get date and time
        target_time = parsed_json[0]['fcstTime']

        date_calibrate = target_date  # date of TMX, TMN

        if int(target_time) > 1300:
            date_calibrate = str(int(target_date) + 1)

        passing_data = {}

        dt = datetime.datetime.now()

        for one_parsed in parsed_json:
            if one_parsed['fcstDate'] == int(api_date) and one_parsed['category'] in ['TMX', 'TMN']:
                passing_data[one_parsed['category']] = one_parsed['fcstValue']
            elif int(dt.hour)*100+int(dt.minute) >= int(one_parsed['fcstTime'])-150:
                if int(dt.hour) * 100 + int(dt.minute) <= int(one_parsed['fcstTime'])+150:
                    passing_data[one_parsed['category']] = one_parsed['fcstValue']
        return passing_data

    def get_max_tem(self):  # 최고기온
        data = self.get_weather_data
        tmx = data['TMX']

        return tmx

    def get_min_tem(self):  # 최저기온
        data = self.get_weather_data
        tmn = data['TMN']

        return tmn

    def get_cur_tem(self):  # 현재기온
        data = self.get_weather_data
        t3h = data['T3H']

        return t3h

    def get_is_rain(self):  # 비오는지
        '''
        0 : 없음
        1 : 비
        2 : 비/눈
        3 :  눈
        '''
        data = self.get_weather_data
        pty = data['PTY']
        return pty

    def get_is_cloudy(self):  # 흐린지
        '''
          1 : 맑음
          2 : 구름조금
          3 : 구름많음
          4 : 흐림
          '''
        data = self.get_weather_data
        sky = data['SKY']

        return sky

    def print_weather(self):

        print(self.get_min_tem())
        rain = self.get_is_rain()
        cloud = self.get_is_cloudy()

        if (rain == 0):
            if (cloud == 1):
                print('sunny')
            elif (cloud == 2):
                print('cloudy')
            elif (cloud == 3):
                print('clooooooudy')
            elif (cloud == 4):
                print('foggy')
        elif (rain == 1):
            print('rainy')
        elif (rain == 2):
            print('rain with snow')
        elif (rain == 3):
            print('snowy')

    def get_weather_data_thread(self):
        while(True):
            try:
                self.data = self.get_weather_data
                dt = datetime.datetime.now()
                print("weather data updated at "+str(dt.hour)+"h "+str(dt.minute)+"m "+str(dt.second)+"s")
                time.sleep(600)
            except:
                print("bb")
                break

    def get_weather(self):
        return self.data