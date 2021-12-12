from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)


# NEW
@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html")


# CREATE
@members_blueprint.route("/members", methods=["POST"])
def create_member():
    name = request.form["name"]
    membership = request.form["membership"]
    new_member = Member(name, membership)
    member_repository.save(new_member)
    return redirect("/members")


# EDIT
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member=member)


# UPDATE
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    name = request.form["name"]
    membership = request.form["membership"]
    member = Member(name, membership, id)
    member_repository.update(member)
    return redirect("/members")


# DELETE
@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")