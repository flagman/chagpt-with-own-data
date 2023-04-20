import unittest
from unittest.mock import MagicMock, patch
from chat_gpt_processor import ChatGPTProcessor


class TestChatGPTProcessor(unittest.TestCase):
    def setUp(self):
        self.api_key = "your_openai_api_key"
        self.processor = ChatGPTProcessor(self.api_key)

    @patch("openai.ChatCompletion.create")
    def test_get_response(self, mock_create):
        # Mock the API response
        mock_create.return_value = MagicMock(choices=[
            MagicMock(
                message=MagicMock(
                    content="The Los Angeles Dodgers won the World Series in 2020.")
            )
        ])

        prompt = "Who won the world series in 2020?"
        expected_response = "The Los Angeles Dodgers won the World Series in 2020."
        actual_response = self.processor.get_response(prompt)
        self.assertEqual(actual_response, expected_response,
                         "Responses do not match")
