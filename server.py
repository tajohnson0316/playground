from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def landing():
    return render_template("index.html", square_color="cornflowerblue", total_squares=0)


@application.route("/play")
def play():
    return render_template("index.html", square_color="cornflowerblue", total_squares=3)


@application.route("/play/<int:total_squares>")
def play_with_amount(total_squares):
    return render_template(
        "index.html", square_color="cornflowerblue", total_squares=total_squares
    )


@application.route("/play/<int:total_squares>/<string:square_color>")
def play_with_color(total_squares, square_color):
    return render_template(
        "index.html", square_color=square_color, total_squares=total_squares
    )


if __name__ == "__main__":
    application.run(debug=True, port=5000)
