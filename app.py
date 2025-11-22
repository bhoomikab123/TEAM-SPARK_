"""
Plant Disease Detection Flask Application
Updated for PyTorch 2.x and Flask 3.0 compatibility
"""

import os
from flask import Flask, redirect, render_template, request
from PIL import Image
import torchvision.transforms.functional as TF
import CNN
import numpy as np
import torch
import pandas as pd

# Load disease and supplement information using absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

disease_csv_path = os.path.join(BASE_DIR, "disease_info.csv")
supplement_csv_path = os.path.join(BASE_DIR, "supplement_info.csv")

if not os.path.exists(disease_csv_path):
    raise FileNotFoundError(f"disease_info.csv not found at {disease_csv_path}")

if not os.path.exists(supplement_csv_path):
    raise FileNotFoundError(f"supplement_info.csv not found at {supplement_csv_path}")

disease_info = pd.read_csv(disease_csv_path, encoding='cp1252')
supplement_info = pd.read_csv(supplement_csv_path, encoding='cp1252')


# Initialize and load model
device = torch.device('cpu')
model = CNN.CNN(39)
model_path = "plant_disease_model_1_latest.pt"

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}. Please download it from the repository.")

model.load_state_dict(torch.load(model_path, map_location=device))
model.to(device)
model.eval()

def prediction(image_path):
    """Predict plant disease from image path"""
    try:
        # Open and preprocess image
        image = Image.open(image_path).convert('RGB')
        image = image.resize((224, 224))
        input_data = TF.to_tensor(image)
        input_data = input_data.unsqueeze(0)  # Add batch dimension
        
        # Make prediction
        with torch.no_grad():
            input_data = input_data.to(device)
            output = model(input_data)
            output = output.cpu().detach().numpy()
        
        index = np.argmax(output)
        return index
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return 0  # Return default index on error


app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact-us.html')

@app.route('/index')
def ai_engine_page():
    return render_template('index.html')

@app.route('/mobile-device')
def mobile_device_detected_page():
    return render_template('mobile-device.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        try:
            if 'image' not in request.files:
                return redirect(request.url)
            
            image = request.files['image']
            if image.filename == '':
                return redirect(request.url)
            
            # Create uploads directory if it doesn't exist
            upload_dir = 'static/uploads'
            os.makedirs(upload_dir, exist_ok=True)
            
            filename = image.filename
            file_path = os.path.join(upload_dir, filename)
            image.save(file_path)
            
            # Make prediction
            pred = prediction(file_path)
            
            # Ensure pred is within valid range
            if pred < 0 or pred >= len(disease_info):
                pred = 0
            
            # Get disease information (using .iloc for pandas 2.x compatibility)
            title = disease_info.iloc[pred]['disease_name']
            description = disease_info.iloc[pred]['description']
            prevent = disease_info.iloc[pred]['Possible Steps']
            image_url = disease_info.iloc[pred]['image_url']
            
            # Get supplement information
            supplement_name = supplement_info.iloc[pred]['supplement name']
            supplement_image_url = supplement_info.iloc[pred]['supplement image']
            supplement_buy_link = supplement_info.iloc[pred]['buy link']
            
            return render_template('submit.html', 
                                 title=title, 
                                 desc=description, 
                                 prevent=prevent, 
                                 image_url=image_url, 
                                 pred=pred,
                                 sname=supplement_name, 
                                 simage=supplement_image_url, 
                                 buy_link=supplement_buy_link)
        except Exception as e:
            print(f"Error in submit route: {str(e)}")
            return render_template('submit.html', 
                                 title="Error", 
                                 desc=f"An error occurred: {str(e)}", 
                                 prevent="Please try again with a valid image.",
                                 image_url="",
                                 pred=0,
                                 sname="",
                                 simage="",
                                 buy_link="")

@app.route('/market', methods=['GET', 'POST'])
def market():
    try:
        return render_template('market.html', 
                             supplement_image=list(supplement_info['supplement image']),
                             supplement_name=list(supplement_info['supplement name']), 
                             disease=list(disease_info['disease_name']), 
                             buy=list(supplement_info['buy link']))
    except Exception as e:
        print(f"Error in market route: {str(e)}")
        return render_template('market.html', 
                             supplement_image=[],
                             supplement_name=[], 
                             disease=[], 
                             buy=[])

if __name__ == '__main__':
    app.run(debug=True)
