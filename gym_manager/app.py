from flask import Flask, render_template
# from controllers.booking_controller import booking_blueprint
# from controllers.member_controller import member_blueprint
# from controllers.class_controller import class_blueprint
# from controllers.coach_controller import coach_blueprint

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
