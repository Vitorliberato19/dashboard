#!/usr/bin/python3

from flask import Flask, render_template
from blueprints.daniel import pocker

app = Flask(__name__)
app.register_blueprint(pocker)

@app.route('/')
def home():
    return render_template('index.html')


app.run(debug=True)
