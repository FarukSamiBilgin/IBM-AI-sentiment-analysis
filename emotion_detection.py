"""Call the Watson NLP emotion prediction service."""

import requests


URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyze):
    """Return the raw Watson NLP response for the supplied text."""
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url=URL, headers=HEADERS, json=payload, timeout=30)
    return response.text
