import docker
from flask import Blueprint, render_template, redirect

pocker = Blueprint('pocker', __name__, url_prefix='/docker')
dc = docker.DockerClient('tcp://192.168.200:2376')

# c = dc.containers.get('flask-app')

@pocker.route('')
def home():
    c = dc.containers.get('flask-app')
    return render_template('docker.html',container=c)


@pocker.route('/start')
def inicia():
    c = dc.containers.get('flask-app')
    c.start()
    return redirect('/docker')

@pocker.route('/stop')
def termina():
    c = dc.containers.get('flask-app')    
    c.stop()
    return redirect('/docker')