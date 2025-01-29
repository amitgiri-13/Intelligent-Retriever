import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY is missing! Set it in the .env file.")

class Generator:
    def __init__(self, model_name="gemini-1.5-flash"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text

if __name__ == "__main__":
    prompt = "what is cat command?"
    generator = Generator()
    print(generator.generate(prompt))


    