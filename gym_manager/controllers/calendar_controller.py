from flask import Blueprint, Flask, redirect, render_template, request

calendar_blueprint = Blueprint("calendar", __name__)

# INDEX
@calendar_blueprint.route("/calendar")
def calendar():
    return render_template("calendar/index.html")