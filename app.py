from flask import Flask
app = Flask(__name__)

import psycopg2

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://lab10_sf5i_user:1SS5isBvW8EITDxpvIgXJHNmmgX4LxMK@dpg-co1fh7021fec73d252kg-a/lab10_sf5i") 
    conn.close()
    return "Database Connection Successful"

@app.route('/')
def hello_world():
    return 'Hello, World from Hallee Ray in 3308!'
