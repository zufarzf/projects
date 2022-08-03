from flask import render_template, url_for, request, flash, session
from . import main
from .forms import LoginUser
from ..dbModels import Institution

methods=["GET", "POST"]

@main.route('/Log in', methods=methods)
def login_user():

    form = LoginUser()

    if form.validate_on_submit():
        pass

    return render_template(
        'login_user.html'
    )

@main.route('/')
def main_page():
    return render_template('main_page.html', title='HFood')

@main.route('/<string:catalog_name>')
def eat_list(catalog_name):
    return render_template('list__content.html', title=catalog_name)