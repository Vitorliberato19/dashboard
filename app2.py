#!/usr/bin/python3
from hashlib import md5
from binascii import b2a_base64
from ldap3 import Server, Connection


from flask import Flask, render_template, request, session, redirect
from blueprints.daniel import pocker
from blueprints.jk import jk
from blueprints.gitlab import gitlab

app = Flask(__name__)
app.secret_key = '4linux'
app.register_blueprint(pocker)
app.register_blueprint(jk)
app.register_blueprint(gitlab)

@app.route('/')
def home():
    if session.get('auth'):
        return redirect('/docker')
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    # print(request.form)
    mail = request.form['email']
    password = request.form['password']
    server = Server('ldap://192.168.0.200:389')
    ldap = Connection(server, 'mail=' + mail + ',dc=dexter,dc=com,dc=br', password)
    if ldap.bind():
        session['auth'] = True
        return redirect('/docker')
    else:
        return redirect('')

@app.route('/logoff')
def logoff():
    if session.get('auth'):
        del session['auth']
    return redirect('/')

app.run(debug=True)