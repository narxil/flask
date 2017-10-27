import os
import sqlite3

from flask import (Flask, request, session, g, redirect, url_for, abort, render_template, flash)

app = Flask(__name__) #crea l'istanza dell'applicazione
app.conmfig.from_object(__name__) #load config dal file flaskr.py

app.config.update (
    DATABASE = os.path.join (app.root_path. 'flaskr.db'),
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/',
    USERNAME = 'admin',
    PASSWORD = 'default'
)

app.conf.from_envvar ('FLASKR_SETTINGS', silent=True)
