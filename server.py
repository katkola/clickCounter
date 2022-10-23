from flask_app import app
from flask_app.controllers import surveyController
#name of the model should be plural, class is singular


if __name__ == "__main__":
    app.run(debug=True)