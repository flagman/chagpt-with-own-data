from typing import List


class PromptGenerator:
    """
    A class that combines user prompt with relevant text passages to generate ChatGPT prompt.
    """

    def generate_prompt(self, user_query: str, similar_texts: List[str]) -> str:
        """
        Generate a ChatGPT prompt using the found chunks and user query.

        Args:
            user_query (str): The user query.
            similar_texts (List[str]): A list of similar text passages to the user query.

        Returns:
            str: The generated prompt.
        """
        prompt = "Use the following information\n"
        for text in similar_texts:
            prompt += f"{text}\n\n"
        prompt += f"To answer the question: \n{user_query}"
        return prompt


# # sample usage
# prompt_generator = PromptGenerator()
# prompt = prompt_generator.generate_prompt("What is the capital of France?", [
#                                           "Paris is the capital of France.", "France is a country in Europe."])
# print(prompt)
