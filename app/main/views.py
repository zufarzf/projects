from flask import render_template, url_for, request, flash, session, redirect
from . import main
from .forms import LoginUser
from ..dbModels import StaffInstitution
from werkzeug.security import generate_password_hash, check_password_hash

methods=["GET", "POST"]

@main.route('/Log in', methods=methods)
def login_user():

    form = LoginUser()

    if form.validate_on_submit():
        staff = StaffInstitution().query.filter_by(name=form.name.data).first()
        
        if staff != None:
            if check_password_hash(staff.password, form.password.data):
                return redirect(url_for('admin.admin_panel'))
            else:
                flash("Не правильный пароль!", category='invalide_message')
                return redirect(url_for('main.login_user'))

        else:
            flash("Не правильное имя пользователя!", category='invalide_message')
            return redirect(url_for('main.login_user'))

    return render_template(
        'login_user.html', title='Авторизация',
        form=form
    )

@main.route('/')
def main_page():
    return render_template('main_page.html', title='HFood')

@main.route('/<string:catalog_name>')
def eat_list(catalog_name):
    return render_template('list__content.html', title=catalog_name)