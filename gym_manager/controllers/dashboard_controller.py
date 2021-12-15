from flask import Blueprint, Flask, redirect, render_template, request
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

dashboard_blueprint = Blueprint("dashboard", __name__)

# INDEX
@dashboard_blueprint.route("/")
def dashboard():
    standard_members = len(member_repository.select_standard())
    deactivated_members = len(member_repository.select_deactivated())
    premium_members = len(member_repository.select_premium())
    return render_template("dashboard/index.html", premium_members = premium_members, standard_members = standard_members, deactivated_members = deactivated_members)