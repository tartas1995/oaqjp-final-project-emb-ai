from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def form():
    text_to_analyze = request.args.get("textToAnalyze")
    if text_to_analyze == None:
        return render_template('index.html')
    result = emotion_detector(text_to_analyze)
    return f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is <b>{result['dominant_emotion']}</b>."


# Run the server if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5000)
