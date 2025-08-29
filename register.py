from flask import Blueprint, request, render_template_string

register_bp = Blueprint("register", __name__)

users = {}

register_form = """
<h2>Register</h2>
<form method="post">
  <input type="text" name="username" placeholder="Username" required><br><br>
  <input type="password" name="password" placeholder="Password" required><br><br>
  <button type="submit">Register</button>
</form>
"""

@register_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Accept both HTML form and Postman JSON
        username = request.form.get("username") or (request.json.get("username") if request.is_json else None)
        password = request.form.get("password") or (request.json.get("password") if request.is_json else None)

        if not username or not password:
            return {"error": "Username and password required"}, 400

        if username in users:
            return {"error": "User already exists"}, 400

        users[username] = password
        return f"<h3>User {username} registered successfully ✅</h3><a href='/login'>Go to Login</a>"

    return register_form
