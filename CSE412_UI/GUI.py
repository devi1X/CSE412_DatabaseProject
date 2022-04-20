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
        self.MainPage.clicked.connect(self.GoMainPage)
        self.Display.clicked.connect(self.DisplayTable)
        self.Search.clicked.connect(self.SearchTable)
        self.State.clicked.connect(self.StatePage)
        self.County.clicked.connect(self.CountyPage)
        self.Population.clicked.connect(self.PolulationPage)
        self.Covid_Cases.clicked.connect(self.CasePage)



    def StatePage(self):
        widget.setCurrentIndex(2)

    def CasePage(self):
        widget.setCurrentIndex(3)

    def PolulationPage(self):
        widget.setCurrentIndex(4)

    def CountyPage(self):
        widget.setCurrentIndex(5)
    def GoMainPage(self):
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
        self.MainPage.clicked.connect(self.GoMainPage)
        self.Display.clicked.connect(self.DisplayTable)
        self.Search.clicked.connect(self.SearchTable)
        self.Area.clicked.connect(self.AreaPage)
        self.County.clicked.connect(self.CountyPage)
        self.Population.clicked.connect(self.PolulationPage)
        self.Covid_Cases.clicked.connect(self.CasePage)

    def AreaPage(self):
        widget.setCurrentIndex(1)

    def CasePage(self):
        widget.setCurrentIndex(3)

    def PolulationPage(self):
        widget.setCurrentIndex(4)

    def CountyPage(self):
        widget.setCurrentIndex(5)
    def GoMainPage(self):
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
        self.MainPage.clicked.connect(self.GoMainPage)
        self.Display.clicked.connect(self.DisplayTable)
        self.Search.clicked.connect(self.SearchTable)
        self.Area.clicked.connect(self.AreaPage)
        self.State.clicked.connect(self.StatePage)
        self.County.clicked.connect(self.CountyPage)
        self.Population.clicked.connect(self.PolulationPage)

    def AreaPage(self):
        widget.setCurrentIndex(1)

    def StatePage(self):
        widget.setCurrentIndex(2)

    def PolulationPage(self):
        widget.setCurrentIndex(4)

    def CountyPage(self):
        widget.setCurrentIndex(5)

    def GoMainPage(self):
        widget.setCurrentIndex(0)
    def SearchTable(self):
        conn = psycopg2.connect(database="CSE412", user="postgres", password="838985850")
        cur = conn.cursor()

        if self.box3.currentText() == "Date":

            SearchString = self.lineEdit.text()
            cur.execute('''SELECT * FROM Covid_Cases WHERE Date =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()


            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
                self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem())
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    tablerow = tablerow + 1
        elif self.box3.currentText() == "FIPS":
            SearchString = self.lineEdit.text()

            cur.execute('''SELECT * FROM Covid_Cases WHERE FIPS   =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()

            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
                self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem())
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    tablerow = tablerow + 1
        elif self.box3.currentText() == "Total_Cases":
            SearchString = self.lineEdit.text()

            cur.execute('''SELECT * FROM Covid_Cases WHERE Total_Cases   =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()

            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
                self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem())
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    tablerow = tablerow + 1

        else:
            SearchString = self.lineEdit.text()

            cur.execute('''SELECT * FROM Covid_Cases WHERE Total_Deaths   =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()

            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
                self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem())
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    tablerow = tablerow + 1
    def DisplayTable(self):
        conn = psycopg2.connect(database="CSE412", user="postgres", password="838985850")
        cur = conn.cursor()

        if self.box1.currentText() == "ALL":
            if self.box2.currentText() == "ALL":
                cur.execute("SELECT * FROM Covid_Cases")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT * FROM Covid_Cases LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT * FROM Covid_Cases LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    tablerow = tablerow + 1


        elif self.box1.currentText() == "Date":
            if self.box2.currentText() == "ALL":
                cur.execute("SELECT Date FROM Covid_Cases")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT Date FROM Covid_Cases LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT Date FROM Covid_Cases LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
        elif self.box1.currentText() == "FIPS":

            if self.box2.currentText() == "ALL":
                cur.execute("SELECT FIPS FROM Covid_Cases")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT FIPS FROM Covid_Cases LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT FIPS FROM Covid_Cases LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1

        elif self.box1.currentText() == "Total_Cases":
            if self.box2.currentText() == "ALL":
                cur.execute("SELECT Total_Cases FROM Covid_Cases")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT Total_Cases FROM Covid_Cases LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT Total_Cases FROM Covid_Cases LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1

        else:
            if self.box2.currentText() == "ALL":
                cur.execute("SELECT Total_Deaths FROM Covid_Cases")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[0])))
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT Total_Deaths FROM Covid_Cases LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[0])))
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT Total_Deaths FROM Covid_Cases LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[0])))
                    tablerow = tablerow + 1
        cur.close()
        conn.close()


