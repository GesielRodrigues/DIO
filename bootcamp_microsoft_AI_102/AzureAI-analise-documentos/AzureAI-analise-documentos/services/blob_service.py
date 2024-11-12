import os
import streamlit as st
from azure.storage.blob import BlobServiceClient
from utils.Config import Config


def upload_blob(file, filename):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=filename)
        blob_client.upload_blob(file, overwrite=True)
        return blob_client.url
    except Exception as ex:
        st.error(f"Erro ao enviar o arquivo para o Azure Blob Storage: {ex}")
        return None
    
# Verificano o que tenho dentro do meu container de nome cartão:
def listar_blob():
    blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(container=Config.CONTAINER_NAME)
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print(f"Name: {blob.name}")
