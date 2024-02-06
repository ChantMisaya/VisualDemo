# -*- coding:utf-8 -*-
# Time: 06/02/2024 21:51
# Author: Bot
# FileName: app.py
# SoftWare: PyCharm
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.run(host="0.0.0.0")