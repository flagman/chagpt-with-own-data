from typing import List
import numpy as np


class VectorDatabaseStorage:
    """
    Stores the generated embeddings in a vector database, allowing for efficient similarity searches
    """

    def __init__(self):
        self.database = {}

    def store(self, text: str, embedding: List[float]):
        """
        Store the input text and its corresponding embedding
        """
        self.database[text] = np.array(embedding)

    def query_similar_texts(self, query_embedding: List[float], num_results: int = 5) -> List[str]:
        """
        Retrieve the most similar texts to the input query using the embeddings
        """
        distances = {}
        for text, embedding in self.database.items():
            distance = np.linalg.norm(embedding - query_embedding)
            distances[text] = distance

        sorted_distances = sorted(distances.items(), key=lambda x: x[1])
        return [text for text, _ in sorted_distances[:num_results]]
