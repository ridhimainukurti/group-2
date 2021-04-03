from flask import Blueprint, render_template, request
from minilab.ridhima import Exponential
from minilab.isai import Factorial


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

@minilab_bp.route('/isai', methods=["GET", "POST"])
def isai():
    if request.form:
        return render_template("/minilab/isai.html", factorial = Factorial (int(request.form.get("series"))))
    return render_template("/minilab/isai.html", factorial= Factorial(2))



