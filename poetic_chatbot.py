from dotenv import load_dotenv
import os 
from openai import OpenAI


load_dotenv()



class PoeticChatbot:
    def __init__(self, model="gpt-4o-mini", temperature=0.7, max_tokens=256):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

        # Base conversation context
        self.base_messages = [
            {
                "role": "system",
                "content": "You are a poetic chatbot."
            },
            {
                "role": "user",
                "content": "When was Google founded?"
            },
            {
                "role": "assistant",
                "content": "In the late '90s, a spark did ignite, Google emerged, a radiant light. By Larry and Sergey, in '98, it was born, a search engine new, on the web it was sworn."
            },
            {
                "role": "user",
                "content": "Which country has the youngest president?"
            },
            {
                "role": "assistant",
                "content": "Ah, the pursuit of youth in politics, a theme we explore. In Austria, Sebastian Kurz did implore, at the age of 31, his journey did begin, leading with vigor, in a world filled with din."
            }
        ]

    def generate(self, prompt: str) -> str:
        """Generate poetic text for a user prompt."""
        messages = self.base_messages + [
            {"role": "user", "content": prompt}
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

        return response.choices[0].message.content.strip()


