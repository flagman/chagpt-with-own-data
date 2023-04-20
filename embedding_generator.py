import openai
from typing import List, Tuple
from tqdm import tqdm


class EmbeddingGenerator:
    """
    Computes embeddings for each document or text passage in the corpus using OpenAI API.
    """

    def __init__(self, api_key: str, chunk_size: int = 1000):
        """
        Initializes the EmbeddingGenerator with the OpenAI API key.

        :param api_key: The OpenAI API key.
        """
        self.api_key = api_key
        self.chunk_size = chunk_size
        openai.api_key = api_key

    def generate_embeddings(self, text: str) -> List[Tuple[str, List[float]]]:
        """
        Generates embeddings for the input text using the OpenAI API.
        The input text is split into chunks of 1000 symbols and each chunk is processed separately.

        :param text: The input text.
        :return: The list of embeddings for the text.
        """
        chunks = [text[i:i+self.chunk_size]
                  for i in range(0, len(text), self.chunk_size)]
        embeddings = []
        for chunk in tqdm(chunks):
            response = openai.Embedding.create(
                engine="text-embedding-ada-002",
                input=chunk
            )
            chunk_embeddings = response["data"][0]["embedding"]
            embeddings.append((chunk, chunk_embeddings))
        return embeddings
