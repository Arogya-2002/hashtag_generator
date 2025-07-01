from src.exceptions import CustomException
from src.logger import logging
from src.constants import *

class ConfigEntity:
    def __init__(self):
        self.google_api_key = GOOGLE_API_KEY
        self.generative_model = GENERATIVE_MODEL
        self.k_hashtags = K_HASHTAGS

class GeminiModelEntity:
    def __init__(self,config:ConfigEntity):
        self.google_api_key = config.google_api_key
        self.generative_model = config.generative_model


class HashtagConfigEntity:
    def __init__(self,config:ConfigEntity):
        self.k_hashtags = config.k_hashtags
   
        
