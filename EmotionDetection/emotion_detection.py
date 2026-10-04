import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = body, headers=headers)
    obj = json.loads(response.text)
    emotions = obj["emotionPredictions"][0]["emotion"]
    result = {
        'anger': emotions["anger"],
        'disgust': emotions["disgust"],
        'fear': emotions["fear"],
        'joy': emotions["joy"],
        'sadness': emotions["sadness"]
    }
    dominant_emotion = max(result, key=result.get)
    result["dominant_emotion"] = dominant_emotion
    return result