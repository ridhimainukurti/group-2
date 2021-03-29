# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
from Blueprints.events.app import addevent_bp, calendar_bp
from Blueprints.minilab.app import ridhima_bp, sriya_bp, isai_bp, iniyaa_bp

#create a Flask instance
app = Flask(__name__)
app.register_blueprint(addevent_bp, url_prefix='/addevent')
app.register_blueprint(calendar_bp, url_prefix='/calendar')
app.register_blueprint(ridhima_bp, url_prefix='/ridhima')
app.register_blueprint(sriya_bp, url_prefix='/sriya')
app.register_blueprint(isai_bp, url_prefix='/isai')
app.register_blueprint(iniyaa_bp, url_prefix='/iniyaa')


#connects default URL of server to a python function
@app.route('/')
@app.route('/home')
def home():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("home.html")




if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)
    #app.run(debug=True, port="5001", host="127.0.0.1")
