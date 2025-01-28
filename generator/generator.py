from transformers import pipeline
import google.generativeai as genai

api_key = "AIzaSyAtNJrVwP_C8hj2XJ43x8diXWlYStOUSTY"

class Generator:
    def __init__(self, model_name="gpt2"):
        self.generator = pipeline("text-generation", model=model_name)

    def generate(self, prompt, max_tokens=50):
        return self.generator(prompt, truncation=True, max_length=500, num_return_sequences=1)
    
if __name__ == "__main__":
    prompt = "Write me one line about cat command."
    

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    print(response.text)