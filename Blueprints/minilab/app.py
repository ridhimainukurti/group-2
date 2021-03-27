from flask import Blueprint

ridhima_bp = flask.Blueprint('trending', __name__,
                              template_folder='templates',
                              static_folder='static')



@ridhima_bp.route('/')
def ridhima():
    return "Ridhima's MiniLab"

