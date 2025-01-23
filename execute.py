from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

version = "0.0.1"
input_data = {"question": "What does Mira Network do and what is its vision, how are they planning to solve the problem of hallucination and biasness in LLM models?"}

# If no version is provided it'll use latest version by default
if version:
	flow_name = f"venmus/mira-qna/{version}"
else:
	flow_name = "venmus/mira-qna"

result = client.flow.execute(flow_name, input_data)
print(result)