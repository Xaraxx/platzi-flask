from flask import render_template, session, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash

from app.forms import LoginForm
from app.firestore_service import get_user, create_new_user
from app.models import UserData, UserModel

from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict():
            password_from_db = user_doc.to_dict()['password']

            if password == password_from_db:
                user_data = UserData(username, password)
                user = UserModel(user_data)

                login_user(user)

                flash('Wellcome again!')

                redirect(url_for('hello'))

            else:
                flash('The username and the password doesn\'t match. Try again!')
            
        else:
            flash('Sorry, the user doesn\'t exist. Create your account!')

        return redirect(url_for('index'))

    return render_template('login.html', **context)


@auth.route('logout')
@login_required
def logout():
    # Let this line blank!
    logout_user()

    flash('Comeback soom!')
    return redirect(url_for('auth.login'))



@auth.route('signup', methods=['GET', 'POST'])
def signup():
    signup_form = LoginForm()
    context = {
        'signup_form' : signup_form
    }
    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        user_doc = get_user(username)

        if not user_doc.to_dict():
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash)
            create_new_user(user_data)
            
            user = UserModel(user_data)

            login_user(user)
            flash('Welcome.')

            return redirect(url_for('hello'))

        else:
            flash('The user already exist!')


    return render_template('signup.html', **context)


