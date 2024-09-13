import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=headers)

    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion' : dominant_emotion
            }

    emotionPredictions = formatted_response["emotionPredictions"][0]["emotion"]
    
    anger_score = emotionPredictions["anger"]
    disgust_score = emotionPredictions["disgust"]
    fear_score = emotionPredictions["fear"]
    joy_score = emotionPredictions["joy"]
    sadness_score = emotionPredictions["sadness"]
    
    scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            }

    dominant_emotion = max(scores, key=scores.get)
    scores["dominant_emotion"] = dominant_emotion

    return scores