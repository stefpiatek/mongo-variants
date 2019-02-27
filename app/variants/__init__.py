from flask import Blueprint

variants = Blueprint("variants", __name__)

# at end to avoid circular references
from . import views
