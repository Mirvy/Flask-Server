from flask import Blueprint

bp = Blueprint('rover', __name__)

from app.rover import routes