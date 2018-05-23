
import firebase_admin
from firebase_admin import credentials, db

class firebase_manager:

    def __init__(self):
        cred = credentials.Certificate('Files/Auth/smartmirror-75b89-firebase-adminsdk-vx8is-56d6e1cacc.json')
        #default_app = firebase_admin.initialize_app(cred)
        firebase_admin.initialize_app(cred, {
            'databaseURL' : 'https://smartmirror-75b89.firebaseio.com'
        })
        self.root = db.reference()
        self.weather = self.root.child('weather')

    def get_weather(self):
        weather_data = db.reference('weather'.format(self.weather.key)).get()
        print(weather_data['cur_sky'])
