from flask import Flask, render_template
# from controllers.booking_controller import booking_blueprint
from controllers.members_controller import members_blueprint
# from controllers.class_controller import class_blueprint
# from controllers.coach_controller import coach_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
