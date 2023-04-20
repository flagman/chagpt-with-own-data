import unittest
from embedding_generator import EmbeddingGenerator
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')


class TestEmbeddingGenerator(unittest.TestCase):

    def setUp(self):
        self.api_key = OPENAI_KEY
        self.generator = EmbeddingGenerator(self.api_key)

    def test_generate_embeddings(self):
        # Test that the method returns a list of tuples
        text = "This is a test text."
        embeddings = self.generator.generate_embeddings(text)
        self.assertIsInstance(embeddings, list)
        for emb in embeddings:
            self.assertIsInstance(emb, tuple)
            self.assertIsInstance(emb[0], str)
            self.assertIsInstance(emb[1], list)

        # Test that the embeddings have the expected length
        text = "This is a test text."
        embeddings = self.generator.generate_embeddings(text)
        for emb in embeddings:
            self.assertEqual(len(emb[1]), 1536)

        # Test that the method works with larger inputs
        text = "1" * 1001
        embeddings = self.generator.generate_embeddings(text)
        self.assertEqual(len(embeddings), 2)
