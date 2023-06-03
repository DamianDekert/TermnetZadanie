from tic_tac_toe.db import db
import datetime


class UserStatistic(db.Model):
    __tablename__ = "statistics"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    draws = db.Column(db.Integer, default=0)
    date = db.Column(db.Date, default=datetime.date.today)
    session_duration = db.Column(db.Interval)

    user = db.relationship(
        "UserModel", back_populates="statistic")

    def increment_wins(self, value):
        self.wins += value
        db.session.commit()

    def increment_loses(self, value):
        self.losses += value
        db.session.commit()

    def increment_draws(self, value):
        self.draws += value
        db.session.commit()

    def start_session(self):
        self.session_start_time = datetime.datetime.now()

    def end_session(self):
        session_end_time = datetime.datetime.now()
        session_duration = session_end_time - self.session_start_time
        self.session_duration = session_duration
        db.session.commit()
