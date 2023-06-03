from flask import render_template, session, request, redirect, url_for

from flask_smorest import Blueprint
from flask.views import MethodView
from tic_tac_toe.board_logic.ai_best_move import get_best_move

from tic_tac_toe.models import UserModel, UserStatistic

from tic_tac_toe.board_logic import check_win
from tic_tac_toe.board_logic import userPoints


blp = Blueprint("Board", __name__, description="Operations   on board")


@blp.route("/board")
class Board(MethodView):
    def get(self):
        # session.pop("board")
        # # del session["user_id"]

        # Checking is user logged to session if not redirect to login
        if "id" not in session:
            return redirect("/")

        # Assign specific user in session
        user = UserModel.query.get_or_404(
                session.get("id"))

        # If board doesn't exist in session create it
        if "board" not in session:
            session["board"] = [
                [None, None, None],
                [None, None, None],
                [None, None, None]
                ]
            session["game_over"] = False

            # Dummy functionality than User always play X
            session["turn"] = "X"

            # Checking is user be able to still playing
            userPoints(user)

            if not session["game_over"]:
                # Taking 3 points for game
                user.decrement_points(3)

        # Setting flag to template
        show_win_message = request.args.get("show_win_message", default=False)
        show_lose_message = request.args.get(
            "show_lose_message",
            default=False
            )
        show_draw_message = request.args.get(
            "show_draw_message",
            default=False
            )

        return render_template(
                        "board.html",
                        board=session["board"],
                        turn=session["turn"],
                        username=user.username,
                        user_points=user.points if user else 0,
                        user_lifes=user.lifes if user else 0,
                        game_over=session["game_over"],
                        show_win_message=show_win_message,
                        show_lose_message=show_lose_message,
                        show_draw_message=show_draw_message,
                        )

    def post(self):
        row = int(request.form.get("row"))
        col = int(request.form.get("col"))
        board = session["board"]
        user = UserModel.query.get_or_404(
                session.get("id"))

        # Assign specific user statistic collecting model
        user_statistic = UserStatistic.query.get_or_404(
            session.get("statistic_id"))

        if board[row][col] is None:
            board[row][col] = session["turn"]

        # Checking winning logic
        if check_win(board):

            # User winning logic
            if session["turn"] == "X":
                if user:
                    user.increment_points(4)
                    user_statistic.increment_wins(1)
                    session.pop("board")
                    return redirect(
                        url_for("Board.Board",
                                show_win_message="True"),
                        )
                else:
                    # Basic error handler
                    raise ValueError("User doesn't exist!")
            else:
                # User losing logic
                userPoints(user)
                user_statistic.increment_loses(1)
                session.pop("board")
                return redirect(
                    url_for("Board.Board",
                            show_lose_message="True"),
                    )

        elif all(cell is not None for row in board for cell in row):
            # Draw logic
            user_statistic.increment_draws(1)
            session.pop("board")
            return redirect(
                            url_for("Board.Board", show_draw_message="True")
                            )
        else:
            # Switch the turn
            session["turn"] = "O" if session["turn"] == "X" else "X"
            # AI Plays INFINITE logic
            if session["turn"] == "O":
                best_move = get_best_move(board)
                if best_move:
                    row, col = best_move
                    board[row][col] = "O"
                    # AI win logic
                    if check_win(board):
                        userPoints(user)
                        user_statistic.increment_loses(1)
                        session.pop("board")
                        return redirect(
                            url_for("Board.Board", show_lose_message="True")
                            )
                    elif all(
                            cell is not None for row in board for cell in row):
                        user_statistic.increment_draws(1)
                        session.pop("board")
                        return redirect(
                            url_for("Board.Board", show_draw_message="True")
                            )
                    else:
                        session["turn"] = "X"
        return redirect(url_for("Board.Board"))
