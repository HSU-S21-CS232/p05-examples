#pip install flask
#pip install flask-session

from flask import Flask, jsonify
import database
import os
import sqlite3
import json

app = Flask(__name__)

def return_as_json(associative_array):
    json_data = [dict(ix) for ix in associative_array]
    return jsonify(json_data)

#base route (home page)
@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'

@app.route('/about')
def about():
    return '<h1>About Me</h1><p>My name is Adam and I\'m an assistant professor at HSU</p>'

@app.route('/tracks')
def get_all_tracks():
    result = database.run_query("SELECT * FROM tracks")
    return return_as_json(result)

@app.route('/tracks/byName/<search_string>')
def search_tracks(search_string):
    sql = "SELECT * FROM tracks WHERE instr(Name, ?)>0"
    params = (search_string, )
    result = database.run_query(sql, params)
    return return_as_json(result)