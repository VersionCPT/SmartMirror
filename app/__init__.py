from flask import Flask
from app import news,weather

app = Flask(__name__)
n = news.News()
w = weather.Weather()

from app.routes import *