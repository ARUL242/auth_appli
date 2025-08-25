from flask import Blueprint, request, render_template_string

register_bp = Blueprint("register", __name__)

# Temporary storage (in-memory dict instead of DB)
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
        # From HTML form
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return {"error": "Username and password required"}, 400

        if username in users:
            return {"error": "User already exists"}, 400

        users[username] = password
        return {"message": f"User {username} registered successfully"}
    
    # For browser access
    return render_template_string(register_form)
