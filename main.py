from flask import request, make_response, redirect, render_template, session, url_for, flash, get_flashed_messages

import unittest

from flask_bootstrap import Bootstrap

from app import create_app
from app.forms import LoginForm
from app.firestore_service import get_users

app = create_app()


things_to_do = ['Buy coffee', 'Send requirenment', 'Deliver a video']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(500)
def internal_server(error):
    return render_template('500.html', error=error)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello/'))
    session['user_ip'] = user_ip
    # response.set_cookie('user_ip', user_ip)
    return response


@app.route('/hello/', methods=['GET'])
def hello():
    user_ip = session.get('user_ip')
    username = session.get('username')
    context = {
         'user_ip': user_ip, 
         'things_to_do': things_to_do,
         'username': username
    }
    
    users = get_users()

    for user in users:
        print(user.id)
        print(user.to_dict()['password'])

    return render_template('hello.html', **context)



