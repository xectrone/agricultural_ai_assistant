from transformers import pipeline
import wikipediaapi

# Create an image classification pipeline with the Plant Disease Detector model
pipe = pipeline("image-classification", model="Abhiram4/PlantDiseaseDetectorVit2")

# Initialize Wikipedia API with a custom user agent
wiki = wikipediaapi.Wikipedia(language='en', user_agent="FinalYearProject/1.0 (spidergeneticks@gmail.com)")

# Function to create human-readable labels
def humanize_label(label):
    # Remove underscores and convert to sentence case
    return label.replace('___', ': ').replace('_', ' ').capitalize()

# Function to fetch description dynamically from Wikipedia
def get_disease_description_dynamic(label):
    try:
        page = wiki.page(label)
        if page.exists():
            summary = page.summary[0:500]  # Limit the summary to the first 500 characters
            return summary
        else:
            return "No description available for this disease."
    except Exception as e:
        return f"Error fetching description: {str(e)}"

# Function to enhance and print results
def enhance_results(results):
    print("Plant Disease Detection Results:\n")
    for result in results:
        label = humanize_label(result['label'])
        score = result['score'] * 100  # Convert to percentage
        description = get_disease_description_dynamic(label)
        print(f"Detected: {label} with match of {score:.2f}%")
        print(f"Description: {description}\n")

# Example: Classify an image (Replace 'your_image_path.jpg' with the actual image path)
image_path = "res/grape3.jpg"
results = pipe(image_path)

# Enhance and print results
enhance_results(results)
