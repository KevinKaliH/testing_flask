from flask import Blueprint
importation_bp = Blueprint('importation_bp', __name__, url_prefix='/importation')

from . import routes