from .extensions import socketio
from flask import session
from .models import UserModel, UserStatistic
from .db import db

# Connet with socketIO save data to Dbase and to session


@socketio.on("user_join")
def handle_user_join(username):
    print(f"User {username} joined")
    user = UserModel(username=username)
    db.session.add(user)
    db.session.commit()
    session["id"] = user.id
    session["username"] = username
    session["points"] = user.points
    session["lifes"] = user.lifes
    if "board" in session:
        session.pop("board")

    # Statistic collecting initialize
    user_statistic = UserStatistic(user_id=user.id)
    user_statistic.start_session()
    db.session.add(user_statistic)
    db.session.commit()
    session["statistic_id"] = user_statistic.id


@socketio.on("user_exit")
def handle_user_exit():
    statistic_id = session.get("statistic_id")
    if statistic_id:
        user_statistic = UserStatistic.query.get(statistic_id)
        if user_statistic:
            user_statistic.end_session()
            db.session.commit()
            session.pop("statistic_id")
