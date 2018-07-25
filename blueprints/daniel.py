import docker
from flask import Blueprint, render_template, redirect, session, current_app

pocker = Blueprint('pocker', __name__, url_prefix='/docker')
dc = docker.DockerClient('tcp://192.168.200:2376')

# c = dc.containers.get('flask-app')

@pocker.route('')
def home():
    if not session.get('auth'):
        current_app.logger.warning('Acesso não autorizado!!!!')
        return redirect('/')
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