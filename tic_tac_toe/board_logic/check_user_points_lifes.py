from flask import flash, session

"""Basic implementation of user.points logic"""


def userPoints(user):
    if user.points < 3:
        if user.lifes + user.points < 3:
            flash("Nie ma wystarczającej ilości \
                  punktów i żyć na kolejną grę")
            session["game_over"] = True

        else:
            user_life_needed = 3 - user.points
            user.decrement_lifes(user_life_needed)
            user.increment_points(user_life_needed)


if __name__ == "__main__":
    userPoints()
