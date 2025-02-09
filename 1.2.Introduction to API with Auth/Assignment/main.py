import os
import requests
from flask import Flask, request, jsonify, render_template
from urllib.request import urlretrieve
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Generate an image using the Illusion Diffusion API
def llusion_diffusion(description):
    API_KEY = os.getenv("Fal_API_KEY")
    url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
        "prompt": f"(masterpiece:1.4), (best quality), (detailed), {description}",
        "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["image"]["url"]
    else:
        return None

# Identify the plant using PlantNet API
def plantnet(image_path):
    API_KEY = os.getenv("Plantnet_API_KEY")
    url = "https://my-api.plantnet.org/v2/identify/all"
    files = {
        "images": open(image_path, "rb")
    }
    params = {
        "api-key": API_KEY
    }

    response = requests.post(url, params=params, files=files)
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            species = results[0]["species"]
            return species.get("commonNames", ["Unknown"])[0]
    return "Unknown"

@app.route("/")
def index():
    return render_template("templates/index.html")

@app.route("/generate", methods=["POST"])
def generate():
    plant_description = request.form.get("description")
    if not plant_description:
        return jsonify({"error": "No description provided"}), 400

    # Generate plant image
    image_url = llusion_diffusion(plant_description)
    if not image_url:
        return jsonify({"error": "Failed to generate image"}), 500

    # Save the image locally
    image_path = "static/local-plant.jpg"
    urlretrieve(image_url, image_path)

    # Identify the plant
    plant_name = plantnet(image_path)

    return jsonify({"image_url": image_url, "plant_name": plant_name})

if __name__ == "__main__":
    app.run(debug=True)
