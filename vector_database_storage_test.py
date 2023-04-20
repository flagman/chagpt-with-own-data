import unittest
from vector_database_storage import VectorDatabaseStorage


class TestVectorDatabaseStorage(unittest.TestCase):
    def setUp(self):
        self.storage = VectorDatabaseStorage()
        self.embedding1 = [0.1, 0.2, 0.3]
        self.embedding2 = [0.4, 0.5, 0.6]
        self.embedding3 = [0.7, 0.8, 0.9]
        self.text1 = "Hello world"
        self.text2 = "Lorem ipsum dolor sit amet"
        self.text3 = "The quick brown fox jumps over the lazy dog"
        self.storage.store(self.text1, self.embedding1)
        self.storage.store(self.text2, self.embedding2)
        self.storage.store(self.text3, self.embedding3)

    def test_store(self):
        self.assertEqual(len(self.storage.database), 3)
        self.assertTrue(self.text1 in self.storage.database)
        self.assertTrue(self.text2 in self.storage.database)
        self.assertTrue(self.text3 in self.storage.database)
        self.assertTrue((self.storage.database[self.text1] == self.embedding1).all())
        self.assertTrue((self.storage.database[self.text2] == self.embedding2).all())
        self.assertTrue((self.storage.database[self.text3] == self.embedding3).all())

    def test_query_similar_texts(self):
        query_embedding = [0.6, 0.7, 0.8]
        similar_texts = self.storage.query_similar_texts(query_embedding, num_results=2)
        self.assertEqual(len(similar_texts), 2)
        self.assertTrue(self.text3 in similar_texts)
        self.assertTrue(self.text2 in similar_texts)
