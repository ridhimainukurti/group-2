import flask
from flask import Flask, Blueprint, render_template, request
from Blueprints.minilab.ridhima_bp import Exponential



minilab_bp = Blueprint('minilab',  __name__,
                       template_folder='templates',
                       static_folder='static')
"""
ridhima_bp = flask.Blueprint('ridhima', __name__,
                              template_folder='templates',
                              static_folder='static')
#make sure to add your blueprints underneath mine

sriya_bp = flask.Blueprint('sriya', __name__,
                           template_folder='templates',
                           static_folder='static')

isai_bp = flask.Blueprint('isai', __name__,
                              template_folder='templates',
                              static_folder='static')

grace_bp = flask.Blueprint('blueprint.grace_bp', __name__,
                          template_folder='templates',
                          static_folder='static')

iniyaa_bp = flask.Blueprint('iniyaa', __name__,
                          template_folder='templates',
                          static_folder='static')
"""
@minilab_bp.route('/')
def minilab():
    return "P4-Walruses Minilabs"

@minilab_bp.route('/ridhima', methods=["GET", "POST"])
def ridhima_bp():
    if request.form:
        return render_template("minilab/ridhima.html", fibonacci = Exponential(int(request.form.get("series"))))
    return render_template("minilab/ridhima.html", fibonacci= Exponential(2))

"""
@ridhima_bp.route('/')
def ridhima():
    return "Ridhima's MiniLab"

@sriya_bp.route('/')
def sriya():
    return "Sriya's MiniLab"

@isai_bp.route('/factorial', methods= ["GET", "POST"])
def factorial():
    if request.form:
        return render_template("isai.html", factorial=Factorial(int(request.form.get("series"))))
    return render_template("/template/isai.html", factorial=Factorial(2))

@minilab_bp.route('/sriya')
def sriya_minilab():
    return render_template("/Blueprints/minilabs/sriya_factorial_templates/sriya_bp.html")


@grace_bp.route('/')
def grace():
    return render_template("grace.html")
    return "Grace's MiniLab"

@iniyaa_bp.route('/')
def iniyaa():
    return "Iniyaa's MiniLab"
"""

