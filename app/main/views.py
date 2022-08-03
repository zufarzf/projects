from flask import render_template, url_for, request, flash, session
from . import main


@main.route('/')
def main_page():
    return render_template('base.html', title='HFood')

@main.route('/<string:catalog_name>')
def eat_list(catalog_name):
    return render_template('list__content.html', title=catalog_name)