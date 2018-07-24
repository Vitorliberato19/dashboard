import requests
from flask import Blueprint, render_template

gitlab = Blueprint('gitlab', __name__, url_prefix='/gitlab')

TOKEN = 'Y3jgjt-mdLKszrnQsSic'
GITLAB = 'http://192.168.0.100/api/v4/{route}?private_token={tk}'

@gitlab.route('')
def home_():
    users = requests.get(GITLAB.format(tk=TOKEN, route='users'))
    projects = requests.get(GITLAB.format(tk=TOKEN, route='projects'))
    return render_template('gitlab.html', users=users.json(), projects = projects.json())


