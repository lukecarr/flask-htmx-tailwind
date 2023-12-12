import os

from flask import Flask, render_template
from flask_assets import Environment
from webassets import Bundle

app = Flask(__name__)

assets = Environment(app)

js = Bundle("./../node_modules/htmx.org/dist/htmx.min.js", output="gen/bundle.js")
css = Bundle("./../dist/index.css", output="gen/bundle.css")

assets.register({"js": js, "css": css})


@app.route("/")
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route("/button", methods=["POST"])
def button_clicked():
    return render_template("button.html")


def run_debug_server():
    from livereload import Server

    app.debug = True
    assets.auto_build = True

    server = Server(app.wsgi_app)
    server.watch("templates")
    server.watch("dist/index.css")
    server.serve(port=5000)


if __name__ == '__main__':
    if os.environ.get("FLASK_DEBUG") == "1":
        run_debug_server()
    else:
        app.run(port=5000)
