from flask import Blueprint
agora = Blueprint('agora', '__init__')

from . import app  # isort:skip