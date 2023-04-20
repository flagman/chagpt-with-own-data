import unittest
from prompt_generator import PromptGenerator


class TestPromptGenerator(unittest.TestCase):
    def setUp(self):
        self.prompt_generator = PromptGenerator()

    def test_generate_prompt(self):
        user_query = "What is the capital of France?"
        similar_texts = ["Paris is the capital of France.",
                         "France is home to Paris, the capital city."]
        expected_output = "Use the following information\nParis is the capital of France.\n\nFrance is home to Paris, the capital city.\n\nTo answer the question: \nWhat is the capital of France?"
        self.assertEqual(self.prompt_generator.generate_prompt(
            user_query, similar_texts), expected_output)
