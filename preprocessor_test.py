import unittest
from preprocessor import Preprocessor


class PreprocessorTest(unittest.TestCase):
    """
    Unit tests for the Preprocessor class.
    """

    def setUp(self):
        self.preprocessor = Preprocessor()

    def test_preprocess_keeps_letters_and_numbers(self):
        text = "Hello world! This is a test 123."
        expected_output = "hello world this is test 123"
        self.assertEqual(self.preprocessor.preprocess(text), expected_output)

    def test_preprocess_keeps_special_characters(self):
        text = "The price is $10.99 (20% off)."
        expected_output = "price is $10 99 (20% off)"
        self.assertEqual(self.preprocessor.preprocess(text), expected_output)

    def test_preprocess_removes_stopwords(self):
        text = "The quick brown fox jumps over the lazy dog."
        expected_output = "quick brown fox jumps over lazy dog"
        self.assertEqual(self.preprocessor.preprocess(text), expected_output)

    def test_preprocess_handles_multiple_sentences(self):
        text = "First sentence. Second sentence! Third sentence?"
        expected_output = "first sentence second sentence third sentence"
        self.assertEqual(self.preprocessor.preprocess(text), expected_output)

    def test_preprocess_handles_extra_whitespaces(self):
        text = "  This   is    a   test.  "
        expected_output = "this is test"
        self.assertEqual(self.preprocessor.preprocess(text), expected_output)


if __name__ == '__main__':
    unittest.main()
