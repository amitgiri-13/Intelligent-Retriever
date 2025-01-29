import sys
import os
import logging
import yaml
from pipeline.rag_pipeline import RAGPipeline

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("rag_pipeline.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)

# Function to load configuration files
def load_config(config_path):
    try:
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        logger.info(f"Successfully loaded config file: {config_path}")
        return config
    except Exception as e:
        logger.error(f"Error loading config file {config_path}: {e}")
        sys.exit(1)

def main():
    try:
        # Load configuration
        config_path = "config/rag_config.yaml"  # Ensure this file exists
        config = load_config(config_path)

        # Extract settings from config
        rag_model = config.get("rag_model")
        gen_model = config.get("gen_model")
        file_path = config.get("file_path")
        top_k = config.get("top_k")

        if not file_path:
            logger.error("File path is missing in the config file.")
            sys.exit(1)

        logger.info("Initializing RAGPipeline...")
        rag_pipeline = RAGPipeline(rag_model, gen_model)
        logger.info(f"RAGPipeline initialized with models: {rag_model}, {gen_model}")

        query = input("Enter your prompt: ")
        logger.info(f"User query: {query}")

        logger.info(f"Running RAGPipeline with file: {file_path} and top_k: {top_k}")
        response = rag_pipeline.run(query, file_path, top_k)

        logger.info(f"Pipeline response: {response}")
        print("Response:", response)

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
