# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template

#create a Flask instance
app = Flask(__name__)



#connects default URL of server to a python function
@app.route('/')
@app.route('/home')
def home():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("home.html")

@app.route('/home2')
def home2():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("home2.html")


@app.route('/about')
def about():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("about_us.html")

@app.route('/cal')
def cal():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("cal.html")

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port='8080')  # main run engine of website



