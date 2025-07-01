import sys
from src.logger import logging
from src.exceptions import CustomException
from src.components.gemini_model import GeminiModel
from src.components.hashtag_generator import HashtagGenerator


def hashtag_pipeline(caption: str):
    try:
        logging.info("Starting hashtag generation pipeline...")

        # Step 1: Initialize Gemini model
        logging.info("Initializing Gemini model...")
        model_handler = GeminiModel()
        model = model_handler.initiate_model()


        # Step 2: Generate hashtags
        logging.info("Generating hashtags for the provided caption...")
        generator = HashtagGenerator()
        hashtags = generator.generate_hashtags(caption=caption, model=model)

        # Step 3: Log result
        if hashtags:
            logging.info(f"Hashtags generated successfully:\n{hashtags}")
            return hashtags
        else:
            logging.warning("No hashtags were returned.")

    except CustomException as ce:
        logging.error("A custom exception occurred in the main pipeline.", exc_info=True)
    except Exception as e:
        logging.error("An unexpected error occurred in the main pipeline.", exc_info=True)
        raise CustomException(e, sys)
