from flask import Blueprint, Flask, redirect, render_template, request

from models.coach import Coach
import repositories.coach_repository as coach_repository

coaches_blueprint = Blueprint("coaches", __name__)

# INDEX
@coaches_blueprint.route("/coaches")
def coaches():
    coaches = coach_repository.select_all()
    return render_template("coaches/index.html", coaches=coaches)


# NEW
@coaches_blueprint.route("/coaches/new")
def new_coach():
    return render_template("coaches/new.html")


# CREATE
@coaches_blueprint.route("/coaches", methods=["POST"])
def create_coach():
    name = request.form["name"]
    new_coach = Coach(name)
    coach_repository.save(new_coach)
    return redirect("/coaches")


# EDIT
@coaches_blueprint.route("/coaches/<id>/edit")
def edit_coach(id):
    coach = coach_repository.select(id)
    return render_template('coaches/edit.html', coach=coach)


# UPDATE
@coaches_blueprint.route("/coaches/<id>", methods=["POST"])
def update_coach(id):
    name = request.form["name"]
    coach = Coach(name, id)
    coach_repository.update(coach)
    return redirect("/coaches")


# DELETE
@coaches_blueprint.route("/coaches/<id>/delete", methods=["POST"])
def delete_coach(id):
    coach_repository.delete(id)
    return redirect("/coaches")