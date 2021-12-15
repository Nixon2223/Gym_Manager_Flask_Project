from flask import Blueprint, Flask, redirect, render_template, request
from repositories.coach_repository import select_all

import repositories.member_repository as member_repository

stats_blueprint = Blueprint("stats", __name__)


@stats_blueprint.route("/stats")
def stats():
    standard_members = len(member_repository.select_standard())
    deactivated_members = len(member_repository.select_deactivated())
    premium_members = len(member_repository.select_premium())
    return render_template("stats/index.html", premium_members = premium_members, standard_members = standard_members, deactivated_members = deactivated_members)