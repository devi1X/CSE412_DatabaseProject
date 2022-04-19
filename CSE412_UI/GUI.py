import sys
from PyQt5.QtCore import QDate
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
import psycopg2
from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QMainWindow
from pandas import DataFrame
from urllib.request import urlopen
import plotly.express as px

conn = psycopg2.connect(database="CSE412", user="postgres", password="838985850")

cur = conn.cursor()
cur.execute("SELECT * FROM Area LIMIT 10")
rows = cur.fetchall()

for row in rows:
    print(row)
    print("\n")
conn.commit()
cur.close()
conn.close()




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('main.ui', self)
        self.Area.clicked.connect(self.gotoArea)
        self.State.clicked.connect(self.gotoState)
        self.County.clicked.connect(self.gotoCounty)
        self.Population.clicked.connect(self.gotoPopulation)
        self.Covid_Cases.clicked.connect(self.gotoCovid)

    def gotoArea(self):
        widget.setCurrentIndex(1)
    def gotoState(self):
        widget.setCurrentIndex(2)
    def gotoCounty(self):
        widget.setCurrentIndex(3)
    def gotoPopulation(self):
        widget.setCurrentIndex(4)
    def gotoCovid(self):
        widget.setCurrentIndex(5)

class Area(QMainWindow):
    def __init__(self):
        super(Area, self).__init__()
        loadUi('Area.ui', self)


class County(QMainWindow):
    def __init__(self):
        super(County, self).__init__()
        loadUi('County.ui', self)

class Covid_Cases(QMainWindow):
    def __init__(self):
        super(Covid_Cases, self).__init__()
        loadUi('Covid_Cases.ui', self)

class Population(QMainWindow):
    def __init__(self):
        super(Population, self).__init__()
        loadUi('Population.ui', self)

class State(QMainWindow):
    def __init__(self):
        super(State, self).__init__()
        loadUi('State.ui', self)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()


widget.addWidget(MainWindow())
widget.addWidget(Area())
widget.addWidget(County())
widget.addWidget(Covid_Cases())
widget.addWidget(Population())
widget.addWidget(State())



widget.setWindowTitle("CSE 412 Covid-19 Database")
widget.setFixedHeight(1200)
widget.setFixedWidth(1200)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")



