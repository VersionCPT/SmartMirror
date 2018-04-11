import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import time

def get_list_urls():
    urls = {};

    url = "http://m.news.naver.com"
    url_main = "/rankingList.nhn"

    req = requests.get(url+url_main)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    link = soup.find(class_="tab_sec").find_all("a")

    for i in link:
        if i.text.startswith("섹션별"):
            req1 = requests.get(url+i.get("href"))
            html1 = req1.text
            soup1 = BeautifulSoup(html1, 'html.parser')
            link1 = soup1.find_all("a")
            #link1 = soup1.find(class_="h2_area_inner").find_all("a")
            for j in link1:
                href = j.get("href")
                if not href.startswith("/"):
                    href = "/"+href
                if j.get("id") is None or not href.startswith("/ranking"):
                    continue
                if j.get("id").startswith("politics"):
                    urls["politics"] = href
                elif j.get("id").startswith("economy"):
                    urls["economy"] = href
                elif j.get("id").startswith("society"):
                    urls["society"] = href
                elif j.get("id").startswith("it"):
                    urls["it"] = href
                elif j.get("id").startswith("life"):
                    urls["life"] = href
                elif j.get("id").startswith("world"):
                    urls["world"] = href
        elif i.text.startswith("남녀별"):
            req1 = requests.get(url+i.get("href"))
            html1 = req1.text
            soup1 = BeautifulSoup(html1, 'html.parser')
            link1 = soup1.find_all("a")
            for j in link1:
                href = j.get("href")
                if not href.startswith("/"):
                    href = "/"+href
                if not href.startswith("/ranking"):
                    continue
                if j.text.startswith("남성"):
                    urls["male"] = href
                elif j.text.startswith("여성"):
                    urls["female"] = href
        elif i.text.startswith("연령별"):
            req1 = requests.get(url+i.get("href"))
            html1 = req1.text
            soup1 = BeautifulSoup(html1, 'html.parser')
            link1 = soup1.find_all("a")
            for j in link1:
                href = j.get("href")
                if not href.startswith("/"):
                    href = "/"+href
                if not href.startswith("/ranking"):
                    continue
                if j.text.startswith("10"):
                    urls["10"] = href
                elif j.text.startswith("20"):
                    urls["20"] = href
                elif j.text.startswith("30"):
                    urls["30"] = href
                elif j.text.startswith("50"):
                    urls["50"] = href
    return urls


def get_news_urls(key, list_urls):
    if list_urls[key] is None:
        return None
    urls = []
    req = requests.get("http://m.news.naver.com"+list_urls[key])
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.find(class_="commonlist")
    link = link.find_all("a")
    for i in link:
        href = i.get("href")
        if not href.startswith("/"):
            href = "/"+href
        urls.append(href)

    return urls


def get_news(url):
    if not url.startswith("http"):
        url = "http://m.news.naver.com" + url
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.find(class_="media_end_head_headline")
    title = link.text
    link = soup.find(id="dic_area")
    body = link.text
    body = body.replace("\n","").replace("\t","")

    #print("process 3 finish")
    print([title, body])

    return [title, body]

if __name__ == '__main__':
    list_urls = get_list_urls()
    news_urls = {}
    news = {}

    start_time = time.time()
    for i in list_urls:
        news_urls[i] = get_news_urls(i, list_urls)
        news[i] = []

        pool = Pool(processes=16)
        pool.map(get_news, news_urls[i])

    print(time.time() - start_time)
