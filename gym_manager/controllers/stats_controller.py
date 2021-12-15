from flask import Blueprint, Flask, redirect, render_template, request
from repositories.coach_repository import select_all

import repositories.member_repository as member_repository

stats_blueprint = Blueprint("stats", __name__)


@stats_blueprint.route("/stats")
def stats():
    all_members = member_repository.select_all()
    
    return render_template("stats/index.html")