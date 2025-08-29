from flask import Blueprint, request, render_template_string, session
import jwt, datetime
from register import users

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

token_template = """
<h2>Login Successful ✅</h2>
<p><b>JWT Token:</b></p>
<textarea rows="4" cols="80">{{ token }}</textarea>
<br><br>
<a href="/protected" target="_blank">Go to Protected Route</a>
"""

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Accept both HTML form and Postman JSON
        username = request.form.get("username") or (request.json.get("username") if request.is_json else None)
        password = request.form.get("password") or (request.json.get("password") if request.is_json else None)

        if not username or not password:
            return {"error": "Username and password required"}, 400

        if username not in users or users[username] != password:
            return {"error": "Invalid username or password"}, 401

        token = jwt.encode(
            {"user": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            SECRET_KEY,
            algorithm="HS256"
        )

        session["token"] = token
        return render_template_string(token_template, token=token)

    return login_form
