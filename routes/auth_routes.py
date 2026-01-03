from sanic import Blueprint
from controllers.auth_controller import register, login

auth_bp = Blueprint("auth_bp")

auth_bp.route("/register", methods=["POST"])(register)
auth_bp.route("/login", methods=["POST"])(login)



