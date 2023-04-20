import openai


class ChatGPTProcessor:
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        self.model = model
        self.api_key = api_key
        openai.api_key = self.api_key

    def get_response(self, prompt: str) -> str:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages
        )

        assistant_message = response.choices[0].message
        return assistant_message.content