class Population(QMainWindow):
    def __init__(self):
        super(Population, self).__init__()
        loadUi('Population.ui', self)
        self.MainPage.clicked.connect(self.GoMainPage)
        self.Display.clicked.connect(self.DisplayTable)
        self.Search.clicked.connect(self.SearchTable)
        self.Area.clicked.connect(self.AreaPage)
        self.State.clicked.connect(self.StatePage)
        self.County.clicked.connect(self.CountyPage)
        self.Covid_Cases.clicked.connect(self.CasePage)

    def AreaPage(self):
        widget.setCurrentIndex(1)

    def StatePage(self):
        widget.setCurrentIndex(2)

    def CasePage(self):
        widget.setCurrentIndex(3)

    def CountyPage(self):
        widget.setCurrentIndex(5)


    def GoMainPage(self):
        widget.setCurrentIndex(0)
    def SearchTable(self):
        conn = psycopg2.connect(database="CSE412", user="postgres", password="838985850")
        cur = conn.cursor()

        if self.box3.currentText() == "FIPS":

            SearchString = self.lineEdit.text()
            cur.execute('''SELECT * FROM Population WHERE FIPS =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()


            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
                self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem())
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                    tablerow = tablerow + 1
        elif self.box3.currentText() == "Total":
            SearchString = self.lineEdit.text()

            cur.execute('''SELECT * FROM Population WHERE Total   =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()

            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
                self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem())
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                    tablerow = tablerow + 1
        elif self.box3.currentText() == "Male":
            SearchString = self.lineEdit.text()

            cur.execute('''SELECT * FROM Population WHERE Male   =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()

            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
                self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem())
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                    tablerow = tablerow + 1


        elif self.box3.currentText() == "Female":

            SearchString = self.lineEdit.text()

            cur.execute('''SELECT * FROM Population WHERE Female   =%s ''', (SearchString,))

            tablerow = 0

            rows = cur.fetchall()

            if len(rows) == 0:

                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
                self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem())

            else:

                self.tableWidget.setRowCount(len(rows))

                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))

                    tablerow = tablerow + 1

        elif self.box3.currentText() == "18+":
            SearchString = self.lineEdit.text()

            cur.execute('''SELECT * FROM Population WHERE "18+"   =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()

            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
                self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem())
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                    tablerow = tablerow + 1

        elif self.box3.currentText() == "65+":
            SearchString = self.lineEdit.text()

            cur.execute('''SELECT * FROM Population WHERE "65+"   =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()

            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
                self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem())
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                    tablerow = tablerow + 1
        elif self.box3.currentText() == "One_Race":
            SearchString = self.lineEdit.text()

            cur.execute('''SELECT * FROM Population WHERE One_Race   =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()

            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
                self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem())
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                    tablerow = tablerow + 1
        elif self.box3.currentText() == "Two_and_more_race":
            SearchString = self.lineEdit.text()

            cur.execute('''SELECT * FROM Population WHERE Two_and_more_race   =%s ''', (SearchString,))
            tablerow = 0
            rows = cur.fetchall()

            if len(rows) == 0:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Not"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Found"))
                self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem())
                self.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem())
            else:
                self.tableWidget.setRowCount(len(rows))
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                    tablerow = tablerow + 1
    def DisplayTable(self):
        conn = psycopg2.connect(database="CSE412", user="postgres", password="838985850")
        cur = conn.cursor()
        if self.box1.currentText() == "ALL":
            if self.box2.currentText() == "ALL":
                cur.execute("SELECT * FROM Population")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT * FROM Population LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:

                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT * FROM Population LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                    tablerow = tablerow + 1


        elif self.box1.currentText() == "FIPS":
            if self.box2.currentText() == "ALL":
                cur.execute("SELECT FIPS FROM Population")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT FIPS FROM Population LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT FIPS FROM Population LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
        elif self.box1.currentText() == "Total":

            if self.box2.currentText() == "ALL":
                cur.execute("SELECT Total FROM Population")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT Total FROM Population LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT Total FROM Population LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1

        elif self.box1.currentText() == "Male":
            if self.box2.currentText() == "ALL":
                cur.execute("SELECT Male FROM Population")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT Male FROM Population LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT Male FROM Population LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1

        elif self.box1.currentText() == "Female":
            if self.box2.currentText() == "ALL":
                cur.execute("SELECT Female FROM Population")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT Female FROM Population LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT Female FROM Population LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
        elif self.box1.currentText() == "18+":
            if self.box2.currentText() == "ALL":
                cur.execute('SELECT "18+" FROM Population')
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute('SELECT "18+" FROM Population LIMIT 10')
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            else:
                cur.execute('SELECT "18+" FROM Population LIMIT 100')
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
        elif self.box1.currentText() == "65+":
            if self.box2.currentText() == "ALL":
                cur.execute('SELECT "65+" FROM Population')
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute('SELECT "65+" FROM Population LIMIT 10')
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            else:
                cur.execute('SELECT "65+" FROM Population LIMIT 100')
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
        elif self.box1.currentText() == "One_Race":
            if self.box2.currentText() == "ALL":
                cur.execute("SELECT One_Race FROM Population")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT One_Race FROM Population LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT One_Race FROM Population LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem())
                    tablerow = tablerow + 1
        elif self.box1.currentText() == "Two_and_more_race":
            if self.box2.currentText() == "ALL":
                cur.execute("SELECT Two_and_more_race FROM Population")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[0])))
                    tablerow = tablerow + 1
            elif self.box2.currentText() == "First 10 Rows":
                cur.execute("SELECT Two_and_more_race FROM Population LIMIT 10")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[0])))
                    tablerow = tablerow + 1
            else:
                cur.execute("SELECT Two_and_more_race FROM Population LIMIT 100")
                tablerow = 0
                rows = cur.fetchall()
                self.tableWidget.setRowCount(len(rows))
                # self.table.setColumnCount(1)
                for row in rows:
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem())
                    self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[0])))
                    tablerow = tablerow + 1
        cur.close()
        conn.close()

class County(QMainWindow):
    def __init__(self):
        super(County, self).__init__()
        loadUi('County.ui', self)
        self.MainPage.clicked.connect(self.GoMainPage)
        self.Display.clicked.connect(self.DisplayTable)
        self.Area.clicked.connect(self.AreaPage)
        self.State.clicked.connect(self.StatePage)
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

    def GoMainPage(self):
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
widget.setFixedHeight(980)
widget.setFixedWidth(1060)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
