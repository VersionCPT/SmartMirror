import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import datetime
import time
import threading

class SmartMirrorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.showFullScreen()
        self.setWindowTitle('鏡:Rorrim')
        self.initUI()

    def closeEvent(self, event):
        self.deleteLater()

    def initUI(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        vlayout = QVBoxLayout()
        self.setLayout(vlayout)
        self.addDatetime()
        self.addSchedule()
        self.addNews()
        self.addMusic()
        self.addWeather()
        #ttt = threading.Timer(1, self.updateDatetime).start()
        th = threading.Thread(target=self.updateDatetime)
        th.start()
        self.show()

    def addSchedule(self):
        # get schedules from server or google calendar
        schedules = []
        schedules.append(["12:00", "족발먹기"])
        schedules.append(["14:20", "곱창먹기"])
        schedules.append(["15:00", "학교가기"])

        num_schedules = len(schedules)

        scheduleLB = []
        for i in range(num_schedules):
            LB = QLabel(schedules[i][0]+" "+schedules[i][1])
            LB.setStyleSheet('color: white')
            LB.setFont(QFont("", 45, QFont.Bold))
            LB.setFixedSize(self.width()/100*40, self.height()/100*7)
            LB.move(self.width()/100*3, self.height()/100*(97-(num_schedules-i)*7))
            LB.setAutoFillBackground(True)
            p = LB.palette()
            p.setColor(LB.backgroundRole(), Qt.black)
            LB.setPalette(p)
            LB.setAlignment(Qt.AlignVCenter)
            scheduleLB.append(LB)

        self.scheduleLB = scheduleLB
        for i in self.scheduleLB:
            self.layout().addChildWidget(i)

    def addNews(self):
        # get news from server
        news = []
        news.append("장미 유전자 지도 완성…'완벽한' 장미 나올")
        news.append("삼성 갤럭시S9 이어 노트9에도 'SLP'적용한..")
        news.append("\"영혼을 찾아라\" 불붙은 민규의 영혼 찾기")
        news.append("반도를 강타한 어벤져스3… 5번 감상한 백승..")

        num_news = len(news)

        newsLB = []
        for i in range(num_news):
            LB = QLabel(news[i])
            LB.setStyleSheet('color: white')
            LB.setFont(QFont("", 30, QFont.Bold))
            LB.setFixedSize(self.width()/100*40, self.height()/100*5)
            LB.move(self.width()/100*57, self.height()/100*(97-(num_news-i)*5))
            LB.setAutoFillBackground(True)
            p = LB.palette()
            p.setColor(LB.backgroundRole(), Qt.black)
            LB.setPalette(p)
            LB.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
            newsLB.append(LB)

        self.newsLB = newsLB
        for i in self.newsLB:
            self.layout().addChildWidget(i)

    def addWeather(self):
        # get weather information from server or by using api

        imgLB = QLabel()
        img = QPixmap("rain.png")
        img.scaledToWidth(10, Qt.FastTransformation)
        img = img.scaledToWidth(self.width()/100*10)
        imgLB.setPixmap(img)
        imgLB.setFixedSize(img.width(), img.height())
        imgLB.move(self.width()/100*3, self.height()/100*5)
        imgLB.setAutoFillBackground(True)
        p = imgLB.palette()
        p.setColor(imgLB.backgroundRole(), Qt.black)
        imgLB.setPalette(p)
        imgLB.setAlignment(Qt.AlignCenter)

        tempLB = QLabel("16˚C")
        tempLB.setStyleSheet('color: white')
        tempLB.setFont(QFont("", 60, QFont.Bold))
        tempLB.setFixedSize(self.width()/100*10, img.height())
        tempLB.move(self.width()/100*5+img.width(), self.height()/100*5)
        tempLB.setAutoFillBackground(True)
        p = tempLB.palette()
        p.setColor(tempLB.backgroundRole(), Qt.black)
        tempLB.setPalette(p)
        tempLB.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        locLB = QLabel("서울 광진구 화양동")
        locLB.setStyleSheet('color: white')
        locLB.setFont(QFont("", 40, QFont.Bold))
        locLB.setFixedSize(self.width()/100*30, self.height()/100*6)
        locLB.move(self.width()/100*5, self.height()/100*5+img.height())
        locLB.setAutoFillBackground(True)
        p = locLB.palette()
        p.setColor(locLB.backgroundRole(), Qt.black)
        locLB.setPalette(p)
        locLB.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        mmLB = QLabel("▲22˚C ▼12˚C")
        mmLB.setStyleSheet('color: white')
        mmLB.setFont(QFont("", 40, QFont.Bold))
        mmLB.setFixedSize(self.width()/100*30, self.height()/100*6)
        mmLB.move(self.width()/100*5, self.height()/100*11 + img.height())
        mmLB.setAutoFillBackground(True)
        p = mmLB.palette()
        p.setColor(mmLB.backgroundRole(), Qt.black)
        mmLB.setPalette(p)
        mmLB.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        self.layout().addChildWidget(imgLB)
        self.layout().addChildWidget(tempLB)
        self.layout().addChildWidget(locLB)
        self.layout().addChildWidget(mmLB)


    def addMusic(self):
        # get music file or information
        musics = []
        musics.append(["♬ What is Love?", "TWICE(트와이스)"])

        musicLB = []
        titleLB = QLabel(musics[0][0])
        titleLB.setStyleSheet('color: white')
        titleLB.setFont(QFont("", 40, QFont.Bold))
        titleLB.setFixedSize(self.width()/100*30, self.height()/100*6)
        titleLB.move(self.width()/100*35, self.height()/100*7)
        titleLB.setAutoFillBackground(True)
        p = titleLB.palette()
        p.setColor(titleLB.backgroundRole(), Qt.black)
        titleLB.setPalette(p)
        titleLB.setAlignment(Qt.AlignHCenter)
        musicLB.append(titleLB)

        artistLB = QLabel(musics[0][1])
        artistLB.setStyleSheet('color: white')
        artistLB.setFont(QFont("", 30, QFont.Bold))
        artistLB.setFixedSize(self.width()/100*30, self.height()/100*6)
        artistLB.move(self.width()/100*35, self.height()/100*13)
        artistLB.setAutoFillBackground(True)
        p = artistLB.palette()
        p.setColor(artistLB.backgroundRole(), Qt.black)
        artistLB.setPalette(p)
        artistLB.setAlignment(Qt.AlignHCenter)
        musicLB.append(artistLB)

        self.musicLB = musicLB
        self.layout().addChildWidget(self.musicLB[0])
        self.layout().addChildWidget(self.musicLB[1])

    def addDatetime(self):
        dt = datetime.datetime.now()

        weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
        month = ["December", "January", "February", "March", "April", "May", "June", "July", "August", "September",
                 "October", "November", "December"]
        d = weekday[dt.weekday()] + ", " + month[dt.month] + " " + str(dt.day) + " " + str(dt.year)

        dateLB = QLabel(d)
        dateLB.setStyleSheet('color: white')
        dateLB.setFont(QFont("", 37, QFont.Bold))
        dateLB.setFixedSize(self.width()/100*30, self.height()/100*6)
        dateLB.move(self.width()/100*67, self.height()/100*7)
        dateLB.setAutoFillBackground(True)
        p = dateLB.palette()
        p.setColor(dateLB.backgroundRole(), Qt.black)
        dateLB.setPalette(p)
        dateLB.setAlignment(Qt.AlignRight)

        t = str(dt)[11:16]
        if dt.hour > 12:
            t = t + " PM"
        else:
            t = t + " AM"
        timeLB = QLabel(t)
        timeLB.setStyleSheet('color: white')
        timeLB.setFont(QFont("", 65, QFont.Bold))
        timeLB.setFixedSize(self.width()/100*30, self.height()/100*8)
        timeLB.move(self.width()/100*67, self.height()/100*13)
        timeLB.setAutoFillBackground(True)
        p = timeLB.palette()
        p.setColor(timeLB.backgroundRole(), Qt.black)
        timeLB.setPalette(p)
        timeLB.setAlignment(Qt.AlignRight | Qt.AlignTop)

        self.timeLB = timeLB
        self.dateLB = dateLB
        self.layout().addChildWidget(self.dateLB)
        self.layout().addChildWidget(self.timeLB)

    def updateDatetime(self):
        while(True):
            try:
                dt = datetime.datetime.now()

                weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
                month = ["December", "January", "February", "March", "April", "May", "June", "July", "August", "September",
                         "October", "November", "December"]
                d = weekday[dt.weekday()] + ", " + month[dt.month] + " " + str(dt.day) + " " + str(dt.year)
                t = str(dt)[11:16]
                if dt.hour > 12:
                    t = t + " PM"
                else:
                    t = t + " AM"
                self.dateLB.setText(d)
                self.timeLB.setText(t)
                time.sleep(1)
            except:
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SmartMirrorGUI()
    app.exec_()
