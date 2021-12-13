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
    return render_template("gym_classes/index.html", gym_classes=gym_classes)


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
    name = request.form["name"]
    coach_id = request.form["coach_id"]
    coach = coach_repository.select(coach_id)
    new_gym_class = GymClass(name, coach)
    gym_class_repository.save(new_gym_class)
    return redirect("/gym_classes")


# EDIT
@gym_classes_blueprint.route("/gym_classes/<id>/edit")
def edit_gym_class(id):
    gym_class = gym_class_repository.select(id)
    coach = coach_repository.select_all()
    return render_template('gym_classes/edit.html', gym_class=gym_class, coach=coach)


# UPDATE
@gym_classes_blueprint.route("/gym_classes/<id>", methods=["POST"])
def update_gym_class(id):
    name = request.form["name"]
    coach_id = request.form["coach_id"]
    coach = coach_repository.select(coach_id)
    gym_class = GymClass(name, coach, id)
    gym_class_repository.update(gym_class)
    return redirect("/gym_classes")


# DELETE
@gym_classes_blueprint.route("/gym_classes/<id>/delete", methods=["POST"])
def delete_gym_class(id):
    gym_class_repository.delete(id)
    return redirect("/gym_classes")