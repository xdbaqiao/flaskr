#!/usr/bin/env python2
# coding: utf-8

import sqlite3
from contextlib import closing
from flask import Flask, url_for, request, session, g, redirect,\
        abort, render_template, flash

DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECREY_KEY = '2be7cb11cb3a5aa42256822d4fbd48f2'
USERNAME = 'admin'
PASSWORD = 'admin123'

app = Flask(__name__)
app.config.from_object(__name__)

def databse_connect():
    return sqllit3.connect(app.config['DATABASE'])

def init_db():
    with closing(databse_connect()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

if __name__ == '__main__':
    app.run()
