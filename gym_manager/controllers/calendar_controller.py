from flask import Blueprint, Flask, redirect, render_template, request

import repositories.gym_class_repository as gym_class_repository

calendar_blueprint = Blueprint("calendar", __name__)

# INDEX
@calendar_blueprint.route("/calendar")
def calendar():
    return render_template("calendar/index.html")

@calendar_blueprint.route("/calendar/<day>")
def calendar_get_day(day):
    all_gym_classes = gym_class_repository.select_all()
    gym_classes = []
    for gym_class in all_gym_classes:
        if str(gym_class.date)[5:-3] == day:
            gym_classes.append(gym_class)
    return render_template("calendar/day.html", day = day, gym_classes = gym_classes)