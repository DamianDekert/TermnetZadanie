from flask import render_template

from flask_smorest import Blueprint
from flask.views import MethodView

blp = Blueprint("Main", __name__, description="Starting main section, \
                 user can pass username")


@blp.route("/")
class UsernamePass(MethodView):
    def get(self):
        return render_template("main.html")
