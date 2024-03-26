from flask import Flask
app = Flask(__name__)

import psycopg2

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab10_wo7m_user:mX4rlb5gfIozk7AJO55lmpYWrZRBwcnN@dpg-co1g20a1hbls738fog90-a/lab10_wo7m") 
    conn.close()
    return "Database Connection Successful"

@app.route('/')
def hello_world():
    return 'Hello, World from Hallee Ray in 3308!'
