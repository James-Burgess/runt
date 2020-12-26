import importlib
import inspect
from pathlib import Path

exclusions = ["__pycache__"]

paths = [
    path
    for path in Path("./tasks").iterdir()
    if path.is_dir() and path.name not in exclusions
]


def extract_task_data(path):
    name = path.name
    task_fn = importlib.import_module(f"tasks.{path.name}.task")
    args = inspect.getfullargspec(task_fn.run).args
    route = f"/api/v1/task/{name}"

    return {
        "name": name,
        "args": args,
        "fn": task_fn,
        "route": route,
    }


tasks = [extract_task_data(path) for path in paths]
