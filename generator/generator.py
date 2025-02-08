import os
from dotenv import load_dotenv
import google.generativeai as genai

# Setting up API Key
load_dotenv()
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY is missing! Set it in the .env file.")

class Generator:
    """Uses genai from google.generativeai as llm to generate answers based on user's query and content from returever.
    """
    def __init__(self, model_name="gemini-1.5-flash"):
        """Initializing the llm model.

        Args:
            model_name (str, optional): Name of the model. Defaults to "gemini-1.5-flash".
        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt:str) -> str:
        """Generate answers based on the prompt using llm model.

        Args:
            prompt (str): Prompt to feed llm.

        Returns:
            str: Response from the llm.
        """
        response = self.model.generate_content(prompt)
        return response.text

# Testing
if __name__ == "__main__":
    prompt = "who is tom?"
    generator = Generator()
    print(generator.generate(prompt))


    