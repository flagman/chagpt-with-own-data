import unittest
from embedding_generator import EmbeddingGenerator


class TestEmbeddingGenerator(unittest.TestCase):

    def setUp(self):
        # Initialize the EmbeddingGenerator with a test API key
        self.embedding_generator = EmbeddingGenerator(
            api_key="")

    def test_generate_embeddings(self):
        # Test that embeddings are generated correctly for a simple input string
        input_text = "Hello world!"
        embeddings = self.embedding_generator.generate_embeddings(input_text)
        # Check that the embeddings have the expected length and type
        self.assertEqual(len(embeddings), 1)
        self.assertIsInstance(embeddings[0], list)

    def test_generate_embeddings_large_input(self):
        # Test that embeddings are generated correctly for a large input string
        # with more than 1000 symbols
        input_text = "Lorem ipsum dolor sit amet" * 100
        embeddings = self.embedding_generator.generate_embeddings(input_text)
        # Check that the embeddings have the expected length and type
        self.assertEqual(len(embeddings), len(input_text)//1000 + 1)
        self.assertIsInstance(embeddings[0], list)
