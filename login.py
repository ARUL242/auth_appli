from flask import Blueprint, request, render_template_string
import jwt, datetime

login_bp = Blueprint("login", __name__)
SECRET_KEY = "supersecretkey"

login_form = """
<h2>Login</h2>
<form method="post">
  <input type="text" name="username" placeholder="Username" required><br><br>
  <input type="password" name="password" placeholder="Password" required><br><br>
  <button type="submit">Login</button>
</form>
"""

# Import users from register.py
from regis import users  

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # HTML form or Postman form-data
        username = request.form.get("username") or request.json.get("username")
        password = request.form.get("password") or request.json.get("password")

        if not username or not password:
            return {"error": "Missing credentials"}, 400

        if username not in users or users[username] != password:
            return {"error": "Invalid username or password"}, 401

        # Create JWT token
        token = jwt.encode(
            {"user": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            SECRET_KEY,
            algorithm="HS256"
        )

        return {"message": "Login successful", "token": token}
    
    return render_template_string(login_form)
