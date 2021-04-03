import flask
from flask import Flask, Blueprint, render_template



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

grace_bp = flask.Blueprint('grace', __name__,
                          template_folder='templates',
                          static_folder='static')

iniyaa_bp = flask.Blueprint('iniyaa', __name__,
                          template_folder='templates',
                          static_folder='static')



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


@grace_bp.route('/')
def grace():
    return "Grace's MiniLab"

@iniyaa_bp.route('/')
def iniyaa():
    return "Iniyaa's MiniLab"

