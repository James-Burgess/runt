from os import getenv

from runt.config import tasks
from runt.server import app
from runt.task_manager import ViewCreator


@app.route("/")
def index():
    """
    List all the available apps to trigger (public).
    """
    return "<br>".join([task["route"] for task in tasks])


"""
Create all the routes for the apps (protected).
"""
views = ViewCreator(tasks)
for task in tasks:
    app.add_url_rule(task["route"], task["name"], methods=["POST"])
    app.view_functions[task["name"]] = getattr(views, task["name"])

def run():
    app.run(host="0.0.0.0", port=getenv("PORT", 8080))
