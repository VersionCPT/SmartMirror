import requests
from bs4 import BeautifulSoup

domain = "http://203.252.166.206:5000"

def get_weather():
    '''
    url = domain + "/get_weather"
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.findChildren()

    ret = {}
    for i in link:
        ret[i.name] = i.text
    return ret
    '''
    #return fm.get_weather()
    pass

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
    files = {'file':open(file, 'rb')}
    r = requests.post(url, files=files)

def get_location():
    url = "https://후이즈검색.한국"+"/kor/whois/whois.jsp"

    info = {'sWord' : '14.42.5.175'}

    s = requests.Session()

    req = s.post(url, data=info)
    #req = requests.post(url, data={'query.value':'14.42.5.175', 'action':'/kor/whois/whois.jsp', 'target':''})
    #print(req.status_code)
    #html = req.text
    #soup = BeautifulSoup(html, 'html.parser')
    #print(soup)

if __name__ == "__main__":
    get_location()