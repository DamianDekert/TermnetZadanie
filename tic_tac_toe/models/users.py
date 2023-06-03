from tic_tac_toe.db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    points = db.Column(db.Integer, default=0)
    lifes = db.Column(db.Integer, default=10)
    statistic = db.relationship(
        "UserStatistic", uselist=False, back_populates="user")

    def increment_points(self, points):
        self.points += points
        db.session.commit()

    def decrement_points(self, points):
        self.points -= points
        db.session.commit()

    def decrement_lifes(self, lifes):
        self.lifes -= lifes
        db.session.commit()
