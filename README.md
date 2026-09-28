# Emotion Detector

An AI-based web application that analyzes English text with the IBM Watson NLP
emotion model. The application reports scores for anger, disgust, fear, joy,
and sadness, then identifies the dominant emotion.

## Project structure

- `EmotionDetection/`: reusable Python package for emotion analysis
- `server.py`: Flask web application
- `templates/index.html`: browser interface
- `test_emotion_detection.py`: unit tests
- `submission/`: assignment code, terminal output, and screenshot evidence

## Run the application

```bash
pip install -r requirements.txt
python server.py
```

Open `http://localhost:5000` in a browser.
