from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
import os
import uuid
from detection import detect_plant_diseases

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.permanent_session_lifetime = timedelta(minutes=30)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Initialize Database
with app.app_context():
    db.create_all()

# Upload folder setup
UPLOAD_FOLDER = "temp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("index"))  
    return redirect(url_for("signin"))  

@app.route("/signin", methods=["GET", "POST"])
def signin():
    message = None  # Initialize message
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session["user"] = email
            session.permanent = True
            flash("Login successful!", "success")
            return redirect(url_for("index"))  
        
        message = "Incorrect email or password. Please try again."
    
    return render_template("op_auth_signin.html", message=message)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("signup-email")
        password = request.form.get("signup-password")

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("User already exists! Try signing in.", "warning")
            return redirect(url_for("signin"))

        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Automatically log in the user
        session["user"] = email
        session.permanent = True

        flash("Signup successful! Redirecting to dashboard.", "success")
        return redirect(url_for("index"))  # Redirect to index.html

    return render_template("op_auth_signup.html")


@app.route("/index")
def index():
    if "user" not in session:
        flash("You must be logged in to access this page.", "warning")
        return redirect(url_for("signin"))
    return render_template("index.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("signin"))

@app.route('/detect', methods=['POST'])
def detect_disease():
    if "user" not in session:
        return jsonify({"error": "Unauthorized access"}), 401

    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = request.files['image']
    temp_filename = os.path.join(app.config["UPLOAD_FOLDER"], f"{uuid.uuid4().hex}.jpg")
    image.save(temp_filename)

    results = detect_plant_diseases(temp_filename)
    os.remove(temp_filename)

    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True)  # Change to False in production
