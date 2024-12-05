"""
Flask application for Emotion Detection.
Provides an endpoint to analyze text and return emotions.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")


@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyze the emotion of the given text provided via query parameters.

    Returns:
        str: A formatted string with emotion analysis results or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please provide input for analysis."

    emotion_result = emotion_detector(text_to_analyze)
    anger = emotion_result.get('anger', 0.0)
    disgust = emotion_result.get('disgust', 0.0)
    fear = emotion_result.get('fear', 0.0)
    joy = emotion_result.get('joy', 0.0)
    sadness = emotion_result.get('sadness', 0.0)
    dominant_emotion = emotion_result.get('dominant_emotion')

    if not dominant_emotion:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Render the index page.

    Returns:
        str: HTML content for the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
