from flask import Blueprint, render_template, current_app, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user
from flask_test.login_handler import authenticate
from flask_test.forms import LoginForm

mod = Blueprint('test', __name__, template_folder='templates')


@mod.route('/')
@login_required
def index():
    return render_template(
        'test/index.html',
        title='Flask Test'
    )


@mod.route('/users')
@login_required
def users():
    return render_template(
        'test/users.html',
        data=current_app.mongo.db.user.find()
    )


@mod.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        login_user(authenticate(form.username.data, form.password.data))
        return redirect(url_for('test.index'))

    else:
        flash('Please enter valid username/password', 'error')

    return render_template(
        'test/login.html',
        title='Login',
        form=form
    )


@mod.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('test.login'))
