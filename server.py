''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions and
        their corresponding weights, as well as the dominant
        emotion amongst them.
    '''
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {anger},"\
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and"\
        f" 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
