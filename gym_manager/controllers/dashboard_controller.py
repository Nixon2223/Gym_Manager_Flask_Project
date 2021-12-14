from flask import Blueprint, Flask, redirect, render_template, request
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

dashboard_blueprint = Blueprint("dashboard", __name__)

# INDEX
@dashboard_blueprint.route("/")
def dashboard():
    all_gym_classes = gym_class_repository.select_all()
    todays_classes = []
    for gym_class in all_gym_classes:
        if str(gym_class.date)[8:] == "16":
            todays_classes.append(gym_class)
    return render_template("dashboard/index.html", todays_classes = todays_classes)