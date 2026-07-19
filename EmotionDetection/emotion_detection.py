"""Utilities for detecting emotions in text with the Watson NLP endpoint."""

from typing import Any

import requests


SERVICE_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_HEADER = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
REQUEST_TIMEOUT = 10
EMOTION_KEYS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_emotion_result() -> dict[str, float | None | str]:
    """Return the standardized response for invalid or unavailable input."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def emotion_detector(text_to_analyze: str) -> dict[str, Any]:
    """Analyze text and return emotion scores with the dominant emotion."""
    request_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            SERVICE_URL,
            headers=MODEL_HEADER,
            json=request_json,
            timeout=REQUEST_TIMEOUT,
        )
        if response.status_code == 400:
            return _empty_emotion_result()

        response.raise_for_status()
        response_dict = response.json()
    except requests.RequestException:
        return _empty_emotion_result()

    emotion_scores = response_dict["emotionPredictions"][0]["emotion"]
    result = {key: emotion_scores[key] for key in EMOTION_KEYS}
    result["dominant_emotion"] = max(result, key=result.get)

    return result
