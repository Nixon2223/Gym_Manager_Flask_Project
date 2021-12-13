from flask import Flask, render_template
# from controllers.booking_controller import booking_blueprint
from controllers.members_controller import members_blueprint
from controllers.gym_classes_controller import gym_classes_blueprint
from controllers.coaches_controller import coaches_blueprint
from controllers.calendar_controller import calendar_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(coaches_blueprint)
app.register_blueprint(gym_classes_blueprint)
app.register_blueprint(calendar_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
