import flask
from flask import Blueprint

ridhima_bp = flask.Blueprint('trending', __name__,
                              template_folder='templates',
                              static_folder='static')
#make sure to add your blueprints underneath mine


@ridhima_bp.route('/')
def ridhima():
    return "Ridhima's MiniLab"

sriya_bp = flask.Blueprint('trending', __name__,
                             template_folder='templates',
                             static_folder='static')



@sriya_bp.route('/')
def sriya():
    return "Sriya's MiniLab"

