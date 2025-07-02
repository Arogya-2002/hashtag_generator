import time
from datetime import datetime
from src.exceptions import CustomException
from src.logger import logging
from src.entity.hashtag_config_entity import HashtagConfigEntity, ConfigEntity
from src.entity.hashtag_artifact_entity import HashtagGeneratorArtifact
import sys

class HashtagGenerator:
    def __init__(self):
        try:
            self.hastag_config = HashtagConfigEntity(config=ConfigEntity())
            logging.info("Initialized HashtagConfigEntity successfully.")
        except Exception as e:
            logging.error("Error initializing HashtagConfigEntity.")
            raise CustomException(e, sys)

    def generate_hashtags(self, caption: str, model):
        """
        Sends caption to Gemini and gets 'k' hashtags.

        Args:
            caption (str): Caption for which hashtags are to be generated
            model: Gemini model object

        Returns:
            HashtagGeneratorArtifact: Structured output with hashtag list
        """
        try:
            logging.info("Preparing prompt for the caption.")
            prompt = f"""Generate exactly {self.hastag_config.k_hashtags} relevant and trendy hashtags for the following caption.
Return only the hashtags separated by spaces, without any explanation or numbering.

Caption: "{caption}"
Hashtags:"""

            logging.info("Sending prompt to Gemini model...")
            t1 = time.time()
            response = model.generate_content(prompt)
            t2 = time.time()
            logging.info(f"Received response from Gemini (Time taken: {t2 - t1:.2f} sec)")

            if response.text:
                hashtags = response.text.strip().replace("\n", " ").split()
                logging.info(f"Caption: {caption}")
                logging.info(f"Generated Hashtags: {hashtags}")
                return HashtagGeneratorArtifact(hashtags=hashtags)
            else:
                logging.warning("Empty response received from model.")
                return HashtagGeneratorArtifact(hashtags=[])

        except Exception as e:
            logging.error("Exception occurred during hashtag generation.")
            raise CustomException(e, sys)
