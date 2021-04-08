from flask import Flask, Blueprint, render_template, request
from minilab.grace import Addition


#app = Flask(__name__)


minilab_bp = Blueprint('minilab', __name__,
                       template_folder='templates',
                       static_folder='static', static_url_path='assets')


@minilab_bp.route('/addition', methods=["GET", "POST"])
def grace():
    if request.form:
        return render_template("minilab/grace-minilab.html", addition=Addition(int(request.form.get("series"))))
    return render_template("minilab/grace-minilab.html", addition=Addition(2))


