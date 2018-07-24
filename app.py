#!/usr/bin/python3

from flask import Flask, render_template
from blueprints.daniel import pocker
from blueprints.jk import jk
from blueprints.gitlab import gitlab

app = Flask(__name__)
app.register_blueprint(pocker)
app.register_blueprint(jk)
app.register_blueprint(gitlab)

@app.route('/')
def home():
    return render_template('index.html')

app.run(debug=True)