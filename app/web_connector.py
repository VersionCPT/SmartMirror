import requests
from bs4 import BeautifulSoup

domain = "http://127.0.0.1:5000"

def get_weather():
    url = domain + "/get_weather"
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.findChildren()

    ret = {}
    for i in link:
        ret[i.name] = i.text
    return ret

def get_news(category):
    url = domain + "/get_news?category=" + category
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.find_all("news")

    ret = []

    for i in link:
        ret.append([i.title.text, i.content.text])

    return ret

def upload_picture(file):
    url = domain + "/face_upload"
    files = {'file':open('weather_img/snow.png', 'rb')}
    r = requests.post(url, files=files)

if __name__ == "__main__":
    upload_picture(None)