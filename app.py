from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
import os
import uuid
from detection import detect_plant_diseases
from datetime import datetime
from zoneinfo import ZoneInfo


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

# In app.py (or models.py if separate)
class DetectionHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(100), db.ForeignKey('user.email'), nullable=False)
    label = db.Column(db.String(100), nullable=False)
    confidence = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text)
    cause = db.Column(db.Text)
    treatment = db.Column(db.Text)
    prevention = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())


# Initialize Database
with app.app_context():
    db.create_all()

# Upload folder setup
UPLOAD_FOLDER = "temp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# Set max upload size to 50 MB
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB

@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("index"))  
    return redirect(url_for("signin"))  

@app.route("/signin", methods=["GET", "POST"])
def signin():
    message = None
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

        session["user"] = email
        session.permanent = True

        flash("Signup successful! Redirecting to dashboard.", "success")
        return redirect(url_for("index"))

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
    image = request.files.get('image')
    lang = request.form.get('lang', 'en')  # Default to English if not provided

    if not image:
        return jsonify({"error": "No image uploaded."}), 400

    temp_filename = os.path.join(app.config["UPLOAD_FOLDER"], f"{uuid.uuid4().hex}.jpg")
    image.save(temp_filename)

    results = detect_plant_diseases(temp_filename, lang=lang)
    os.remove(temp_filename)

    # Save result to DB
    if "user" in session and isinstance(results, list) and results:
        result = results[0]  # only saving top result
        history = DetectionHistory(
            user_email=session["user"],
            label=result["label"],
            confidence=result["confidence"],
            description=result["description"],
            cause=result["cause"],
            treatment=result["treatment"],
            prevention=result["prevention"]
        )
        db.session.add(history)
        db.session.commit()


    return jsonify({"results": results})

@app.route('/history')
def view_history():
    if "user" not in session:
        flash("You must be logged in to view your history.", "warning")
        return redirect(url_for("signin"))

    history = DetectionHistory.query.filter_by(user_email=session["user"]).order_by(DetectionHistory.timestamp.desc()).all()
    return render_template("history.html", history=history)

@app.route("/get-history")
def get_history():
    if "user" not in session:
        return jsonify({"history": []})

    records = DetectionHistory.query.filter_by(user_email=session["user"]).order_by(DetectionHistory.timestamp.desc()).all()

    history_data = []
    for h in records:
        history_data.append({
            "label": h.label,
            "confidence": h.confidence,
            "description": h.description,
            "cause": h.cause,
            "treatment": h.treatment,
            "prevention": h.prevention,
            "timestamp": h.timestamp.replace(tzinfo=ZoneInfo("UTC")).astimezone(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d %I:%M %p"),
        })

    return jsonify({"history": history_data})


@app.route("/clear-history", methods=["POST"])
def clear_history():
    if "user" not in session:
        return jsonify({"success": False}), 403

    DetectionHistory.query.filter_by(user_email=session["user"]).delete()
    db.session.commit()
    return jsonify({"success": True})



if __name__ == "__main__":
    app.run(debug=True)  # Change to False in production
