from flask import request

from .server import auth


class ViewCreator(object):
    def __init__(self, tasks):
        for task in tasks:
            name = task["name"]
            _method = self.make_method(task)
            setattr(self, name, _method)

    @staticmethod
    def make_method(task):
        """
        Generic api route to get required args and call fn.
        """

        @auth.login_required
        def _method(*args, **kwargs):
            args = {}
            for arg in task.get("args", []):
                try:
                    args[arg] = request.form[arg]
                except KeyError:
                    return f"{arg} was not provided"
            return task["fn"].run(**args)

        return _method
