from flask import Blueprint, Flask, redirect, render_template, request

import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository

calendar_blueprint = Blueprint("calendar", __name__)

# INDEX
@calendar_blueprint.route("/calendar")
def calendar():
    return render_template("calendar/index.html")

#VIEW DAY
@calendar_blueprint.route("/calendar/<day>")
def calendar_get_day(day):
    all_members = member_repository.select_all()
    all_gym_classes = gym_class_repository.select_all()
    gym_classes = []
    for gym_class in all_gym_classes:
        if str(gym_class.date)[8:] == day:
            gym_classes.append(gym_class)
    return render_template("calendar/day.html", day = day, gym_classes = gym_classes, members = all_members)