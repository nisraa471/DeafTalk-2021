# DeafTalk-2021
Arabic sign language recognition web application using TensorFlow and Flask, powered by a custom-trained deep learning model. Built in 2021 as the first phase of the Deaf Vision research project, which explored AI-driven assistive technology for the deaf community.

Deaf Vision later expanded into real-time sound recognition for AR glasses, presented at the First World Cup for Innovation and Scientific Research (2022).

Overview
DeafTalk takes hand gesture images as input, classifies them using a TensorFlow/Keras model, and returns the Arabic translation with a text-to-speech audio output. The app handles two gestures simultaneously and flags low-confidence predictions automatically.
Features

Image-based sign language classification using a trained CNN model
Arabic text output with text-to-speech audio playback (gTTS)
Confidence threshold filtering — results below 80% are marked as unreliable
Dual image upload, classifying two gestures in one request
Flask web interface with Arabic RTL support

Supported Classes

GestureArabic TranslationSee you laterأراك لاحقاًYouأنتGood jobعمل جيدQuotationاقتباس
Tech Stack
LayerTechnologyLanguagePython 3.8ML FrameworkTensorFlow / KerasWeb FrameworkFlaskImage ProcessingPillow (PIL), NumPyText to SpeechgTTS
Project Structure
DeafTalk/
├── app.py                     Flask routes and request handling
├── SignLanguageDetector.py    Model loading and inference pipeline
├── keras_model.h5             Trained Keras CNN model
├── labels.txt                 Class label definitions
├── templates/
│   ├── home.html              Upload interface
│   └── classification.html   Results display
└── static/                    Sample test images

How It Works

Two gesture images are uploaded via the web interface
Each image is resized to 224x224 and normalized to the range used during training
The Keras model runs inference and outputs confidence scores per class
The highest-confidence class is selected as the prediction
If confidence is below 0.8, the output is flagged as unreliable (غير معروف)
The Arabic translation and audio URL are returned to the results page

Getting Started

bashpip install flask tensorflow pillow numpy gtts flask-cors
python app.py
Open http://localhost:5000 in your browser. The keras_model.h5 file must be present in the root directory.
Research Context
DeafTalk was the image recognition phase of a broader two-year independent research project (2020-2022). The project evolved into Deaf Vision, which focused on real-time environmental sound recognition designed to run on AR glasses, giving deaf individuals visual awareness of surrounding audio. The research was presented internationally in 2022.
