"""Unit tests for the EmotionDetection package."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Validate dominant emotions for representative input phrases."""

    @staticmethod
    def mock_successful_response(emotion_scores: dict[str, float]) -> Mock:
        """Create a mock Watson response containing emotion scores."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [{"emotion": emotion_scores}]
        }
        return mock_response

    def assert_dominant_emotion(
        self,
        text_to_analyze: str,
        expected_emotion: str,
        emotion_scores: dict[str, float],
    ) -> None:
        """Assert that the detector returns the expected dominant emotion."""
        mock_response = self.mock_successful_response(emotion_scores)

        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=mock_response,
        ):
            result = emotion_detector(text_to_analyze)

        self.assertEqual(result["dominant_emotion"], expected_emotion)

    def test_joy_statement(self) -> None:
        """Detect joy from a glad statement."""
        self.assert_dominant_emotion(
            "I am glad this happened",
            "joy",
            {
                "anger": 0.01,
                "disgust": 0.01,
                "fear": 0.01,
                "joy": 0.95,
                "sadness": 0.02,
            },
        )

    def test_anger_statement(self) -> None:
        """Detect anger from a mad statement."""
        self.assert_dominant_emotion(
            "I am really mad about this",
            "anger",
            {
                "anger": 0.92,
                "disgust": 0.03,
                "fear": 0.02,
                "joy": 0.01,
                "sadness": 0.02,
            },
        )

    def test_disgust_statement(self) -> None:
        """Detect disgust from a disgusted statement."""
        self.assert_dominant_emotion(
            "I feel disgusted just hearing about this",
            "disgust",
            {
                "anger": 0.05,
                "disgust": 0.89,
                "fear": 0.02,
                "joy": 0.01,
                "sadness": 0.03,
            },
        )

    def test_sadness_statement(self) -> None:
        """Detect sadness from a sad statement."""
        self.assert_dominant_emotion(
            "I am so sad about this",
            "sadness",
            {
                "anger": 0.02,
                "disgust": 0.01,
                "fear": 0.03,
                "joy": 0.01,
                "sadness": 0.93,
            },
        )

    def test_fear_statement(self) -> None:
        """Detect fear from an afraid statement."""
        self.assert_dominant_emotion(
            "I am really afraid that this will happen",
            "fear",
            {
                "anger": 0.01,
                "disgust": 0.01,
                "fear": 0.94,
                "joy": 0.01,
                "sadness": 0.03,
            },
        )


if __name__ == "__main__":
    unittest.main()
