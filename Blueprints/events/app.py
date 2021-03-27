import flask

addevent_bp = flask.Blueprint('addevent', __name__,
                              template_folder='templates',
                              static_folder='static')

calendar_bp = flask.Blueprint('calendar', __name__,
                              template_folder='templates',
                              static_folder='static')

@addevent_bp.route('/')
def addevent():
    return "Adding Event"

@calendar_bp.route('/')
def calendar():
    return "Creation of Calendar"