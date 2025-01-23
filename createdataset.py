from mira_sdk import MiraClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("TEST_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

# Create dataset ->This is creating a datset with username/nameofdataset and description about dataset 
client.dataset.create("1404samyak/cp-questions","A PDF file of CP resources")

#After creating the dataset we need to add some sources like url/pdfs to the created dataset 

#  Add URL to your data set (URL must be added to an existing dataset)->This must be added so that the dataset can be added
client.dataset.add_source("1404samyak/cp-questions", url="https://flows.mira.network/data-manager")

# Add file to your data set (file must be added to an existing dataset)
client.dataset.add_source("1404samyak/cp-questions", file_path="CP.pdf")