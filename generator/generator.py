from transformers import pipeline

class Generator:
    def __init__(self, model_name="gpt2"):
        self.generator = pipeline("text-generation", model=model_name)

    def generate(self, prompt, max_tokens=50):
        return self.generator(prompt, truncation=True, max_length=500, num_return_sequences=1)
    
    