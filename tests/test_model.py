import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.model import predict_message, train_model

class TestModel(unittest.TestCase):
    def test_prediction_spam(self):
        msg = "Win a free iPhone now! Click here."
        pred, _ = predict_message(msg)
        self.assertEqual(pred, 1)

    def test_prediction_ham(self):
        msg = "Hey, are we still on for dinner?"
        pred, _ = predict_message(msg)
        self.assertEqual(pred, 0)

if __name__ == '__main__':
    unittest.main()
