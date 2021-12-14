from flask import Blueprint, Flask, redirect, render_template, request
from controllers.members_controller import members

from models.gymclass import GymClass
import repositories.gym_class_repository as gym_class_repository
import repositories.coach_repository as coach_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

# INDEX
@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all()
    coaches = coach_repository.select_all()
    return render_template("gym_classes/index.html", gym_classes=gym_classes, coaches = coaches)


# SHOW
@gym_classes_blueprint.route("/gym_classes/<id>")
def show_gym_class(id):
    members = gym_class_repository.select_victims_of_gym_class(id)
    gym_class = gym_class_repository.select(id)
    return render_template("gym_classes/show.html", members=members, gym_class=gym_class)


# NEW
@gym_classes_blueprint.route("/gym_classes/new")
def new_gym_class():
    coaches = coach_repository.select_all()
    return render_template("gym_classes/new.html", coaches=coaches)

# CREATE
@gym_classes_blueprint.route("/gym_classes", methods=["POST"])
def create_gym_class():
    title = request.form["title"]
    sport = request.form["sport"]
    coach_id = request.form["coach_id"]
    coach = coach_repository.select(coach_id)
    capacity = request.form["capacity"]
    date = str(request.form["date"])
    start_time = str(request.form["start_time"])
    end_time = str(request.form["end_time"])
    new_gym_class = GymClass(title, sport, capacity, coach, date, start_time, end_time)
    gym_class_repository.save(new_gym_class)
    return redirect("/gym_classes")


# EDIT
@gym_classes_blueprint.route("/gym_classes/<id>/edit")
def edit_gym_class(id):
    gym_class = gym_class_repository.select(id)
    coaches = coach_repository.select_all()
    return render_template('gym_classes/edit.html', gym_class=gym_class, coaches=coaches)


# UPDATE
@gym_classes_blueprint.route("/gym_classes/<id>", methods=["POST"])
def update_gym_class(id):
    title = request.form["title"]
    sport = request.form["sport"]
    coach_id = request.form["coach_id"]
    coach = coach_repository.select(coach_id)
    capacity = request.form["capacity"]
    date = str(request.form["date"])
    start_time = str(request.form["start_time"])
    end_time = str(request.form["end_time"])
    gym_class = GymClass(title, sport, capacity, coach, date, start_time, end_time, id)
    gym_class_repository.update(gym_class)
    return redirect("/gym_classes")


# DELETE
@gym_classes_blueprint.route("/gym_classes/<id>/delete", methods=["POST"])
def delete_gym_class(id):
    gym_class_repository.delete(id)
    return redirect("/gym_classes")