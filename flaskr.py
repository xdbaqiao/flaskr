#!/usr/bin/env python2
# coding: utf-8
from flask import Flask, url_for, request, session, g, redirect,\
        abort, render_template, flash

DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECREY_KEY = '2be7cb11cb3a5aa42256822d4fbd48f2'
USERNAME = 'admin'
PASSWORD = 'admin123'

app = Falsk(__name__)
app.config.from_object(__name__)



if __name__ == '__main__':
