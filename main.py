import sys
import os
from retriever.retriever import Retriever
from generator.generator import Generator
from pipeline.rag_pipeline import RAGPipeline
from scripts import query_pipeline, index_data
import logging
import yaml


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to load configuration files
def load_config(config_path):
    try:
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        logger.error(f"Error loading config file {config_path}: {e}")
        sys.exit(1)

def main():
    # Load configuration files 
    logger.info("Loading configurations...")
    retriever_config = load_config("config/retriever_config.yaml")
    generator_config = load_config("config/generator_config.yaml")
    pipeline_config = load_config("config/pipeline_config.yaml")

    # INitialize the retirever, generator and RAG pipeline
    logger.info("Initializing retriever, generator, and pipeline...")
    retriever = Retriever(retriever_config["retriever_model"],retriever_config["dimension"])
    generator = Generator(generator_config["generator_model"])
    rag_pipeline = RAGPipeline(retriever_config["retriever_model"],generator_config["generator_model"])
 
#    # Indexing data (can be customized to use specific files)
#     logger.info("Indexing data...")
#     rag_pipeline.index_data("data/corpus/docs.txt")

   # Querying the pipeline
    query = input("enter your prompt: ")
    logger.info(f"Querying the pipeline with: {query}")
    response = rag_pipeline.run(query,"/home/amit/Repositories/PythonStuffs/ArtificialIntelligence/RAGImplementation/data/corpus/nepal.pdf",5)
    logger.info(f"Response: {response}")

if __name__ == "__main__":
    main()


