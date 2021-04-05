from flask import Blueprint, render_template, request
from minilab.ridhima import Exponential
from minilab.isai import Factorial
from minilab.grace import numlist
from minilab.iniyaa import lucas


minilab_bp = Blueprint('minilab',  __name__,
                       template_folder='templates',
                       static_folder='static')

@minilab_bp.route('/')
def minilab():
    return ("P4-Walruses Minilabs")

@minilab_bp.route('/ridhima', methods=["GET", "POST"])
def ridhima():
    if request.form:
        return render_template("/minilab/ridhima.html", exponential = Exponential(int(request.form.get("series"))))
    return render_template("/minilab/ridhima.html", exponential= Exponential(2))

@minilab_bp.route('/sriya', methods=["GET", "POST"])
def sriya():
    if request.form:
        return render_template("/minilab/sriya_bp.html", factorial = Factorial(int(request.form.get("series"))))
    return render_template("/minilab/sriya_bp.html", factorial = Factorial(2))

@minilab_bp.route('/isai', methods=["GET", "POST"])
def isai():
    if request.form:
        return render_template("/minilab/isai.html", factorial = Factorial (int(request.form.get("series"))))
    return render_template("/minilab/isai.html", factorial= Factorial(2))
 
@minilab_bp.route('/iniyaa', methods=["GET", "POST"])
def iniyaa():
    if request.form:
        return render_template("/minilab/iniyaa.html", lucas = lucas (int(request.form.get("series"))))
    return render_template("/minilab/iniyaa.html", lucas= lucas(2))

@minilab_bp.route('/sriya', methods=["GET", "POST"])
def sriya():
    if request.form:
        return render_template("/minilab/isai.html", factorial = Factorial (int(request.form.get("series"))))
    return render_template("/minilab/sriya.html", factorial= Factorial(2))

@minilab_bp.route('/grace' , methods=['GET', 'POST'])
def grace():
    mean = 0
    mode = 0
    median = 0
    list = ""
    if request.method == 'POST':
        values = request.form['list']
        n = numlist()
        n.values2(values)
        mean = n.average()
        median = n.median()
        mode = n.mode()
        list = n.list()
    return render_template("/minilab/grace-minilab.html", mean=mean, median=median, mode=mode, list=list)
