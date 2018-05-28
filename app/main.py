from app import gui,app
#from app import people_catcher as pc
#import threading

if __name__ == "__main__":
    gui.show()
    app.exec_()
    '''
    th = threading.Thread(target=pc.catchPeople())
    th.daemon = True
    th.start()
    '''