# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
from Blueprints.minilab.app import minilab_bp

#create a Flask instance
app = Flask(__name__)
app.register_blueprint(minilab_bp, url_prefix='/Blueprints/minilab')



#connects default URL of server to a python function
@app.route('/')
@app.route('/home')
def home():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("home.html")

@app.route('/ridhima/')
def ridhima():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("/minilab/ridhima.html")
@app.route('/sriya_minilab')
def sriya_minilab():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("sriya_bp.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)
    #app.run(debug=True, port="5001", host="127.0.0.1")



