# 🌱 Plant Disease Detection

A deep learning-based web application for detecting plant diseases from leaf images. This project uses a Convolutional Neural Network (CNN) built with PyTorch to classify leaf images into 39 different disease categories.

## 📋 Table of Contents

- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Model Information](#-model-information)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- 🔍 **39 Disease Categories**: Detects various plant diseases across multiple plant species
- 🖼️ **Image Upload**: Easy-to-use web interface for uploading leaf images
- 📊 **Detailed Results**: Provides disease name, description, and treatment recommendations
- 💊 **Supplement Store**: Integrated marketplace for disease treatment products
- 🎯 **High Accuracy**: Achieves 98.9% test accuracy
- 🚀 **Modern Stack**: Built with PyTorch 2.x, Flask 3.0, and latest libraries

## 🛠️ Technologies Used

- **Deep Learning**: PyTorch 2.1.1, Torchvision 0.16.1
- **Web Framework**: Flask 3.0.0
- **Data Processing**: NumPy 1.26.2, Pandas 2.1.4
- **Image Processing**: Pillow 10.1.0
- **Frontend**: HTML, CSS, JavaScript
- **Development**: Jupyter Notebook

## 📦 Installation

### Prerequisites

- Python 3.9+ (recommended: Python 3.10 or 3.11)
- pip package manager
- Git (for cloning the repository)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Plant-Disease-Detection.git
   cd Plant-Disease-Detection
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   cd "Flask Deployed App"
   pip install -r requirements.txt
   ```

4. **Download the pre-trained model**
   - Download `plant_disease_model_1_latest.pt` from [Google Drive](https://drive.google.com/drive/folders/1ewJWAiduGuld_9oGSrTuLumg9y62qS6A?usp=share_link)
   - Place it in the `Flask Deployed App` folder

5. **Verify CSV files are present**
   - Ensure `disease_info.csv` and `supplement_info.csv` are in the `Flask Deployed App` folder

## 🚀 Usage

### Running the Web Application

1. Navigate to the Flask app directory:
   ```bash
   cd "Flask Deployed App"
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your browser and go to:
   ```
   http://localhost:5000
   ```

4. Upload a leaf image to get disease detection results!

### Using the Jupyter Notebook

1. Navigate to the Model directory:
   ```bash
   cd Model
   ```

2. Install notebook dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

4. Open `Plant Disease Detection Code.ipynb` to explore the model training and testing code.

## 📁 Project Structure

```
Plant-Disease-Detection/
│
├── Flask Deployed App/          # Web application
│   ├── app.py                   # Flask application main file
│   ├── CNN.py                   # CNN model architecture
│   ├── requirements.txt         # Python dependencies
│   ├── disease_info.csv         # Disease information database
│   ├── supplement_info.csv      # Supplement information
│   ├── plant_disease_model_1_latest.pt  # Pre-trained model
│   ├── templates/               # HTML templates
│   └── static/                  # Static files (CSS, images, uploads)
│
├── Model/                       # Model training and development
│   ├── Plant Disease Detection Code.ipynb  # Jupyter notebook
│   ├── requirements.txt         # Notebook dependencies
│   └── Readme.md                # Model documentation
│
├── test_images/                 # Sample test images
├── demo_images/                 # Demo screenshots
├── README.md                    # This file
├── CONTRIBUTING.md              # Contribution guidelines
├── LICENSE                      # MIT License
├── .gitignore                   # Git ignore rules
├── UPDATES.md                   # Version update details
└── FIXES_APPLIED.md             # Bug fixes documentation
```

## 🧠 Model Information

### Architecture
- **Type**: Convolutional Neural Network (CNN)
- **Layers**: 4 convolutional blocks with batch normalization
- **Input Size**: 224x224x3 (RGB images)
- **Output Classes**: 39 disease categories
- **Total Parameters**: ~52.6 million

### Performance
- **Train Accuracy**: 96.7%
- **Test Accuracy**: 98.9%
- **Validation Accuracy**: 98.7%

### Dataset
- **Source**: Plant Village Dataset
- **Link**: [Mendeley Data](https://data.mendeley.com/datasets/tywbtsjrjv/1)
- **Classes**: 39 different plant disease categories

## 🔄 Updated Versions (2024)

This project has been updated to use the latest stable versions:

| Package | Old Version | New Version |
|---------|------------|-------------|
| PyTorch | 1.8.1 | 2.1.1 |
| Torchvision | 0.9.1 | 0.16.1 |
| Flask | 1.1.2 | 3.0.0 |
| NumPy | 1.20.2 | 1.26.2 |
| Pandas | 1.2.4 | 2.1.4 |
| Pillow | 8.2.0 | 10.1.0 |

See [UPDATES.md](UPDATES.md) for detailed migration information.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on:

- Code of conduct
- Development setup
- Pull request process
- Coding standards

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Testing

Test images are available in the `test_images/` folder. Each image is named according to its disease category, making it easy to verify model predictions.

## 📚 Additional Resources

- **Blog Post**: [Plant Disease Detection Using CNNs with PyTorch](https://medium.com/analytics-vidhya/plant-disease-detection-using-convolutional-neural-networks-and-pytorch-87c00c54c88f)
- **Live Demo**: [Plant-Disease-Detection-AI](https://plant-disease-detection-ai.herokuapp.com/)
- **Dataset**: [Plant Village Dataset on Mendeley](https://data.mendeley.com/datasets/tywbtsjrjv/1)


## 📸 Screenshots

### Main Page
![Main Page](demo_images/1.png)

### AI Engine
![AI Engine](demo_images/2.png)

### Results Page
![Results Page](demo_images/3.png)

### Supplements/Fertilizer Store
![Store](demo_images/4.JPG)

### Contact Us
![Contact](demo_images/5.png)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Plant Village Dataset for providing the training data
- PyTorch community for excellent documentation
- All contributors who have helped improve this project

## 📧 Contact

For questions, issues, or suggestions, please open an issue on GitHub.

---

⭐ If you find this project helpful, please consider giving it a star!
