from flask import Flask, request, make_response, redirect, render_template

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRET'

things_to_do = ['Buy coffee', 'Send requirenment', 'Deliver a video']

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit   = SubmitField('Submit')

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


@app.route('/hello/')
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    context = {
         'user_ip': user_ip, 
         'things_to_do': things_to_do,
         'login_form': login_form
    }
    
    return render_template('hello.html', **context)
