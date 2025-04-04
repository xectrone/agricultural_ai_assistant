from transformers import pipeline
import logging
import sys  # For console logging
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
with open('disease_description.json', 'r', encoding='utf-8') as f:
    disease_descriptions = json.load(f)
logging.info("Disease descriptions loaded from JSON.")


def normalize_label(label):
    normalized = label.replace('___', '___').replace('_', ' ').title()
    logging.debug(f"Normalized label: {label} to {normalized}")
    return normalized


def get_disease_description_from_json(label, lang='en'):
    data = disease_descriptions.get(label) or disease_descriptions.get(normalize_label(label))

    if not data:
        logging.warning(f"No description found for {label}")
        return {
            "description": "No description available for this disease.",
            "cause": "N/A",
            "treatment": "N/A",
            "prevention": "N/A"
        }

    return {
        "description": data.get(f"Description_{lang}", data.get("Description", "No description available.")),
        "cause": data.get(f"Cause_{lang}", data.get("Cause", "No cause information available.")),
        "treatment": data.get(f"Treatment_{lang}", data.get("Treatment", "No treatment information available.")),
        "prevention": data.get(f"Prevention_{lang}", data.get("Prevention", "No prevention information available."))
    }


def detect_plant_diseases(image_path, lang='en'):
    try:
        results = pipe(image_path)
        logging.info(f"Image classification results: {results}")

        enhanced_results = []
        for result in results:
            label = result['label']
            score = result['score'] * 100
            description_info = get_disease_description_from_json(label, lang)

            enhanced_results.append({
                "label": normalize_label(label),
                "confidence": f"{score:.2f}%",
                "description": description_info['description'],
                "cause": description_info['cause'],
                "treatment": description_info['treatment'],
                "prevention": description_info['prevention']
            })

        logging.info("Detection and enhancement complete.")

        # Only return the top result as a list with one item
        return [enhanced_results[0]] if enhanced_results else []

    except Exception as e:
        logging.error(f"Error in detecting plant diseases: {str(e)}")
        return {"error": "An error occurred during detection."}
