from utils.api import app
from utils.config import tasks
from utils.task_manager import ViewCreator
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


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


app.run(host="0.0.0.0", port=8080)
