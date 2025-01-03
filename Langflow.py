import requests
from typing import Optional
import os

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "004b8f6a-4ab4-4e79-bbcf-e822281fd951"
APPLICATION_TOKEN = "AstraCS:xbIaSnPrzfgBqEeYEoqWBuvj:d6d7e4fc1b3346237ff6ff87292241eba14b0681e04cafa083ea80bc971688f1"

def get_socialAna(platform,post_type):
        
    TWEAKS = {
    "TextInput-dcGgU": {
        "input_value": post_type
    },
    "TextInput-yNPir": {
        "input_value": platform
    },
    }
    return run_flow("",tweaks=TWEAKS,application_token=APPLICATION_TOKEN)

def run_flow(message: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/socialana"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()["outputs"][0]["outputs"][0]["results"]["message"]["text"]


def GPT_insight(platform,post_type):
    result = get_socialAna(platform=platform,post_type=post_type)
    return result