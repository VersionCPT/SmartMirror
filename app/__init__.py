from flask import Flask
from app import news, weather, FirebaseManager

app = Flask(__name__)
fb = FirebaseManager.FirebaseManager()

n = news.News()
w = weather.Weather()

from app.routes import *