import flask
from flask import Blueprint, render_template

ridhima_bp = Blueprint('ridhima', __name__,
                              template_folder='templates',
                              static_folder='static')
#make sure to add your blueprints underneath mine

sriya_bp = Blueprint('sriya', __name__,
                           template_folder='templates',
                           static_folder='static')

isai_bp = Blueprint('isai', __name__,
                              template_folder='templates',
                              static_folder='static')

grace_bp = Blueprint('grace_bp', __name__,
                          template_folder='templates',
                          static_folder='static')

iniyaa_bp = Blueprint('iniyaa', __name__,
                          template_folder='templates',
                          static_folder='static')



@ridhima_bp.route('/')
def ridhima():
    return "Ridhima's MiniLab"

@sriya_bp.route('/')
def sriya():
    return "Sriya's MiniLab"

@isai_bp.route('/')
def isai():
    return "Isai's MiniLab"

@grace_bp.route('/minilabs')
@grace_bp.route('/')
def grace():
    return render_template("grace-minilab.html")

@iniyaa_bp.route('/')
def iniyaa():
    return "Iniyaa's MiniLab"

