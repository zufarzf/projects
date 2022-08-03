from flask import Blueprint

errors = Blueprint(
                    'errors', __name__,
                    template_folder='errors-templates',
                    static_folder='errors-static'
                )

from . import views