import jenkins
from flask import Blueprint, render_template

jk = Blueprint('jk', __name__, url_prefix='/jenkins')
jc = jenkins.Jenkins('http://192.168.0.200:8080')

# @jk.route('')
# def home():
#     return 'Jenkins!'


@jk.route('')
def home_():
    for job in jc.get_jobs():
        if job['name'] == 'pipeline':
            pipeline = job
            break
    else:
        pipeline = {'name':'Nenhum job encontrado', 'color':''}
    if pipeline['color'] == 'blue':
        pipeline['color'] = 'Construiu'
    else:
        pipeline['color'] = 'Falhou'
    return render_template('jenkins.html', job=pipeline)