import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENDPOINT_AZURE_DOC = os.getenv("ENDPOINT_AZURE_DOC")
    KEY_AZURE_DOC = os.getenv("KEY_AZURE_DOC")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")    