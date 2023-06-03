from flask import render_template

from sqlalchemy import func

import datetime
from flask_smorest import Blueprint
from flask.views import MethodView
from tic_tac_toe.db import db
from tic_tac_toe.models import UserStatistic

blp = Blueprint(
    "Statistic", __name__, description="Statistic view")


@blp.route("/statistics")
class UsersStatistic(MethodView):
    def get(self):
        today = datetime.date.today()

        data = db.session.query(
            func.sum(UserStatistic.wins).label("total_wins"),
            func.sum(UserStatistic.losses).label("total_losses"),
            func.sum(UserStatistic.draws).label("total_draws"),
        ).filter(UserStatistic.date == today).first()

        total_wins = data.total_wins
        total_losses = data.total_losses
        total_draws = data.total_draws

        return render_template(
            "statistics.html",
            total_wins=total_wins,
            total_losses=total_losses,
            total_draws=total_draws,
            today=today,
            )
