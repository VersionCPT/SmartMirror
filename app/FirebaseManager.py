
import firebase_admin
from firebase_admin import credentials, db

class FirebaseManager:

    def __init__(self):
        cred = credentials.Certificate('Files/Auth/smartmirror-75b89-firebase-adminsdk-vx8is-56d6e1cacc.json')
        #default_app = firebase_admin.initialize_app(cred)
        firebase_admin.initialize_app(cred, {
            'databaseURL' : 'https://smartmirror-75b89.firebaseio.com'
        })
        self.root = db.reference()
        self.new_weather = self.root.child('weather')


    def update_weather(self, weather_data):
        self.new_weather.update(weather_data)

