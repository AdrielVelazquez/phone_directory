from flask.ext.api import FlaskAPI

app = FlaskAPI(__name__)
app.config.from_object('config')

from app import routes

from routes import quiz

app.register_blueprint(quiz)