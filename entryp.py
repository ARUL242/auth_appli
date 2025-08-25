from flask import Flask
from regis import register_bp
from login import login_bp
from authen import auth_bp

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for JWT and sessions

# Register blueprints
app.register_blueprint(register_bp, url_prefix="/")
app.register_blueprint(login_bp, url_prefix="/")
app.register_blueprint(auth_bp, url_prefix="/")

@app.route("/")
def home():
    return "Welcome to Auth App! Go to /register or /login"

if __name__ == "__main__":
    app.run(port=5001, debug=True)
