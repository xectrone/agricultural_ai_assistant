# detection.py
from transformers import pipeline
import logging
import sys   # For console logging
from flask import Flask, request, jsonify
import json

# Set up logging to log both to file and console
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler(sys.stdout)  # Log to console
    ]
)

# Initialize the image classification pipeline with the Hugging Face model
pipe = pipeline("image-classification", model="Abhiram4/PlantDiseaseDetectorVit2")
logging.info("Image classification pipeline initialized.")

# Load the disease descriptions from the JSON file
with open('disease_description.json', 'r') as f:
    disease_descriptions = json.load(f)
logging.info("Disease descriptions loaded from JSON.")

def normalize_label(label):
    normalized = label.replace('___', '___').replace('_', ' ').title()  # Keep triple underscores as they are for the JSON keys
    logging.debug(f"Normalized label: {label} to {normalized}")
    return normalized

def get_disease_description_from_json(label):
    # Check if the raw label exists in the JSON dictionary
    if label in disease_descriptions:
        disease_info = disease_descriptions[label]
        description = disease_info.get("Description", "No description available.")
        cause = disease_info.get("Cause", "No cause information available.")
        treatment = disease_info.get("Treatment", "No treatment information available.")
        prevention = disease_info.get("Prevention", "No prevention information available.")
        return {
            "description": description,
            "cause": cause,
            "treatment": treatment,
            "prevention": prevention
        }
    
    # If the raw label doesn't match, normalize it and check again
    normalized_label = normalize_label(label)
    if normalized_label in disease_descriptions:
        disease_info = disease_descriptions[normalized_label]
        description = disease_info.get("Description", "No description available.")
        cause = disease_info.get("Cause", "No cause information available.")
        treatment = disease_info.get("Treatment", "No treatment information available.")
        prevention = disease_info.get("Prevention", "No prevention information available.")
        return {
            "description": description,
            "cause": cause,
            "treatment": treatment,
            "prevention": prevention
        }

    # If neither the raw nor normalized label matches, return default values
    logging.warning(f"No description found for {label}")
    return {
        "description": "No description available for this disease.",
        "cause": "N/A",
        "treatment": "N/A",
        "prevention": "N/A"
    }


def detect_plant_diseases(image_path):
    try:
        # Use the model to classify the image
        results = pipe(image_path)
        logging.info(f"Image classification results: {results}")

        # Enhance results with descriptions from JSON
        enhanced_results = []
        for result in results:
            label = result['label']  # Use the raw label from the model output
            score = result['score'] * 100  # Convert to percentage
            description_info = get_disease_description_from_json(label)
            
            enhanced_results.append({
                "label": normalize_label(label),  # Keep the raw label in the result
                "confidence": f"{score:.2f}%",
                "description": description_info['description'],
                "cause": description_info['cause'],
                "treatment": description_info['treatment'],
                "prevention": description_info['prevention']
            })

        logging.info("Detection and enhancement complete.")
        return enhanced_results

    except Exception as e:
        logging.error(f"Error in detecting plant diseases: {str(e)}")
        return {"error": "An error occurred during detection."}