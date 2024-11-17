# AGRICULTURAL AI ASSISTANT

### Model
https://huggingface.co/Abhiram4/PlantDiseaseDetectorVit2

### Curl Command
```
curl -X POST -F "image=@temp/strawberry.jpg" http://127.0.0.1:5000/detect
```

### NGROK
```
ngrok config add-authtoken 2arA8uemHkeZTWsMZUmTLygh2Kc_6nN58vALm6fTkk3hqkcqV
```
```
ngrok http http://127.0.0.1:5000
```
#### LIVE 
https://agricultural-ai-assistant.onrender.com/
