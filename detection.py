# detection.py
from transformers import pipeline
import wikipediaapi
import logging
import os
import uuid  # For generating unique filenames
from flask import Flask, request, jsonify

# Set up logging
logging.basicConfig(
    filename='logs/app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Initialize the image classification pipeline with the Hugging Face model
pipe = pipeline("image-classification", model="Abhiram4/PlantDiseaseDetectorVit2")
logging.info("Image classification pipeline initialized.")

# Initialize Wikipedia API with a custom user agent
wiki = wikipediaapi.Wikipedia(user_agent="agricultural_ai_assistant/1.0 (spidergeneticks@gmail.com)")

logging.info("Wikipedia API initialized.")

def normalize_label(label):
    normalized = label.replace('___', ': ').replace('_', ' ').title()
    logging.debug(f"Normalized label: {label} to {normalized}")
    return normalized

def get_disease_description_dynamic(label):
    normalized_label = normalize_label(label)
    try:
        page = wiki.page(normalized_label)
        if page.exists():
            summary = page.summary[0:500]  # Limit the summary to the first 500 characters
            logging.info(f"Description found for {normalized_label}")
            return summary
        else:
            logging.warning(f"No description found for {normalized_label}")
            return "No description available for this disease."
    except Exception as e:
        logging.error(f"Error fetching description for {normalized_label}: {str(e)}")
        return f"Error fetching description: {str(e)}"

def detect_plant_diseases(image_path):
    try:
        # Use the model to classify the image
        results = pipe(image_path)
        logging.info(f"Image classification results: {results}")

        # Enhance results with descriptions
        enhanced_results = []
        for result in results:
            label = normalize_label(result['label'])
            score = result['score'] * 100  # Convert to percentage
            description = get_disease_description_dynamic(label)
            enhanced_results.append({
                "label": label,
                "confidence": f"{score:.2f}%",
                "description": description
            })

        logging.info("Detection and enhancement complete.")
        return enhanced_results

    except Exception as e:
        logging.error(f"Error in detecting plant diseases: {str(e)}")
        return {"error": "An error occurred during detection."}

