import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.preprocessing import transform_text

class TestPreprocessing(unittest.TestCase):
    def test_transform_text(self):
        text = "I loved the YouTube video!"
        transformed = transform_text(text)
        self.assertIn("love", transformed)
        self.assertIn("youtub", transformed)
        self.assertIn("video", transformed)

    def test_special_chars(self):
        text = "Hello!!! %$#"
        transformed = transform_text(text)
        self.assertEqual(transformed, "hello")

if __name__ == '__main__':
    unittest.main()
