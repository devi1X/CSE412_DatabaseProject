import sys
from PyQt5.QtCore import QDate
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
import psycopg2
from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QMainWindow, QTableWidget, QTableWidgetItem
from pandas import DataFrame
from urllib.request import urlopen
import plotly.express as px


# conn = psycopg2.connect(database="CSE412", user="postgres", password="838985850")

# cur = conn.cursor()
# cur.execute("SELECT * FROM Area LIMIT 10")
# rows = cur.fetchall()

# for row in rows:
# print(row)
# print("\n")
# conn.commit()
# cur.close()
# conn.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('main.ui', self)
        self.Area.clicked.connect(self.AreaPage)
        self.State.clicked.connect(self.StatePage)
        self.County.clicked.connect(self.CountyPage)
        self.Population.clicked.connect(self.PolulationPage)
        self.Covid_Cases.clicked.connect(self.CasePage)

    def AreaPage(self):
        widget.setCurrentIndex(1)

    def StatePage(self):
        widget.setCurrentIndex(2)

    def CasePage(self):
        widget.setCurrentIndex(3)

    def PolulationPage(self):
        widget.setCurrentIndex(4)

    def CountyPage(self):
        widget.setCurrentIndex(5)


class Area(QMainWindow):
    def __init__(self):
        super(Area, self).__init__()
        loadUi('Area.ui', self)
        self.Back.clicked.connect(self.GoBack)
        self.Display.clicked.connect(self.DisplayTable)
        self.Search.clicked.connect(self.SearchTable)

    def GoBack(self):
        widget.setCurrentIndex(0)

    def SearchTable(self):
        conn = psycopg2.connect(database="CSE412", user="postgres", password="838985850")
        cur = conn.cursor()
        if self.box3.currentText() == "Area_Name":

            SearchString = self.lineEdit.text()

            cur.execute('''SELECT * FROM Area WHERE Area_Name =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()

            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    tablerow = tablerow + 1
        else:
            SearchString = self.lineEdit.text()

            cur.execute('''SELECT * FROM Area WHERE FIPS   =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()

            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    tablerow = tablerow + 1

    def DisplayTable(self):
        conn = psycopg2.connect(database="CSE412", user="postgres", password="838985850")
        cur = conn.cursor()

        if self.box1.currentText() == "ALL":
            if self.box2.currentText() == "ALL":
                cur.execute("SELECT * FROM Area")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT * FROM Area LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT * FROM Area LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    tablerow = tablerow + 1


        elif self.box1.currentText() == "FIPS":
            if self.box2.currentText() == "ALL":
                cur.execute("SELECT FIPS FROM Area")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT FIPS FROM Area LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT FIPS FROM Area LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
        else:
            if self.box2.currentText() == "ALL":

                cur.execute("SELECT Area_Name FROM Area")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[0])))
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT Area_Name FROM Area LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[0])))
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT Area_Name FROM Area LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[0])))
                    tablerow = tablerow + 1
        cur.close()
        conn.close()


class State(QMainWindow):
    def __init__(self):
        super(State, self).__init__()
        loadUi('State.ui', self)
        self.Back.clicked.connect(self.GoBack)
        self.Display.clicked.connect(self.DisplayTable)
        self.Search.clicked.connect(self.SearchTable)

    def GoBack(self):
        widget.setCurrentIndex(0)
    def SearchTable(self):
        conn = psycopg2.connect(database="CSE412", user="postgres", password="838985850")
        cur = conn.cursor()
        if self.box3.currentText() == "Postal_abbr":

            SearchString = self.lineEdit.text()

            cur.execute('''SELECT * FROM State WHERE Postal_abbr =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()

            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    tablerow = tablerow + 1
        else:
            SearchString = self.lineEdit.text()

            cur.execute('''SELECT * FROM State WHERE FIPS   =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()

            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    tablerow = tablerow + 1

    def DisplayTable(self):
        conn = psycopg2.connect(database="CSE412", user="postgres", password="838985850")
        cur = conn.cursor()

        if self.box1.currentText() == "ALL":
            if self.box2.currentText() == "ALL":
                cur.execute("SELECT * FROM State")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT * FROM State LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT * FROM State LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    tablerow = tablerow + 1


        elif self.box1.currentText() == "FIPS":
            if self.box2.currentText() == "ALL":
                cur.execute("SELECT FIPS FROM State")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT FIPS FROM State LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT FIPS FROM State LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
        else:
            if self.box2.currentText() == "ALL":

                cur.execute("SELECT Postal_abbr FROM State")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[0])))
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT Postal_abbr FROM State LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[0])))
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT Postal_abbr FROM State LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[0])))
                    tablerow = tablerow + 1
        cur.close()
        conn.close()


class Covid_Cases(QMainWindow):
    def __init__(self):
        super(Covid_Cases, self).__init__()
        loadUi('Covid_Cases.ui', self)
        self.Back.clicked.connect(self.GoBack)




    def GoBack(self):
        widget.setCurrentIndex(0)


class Population(QMainWindow):
    def __init__(self):
        super(Population, self).__init__()
        loadUi('Population.ui', self)
        self.Back.clicked.connect(self.GoBack)

    def GoBack(self):
        widget.setCurrentIndex(0)


class County(QMainWindow):
    def __init__(self):
        super(County, self).__init__()
        loadUi('County.ui', self)
        self.Back.clicked.connect(self.GoBack)
        self.Display.clicked.connect(self.DisplayTable)
        self.tableWidget.setColumnWidth(0, 150)

    def GoBack(self):
        widget.setCurrentIndex(0)

    def DisplayTable(self):
        conn = psycopg2.connect(database="CSE412", user="postgres", password="838985850")
        cur = conn.cursor()
        if (self.box.currentText() == "ALL"):
            cur.execute("SELECT * FROM County")
            tablerow = 0
            rows = cur.fetchall()
            self.tableWidget.setRowCount(len(rows))
            # self.table.setColumnCount(1)
            for row in rows:
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                tablerow = tablerow + 1



        elif (self.box.currentText() == "First 10 Rows"):
            cur.execute("SELECT * FROM County LIMIT 10")
            tablerow = 0
            rows = cur.fetchall()
            self.tableWidget.setRowCount(len(rows))
            # self.table.setColumnCount(1)
            for row in rows:
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                tablerow = tablerow + 1
        else:
            cur.execute("SELECT * FROM County LIMIT 100")
            tablerow = 0
            rows = cur.fetchall()
            self.tableWidget.setRowCount(len(rows))
            # self.table.setColumnCount(1)
            for row in rows:
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                tablerow = tablerow + 1
        cur.close()
        conn.close()


app = QtWidgets.QApplication(sys.argv)
app.setStyle("fusion")
widget = QtWidgets.QStackedWidget()

widget.addWidget(MainWindow())
widget.addWidget(Area())
widget.addWidget(State())
widget.addWidget(Covid_Cases())
widget.addWidget(Population())
widget.addWidget(County())

widget.setWindowTitle("COVID-19 DATA HELPER")

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
