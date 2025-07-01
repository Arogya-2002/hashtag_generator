from src.exceptions import CustomException
from src.logger import logging
import sys
from src.entity.hashtag_config_entity import GeminiModelEntity, ConfigEntity
import google.generativeai as genai

class GeminiModel:
    def __init__(self):
        try:
            logging.info("Initializing GeminiModelEntity...")
            self.gemini_model_config = GeminiModelEntity(config=ConfigEntity())
            logging.info("GeminiModelEntity initialized successfully.")
        except Exception as e:
            logging.error("Failed to initialize GeminiModelEntity.")
            raise CustomException(e, sys) from e

    def initiate_model(self):
        try:
            logging.info("Gemini model initiation started.")
            genai.configure(api_key=self.gemini_model_config.google_api_key)
            model = genai.GenerativeModel(self.gemini_model_config.generative_model)
            logging.info(f"Gemini model '{self.gemini_model_config.generative_model}' initiated successfully.")
            return model
        except Exception as e:
            logging.error("Exception occurred while initiating Gemini model.", exc_info=True)
            raise CustomException(e, sys) from e
