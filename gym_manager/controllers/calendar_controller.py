from flask import Blueprint, Flask, redirect, render_template, request

calendar_blueprint = Blueprint("calendar", __name__)

# INDEX
@calendar_blueprint.route("/calendar")
def calendar():
    return render_template("calendar/index.html")

@calendar_blueprint.route("/calendar/<day>")
def calendar_get_day(day):
    
    return render_template("calendar/<day>index.html", day=day)