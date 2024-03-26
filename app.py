from flask import Flask
app = Flask(__name__)

import psycopg2

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab10_wo7m_user:mX4rlb5gfIozk7AJO55lmpYWrZRBwcnN@dpg-co1g20a1hbls738fog90-a/lab10_wo7m") 
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def create():
    conn = psycopg2.connect("postgres://lab10_wo7m_user:mX4rlb5gfIozk7AJO55lmpYWrZRBwcnN@dpg-co1g20a1hbls738fog90-a/lab10_wo7m") 
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Basketball(First varchar(255), Last varchar(255), City varchar(255), Name varchar(255), Number int); ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully created"

@app.route('/db_insert')
def insert():
    conn = psycopg2.connect("postgres://lab10_wo7m_user:mX4rlb5gfIozk7AJO55lmpYWrZRBwcnN@dpg-co1g20a1hbls738fog90-a/lab10_wo7m") 
    cur = conn.cursor()
    cur.execute('''INSERT INTO Basketball (First, Last, City, Name, Number)
Values
('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2); ''')
    conn.commit()
    conn.close()
    return "Basketball table populated"

@app.route('/db_select')
def select():
    conn = psycopg2.connect("postgres://lab10_wo7m_user:mX4rlb5gfIozk7AJO55lmpYWrZRBwcnN@dpg-co1g20a1hbls738fog90-a/lab10_wo7m") 
    cur = conn.cursor()
    cur.execute("SELECT * FROM Basketball;")
    records = cur.fetchall()
    conn.close()
    response_string = ""
    response_string += "<table>"
    
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string += "<td>{}</td>".format(info)
        response_string += "</tr>"
    response_string += "</table>"
    
    return response_string

@app.route('/db_drop')
def drop():
    conn = psycopg2.connect("postgres://lab10_wo7m_user:mX4rlb5gfIozk7AJO55lmpYWrZRBwcnN@dpg-co1g20a1hbls738fog90-a/lab10_wo7m") 
    cur = conn.cursor()
    cur.execute('''DROP TABLE Basketball; ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully dropped"

@app.route('/')
def hello_world():
    return 'Hello, World from Hallee Ray in 3308!'
