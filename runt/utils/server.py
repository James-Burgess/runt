from os import getenv

from flask import Flask
from flask_httpauth import HTTPTokenAuth


app = Flask(__name__)
auth = HTTPTokenAuth(scheme="token")


@auth.verify_token
def verify_token(token):
    if getenv("SERVER_KEY", "unsafe") == token:
        return "internal server"
