# 🌿 Agricultural AI Assistant

![Kotlin](https://img.shields.io/badge/Kotlin-1.8.10-blue.svg)
![Compose](https://img.shields.io/badge/Compose-1.4.0-green.svg)
![Hilt](https://img.shields.io/badge/Hilt-2.45-brightgreen.svg)
![Room](https://img.shields.io/badge/Room-2.5.0-blue.svg)
[![Android API](https://img.shields.io/badge/Android%20API-26%2B-brightgreen)](https://developer.android.com/studio/releases/platforms)
![Version](https://img.shields.io/badge/Version-1.0.10-brightgreen.svg)

A web and Android-based plant disease detection system using AI and Computer Vision. Users can upload or capture images of plants to get instant disease diagnosis along with cause, treatment, and prevention — all in English, Hindi, or Marathi.

---

## 🌐 Live Web App

🚀 **Try it now**:  
[https://agricultural-ai-assistant.onrender.com/](https://agricultural-ai-assistant.onrender.com/)

---

## 🎓 Academic Information

🏫 **Final Year Project (2025)**
🎓 BE Computer Engineering
🏢 Gokhale Education Society's R. H. Sapat College of Engineering, Nashik
📚 Savitribai Phule Pune University (SPPU)

---

## 👩‍💻 Team Members

| Name                | Email                                                                        | GitHub                                                           |
| ------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Bhushan Malekar** | [xectrone@gmail.com](mailto:xectrone@gmail.com)      | [@xectrone](https://github.com/xectrone) |
| **Srushty Borkar**  | [borkar.srushty@ges-coengg.org](mailto:borkar.srushty@ges-coengg.org)        | [github.com/srushtyborkar](https://github.com/srushtyborkar)     |
| **Prasen Mhaskar**  | [prasenmhaskar13092003@gmail.com](mailto:prasenmhaskar13092003@gmail.com) | [@Prasen45](https://github.com/Prasen45)     |
| **Anand Dhomase**   | [21\_anand.dhomase@ges-coengg.org](mailto:21_anand.dhomase@ges-coengg.org)   | [github.com/ananddhomase](https://github.com/ananddhomase)       |

---

## 🧠 Features

* 🌱 **Plant Disease Detection** using HuggingFace ViT (Vision Transformer)
* 📸 **Image Upload Support** via Android App
* 📝 **Disease History Tracking** (per user, without storing images)
* 🧾 **Detailed Disease Info**: Description, Cause, Treatment, Prevention
* 🔐 **User Authentication** (Signup/Login using Flask)
* 🌐 **Multilingual Support**: English, Hindi, Marathi
* 🧰 **Logs** for debugging (`logs/app.log`)

---

## 🏗️ Tech Stack

| Component       | Technology                         |
| --------------- | ---------------------------------- |
| Frontend (App)  | Android (Jetpack Compose + Kotlin) |
| Backend         | Flask (Python)                     |
| Model Inference | HuggingFace Transformers (ViT)     |
| Database        | SQLite (via Flask SQLAlchemy)      |
| Deployment      | [Render.com](https://render.com/)  |

---

## 🔌 How it Works

1. 📲 Android app captures or uploads a plant image.
2. 📤 The image is sent to the Flask backend (`/detect` route).
3. 🧠 The backend uses a pretrained ViT model (`Abhiram4/PlantDiseaseDetectorVit2`) to detect disease.
4. 📚 Results are enhanced with descriptions from a JSON file (`disease_description.json`).
5. 🧾 Top result is returned and stored in user-specific history (excluding images).
6. 📱 The result is displayed in-app in the selected language.

---

## 📷 Supported Plants and Diseases

### ✅ Plants:

Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato

### 🦠 Diseases:

Apple Scab, Black Rot, Cedar Apple Rust, Powdery Mildew, Common Rust, Northern Leaf Blight, Citrus Greening, Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Spider Mites, Target Spot, Tomato Mosaic Virus, and more…

---

## 🧪 How to Run Locally

### 🔧 Backend Setup (Flask)

```bash
# Clone repo
git clone https://github.com/yourname/agri-ai-assistant.git
cd agri-ai-assistant

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py
```

### 📱 Android App

You can find the companion Android app repository here:
👉 [https://github.com/xectrone/agricultural_ai_assistant_android](https://github.com/xectrone/agricultural_ai_assistant_android)

1. Open in Android Studio
2. Change the Flask server URL in `uploadImageAndDetectDisease()` if needed
3. Run on emulator or real device

---

## 👥 User Authentication

* Users sign up using their email and password.
* Sessions are maintained using Flask sessions.
* Each user’s detection history is tracked separately and can be retrieved on login.

---

## 🗃️ Folder Structure

```
/app.py                  # Main Flask backend
/detection.py            # Handles image classification and description mapping
/disease_description.json # Disease info in multiple languages
/templates/              # HTML templates (index, signin, signup, history)
/static/                 # CSS/JS/static files
/temp/                   # Temporary uploaded images
/logs/app.log            # Logging for debug
```

---

## 🚀 Deployment

Deployed on [Render](https://render.com/) at:

```
https://agricultural-ai-assistant.onrender.com
```

---

## 🛡️ Future Improvements

* ✅ Add pagination & filters to detection history
* 🖼️ Store image thumbnails optionally (base64, size-limited)
* 🔍 Search plants/diseases dynamically
* 🗣️ Voice output support for disease reports

---

## 📄 License

MIT License