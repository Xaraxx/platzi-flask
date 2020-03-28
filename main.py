import unittest

from flask import request, make_response, redirect, render_template, session, url_for, flash, get_flashed_messages

from flask_bootstrap import Bootstrap
from flask_login import login_required, current_user

from app import create_app
from app.forms import ThingsToDoForm
from app.firestore_service import get_users, get_things_to_do

app = create_app()

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
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    things_to_do_form = ThingsToDoForm()
    context = {
         'user_ip': user_ip, 
         'things_to_do': get_things_to_do(user_id=username),
         'username': username,
         'things_to_do_form': things_to_do_form
    }
    
    return render_template('hello.html', **context)



