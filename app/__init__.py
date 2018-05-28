from app import client_gui, firebase_manager
from PyQt5.QtWidgets import *
import sys

fm = firebase_manager.FirebaseManager()
app = QApplication(sys.argv)
gui = client_gui.SmartMirrorGUI()