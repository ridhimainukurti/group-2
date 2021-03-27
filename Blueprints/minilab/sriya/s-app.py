import flask
from flask import Blueprint

sriya_bp = flask.Blueprint('trending', __name__,
                             template_folder='templates',
                             static_folder='static')



@sriya_bp.route('/')
def sriya():
    return "Sriya's MiniLab"