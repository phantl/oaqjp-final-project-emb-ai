import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        
        resp1 = emotion_detector("I am glad this happened")
        self.assertEqual("joy", resp1["dominant_emotion"])

        resp2 = emotion_detector("I am really mad about this")
        self.assertEqual("anger", resp2["dominant_emotion"])

        resp3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual("disgust", resp3["dominant_emotion"])

        resp4 = emotion_detector("I am so sad about this")
        self.assertEqual("sadness", resp4["dominant_emotion"])

        resp5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual("fear", resp5["dominant_emotion"])

if __name__ == "__main__":
    unittest.main()