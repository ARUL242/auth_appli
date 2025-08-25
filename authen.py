from flask import Blueprint, request
import jwt

auth_bp = Blueprint("auth", __name__)
SECRET_KEY = "supersecretkey"

@auth_bp.route("/protected", methods=["GET"])
def protected():
    token = request.headers.get("Authorization")

    if not token:
        return {"error": "Token missing"}, 401
    
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"message": "Access granted", "user": decoded["user"]}
    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}, 401
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}, 401
