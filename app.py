import argparse
import os

from dotenv import load_dotenv
from datasource import PDFDataSource
from preprocessor import Preprocessor
from embedding_generator import EmbeddingGenerator
from vector_database_storage import VectorDatabaseStorage
from prompt_generator import PromptGenerator
from chat_gpt_processor import ChatGPTProcessor


def main():
    parser = argparse.ArgumentParser(
        description='Query a PDF file using ChatGPT.')
    parser.add_argument('--pdf-url', required=True,
                        help='The URL of the PDF file to query.')
    parser.add_argument('--user-query', required=True,
                        help='The user query to ask ChatGPT.')
    parser.add_argument('--chunk-size', type=int, default=1000,
                        help='The number of texts to process at a time')
    parser.add_argument('--num-results', type=int, default=10,
                        help='The number of similar chunks to retrieve')

    args = parser.parse_args()

    # Load environment variables
    load_dotenv()
    OPENAI_KEY = os.getenv('OPENAI_KEY')

    # Step 1: Download and convert PDF data to text
    pdf_data_source = PDFDataSource(args.pdf_url)
    data = pdf_data_source.fetch_data()

    # Step 2: Preprocess the text
    preprocessor = Preprocessor()
    preprocessed_data = preprocessor.preprocess(data)

    # Step 3: Generate embeddings for preprocessed text and user query
    embedding_generator = EmbeddingGenerator(
        api_key=OPENAI_KEY, chunk_size=args.chunk_size)
    embeddings = embedding_generator.generate_embeddings(preprocessed_data,)

    _, query_embedding = embedding_generator.generate_embeddings(args.user_query)[
        0]

    # Step 4: Store embeddings in vector database storage
    vector_db = VectorDatabaseStorage()
    for chunk_embedding in embeddings:
        vector_db.store(chunk_embedding[0], chunk_embedding[1])

    # Step 5: Find similar chunks in vector database using query embedding
    similar_chunk_embeddings = vector_db.query_similar_texts(
        query_embedding, num_results=args.num_results)

    # Step 6: Generate ChatGPT prompt using found chunks and user query
    prompt_generator = PromptGenerator()
    prompt = prompt_generator.generate_prompt(
        args.user_query, similar_chunk_embeddings)

    # Step 7: Send prompt to ChatGPT and get response
    chatgpt_processor = ChatGPTProcessor(api_key=OPENAI_KEY)
    response = chatgpt_processor.get_response(prompt)

    print(response)


if __name__ == '__main__':
    main()
