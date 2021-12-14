from flask import Blueprint, Flask, redirect, render_template, request

import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository

calendar_blueprint = Blueprint("calendar", __name__)

# INDEX
@calendar_blueprint.route("/calendar")
def calendar():
    all_gym_classes = gym_class_repository.select_all()
    list_of_days = []
    for gym_class in all_gym_classes:
        list_of_days.append(str(gym_class.date)[8:])
    return render_template("calendar/index.html", list_of_days = list_of_days)

#VIEW DAY
@calendar_blueprint.route("/calendar/<day>")
def calendar_get_day(day):
    all_gym_classes = gym_class_repository.select_all()
    gym_classes = []
    for gym_class in all_gym_classes:
        if str(gym_class.date)[8:] == day:
            gym_classes.append(gym_class)
    all_members = member_repository.select_all()
    return render_template("calendar/day.html", day = day, gym_classes = gym_classes, members = all_members)

#VIEW CLASS
@calendar_blueprint.route("/calendar/class/<id>")
def calendar_get_class(id):
    num_booked_in =len(gym_class_repository.select_members_of_gym_class(id))
    all_members = member_repository.select_all()
    gym_class = gym_class_repository.select(id)
    booked_in_members = []
    for member in gym_class_repository.select_members_of_gym_class(id):
        booked_in_members.append(member)
    booked_in = []
    for member in gym_class_repository.select_members_of_gym_class(id):
        booked_in.append(member.id)
    return render_template("calendar/class.html", gym_class = gym_class, booked_in = booked_in, members = all_members, booked_in_members = booked_in_members, num_booked_in = num_booked_in)