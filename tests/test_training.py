import unittest
from app.training import model

class TrainingTestCase(unittest.TestCase):
    def test_model_exists(self):
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
