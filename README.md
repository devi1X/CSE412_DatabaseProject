# CSE412_DatabaseProject

## Tools used for this project:
PyQt5  
psycopg2  
Qt Designer  
Python 3.8.0    
PostgreSQL (14.1)  
PyCharm CE  
Git/GitHub

## How to use this application:
### 1. Clone the repository of this application by using the code below.
git clone https://github.com/devi1X/CSE412_DatabaseProject
### 2. Install PyQt5 and psycopg2 by using the code below.
pip install PyQt5  
pip install psycopg2  
(For MacOS:  
            pip3 install PyQt5  
            pip3 install psycopg2  
)
### 3. Set up PostgreSQL in your computer

### 4. Follow the guide to create database and insert data
https://docs.google.com/document/d/1po43tCQl34IgnkJckKIhjp5URosIXvR74iuM_b13B_k/edit?usp=sharing

### 5: Change database information in GUI.py file
#### 5.1 Find  conn = psycopg2.connect(database="CSE412", user="postgres", password="838985850")  
#### There are many statements need to modify. You can use Ctrl + F to find and change statement easily. 
#### 5.2 Change database, user, and password to your local database information  

### 6: Run GUI.py using PyCharm CE

### Notes: The best way to run this application is using PyCharm CE, if you use terminal, some error may happen.
### Some error will happen if you try to install PyQt5 and psycopg2 on ARM Mac




