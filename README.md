# 🌿 Agricultural AI Assistant
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)  
![Flask](https://img.shields.io/badge/Flask-2.3.3-lightgrey.svg)  
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.30-orange.svg)  
![HuggingFace Transformers](https://img.shields.io/badge/Transformers-ViT-yellow.svg)  
![Multilingual](https://img.shields.io/badge/Multilingual-English%2C%20Hindi%2C%20Marathi-brightgreen.svg)  
![Deployment](https://img.shields.io/badge/Hosted_on-Render-blue.svg)  
![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen.svg)

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


## 👨‍💻 Project Contributors


| 👤 Name         | 📧 Email                          | 🌐 GitHub Profile                                                                                                           |
| --------------- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Bhushan Malekar | `xectrone@gmail.com`              | [![@xectrone](https://img.shields.io/badge/GitHub-@xectrone-blue?logo=github)](https://github.com/xectrone)                 |
| Srushty Borkar  | `1002borkarsr@gmail.com`   | [![@cygnusart](https://img.shields.io/badge/GitHub-@cygnusart-green?logo=github)](https://github.com/srushtyborkar) |
| Prasen Mhaskar  | `prasenmhaskar45@gmail.com` | [![@Prasen45](https://img.shields.io/badge/GitHub-@Prasen45-purple?logo=github)](https://github.com/Prasen45)               |
| Anand Dhomase   | `21_anand.dhomase@ges-coengg.org` | [![@ananddhomase](https://img.shields.io/badge/GitHub-@ananddhomase-orange?logo=github)](https://github.com/ananddhomase)   |

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