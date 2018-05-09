from flask import Flask
from app import news

app = Flask(__name__)
n = news.News()

from app.routes import *