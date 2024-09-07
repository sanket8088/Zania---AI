import requests
import json

class SlackNotifier:
    
    def __init__(self, token: str):
        self.token = token
        self.api_url = 'https://slack.com/api/chat.postMessage'
    
    def send_message(self, channel: str, text: str) -> dict:
        """Send a message to a Slack channel."""
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        
        payload = {
            'channel': channel,
            'text': text,
            "parse" : "full"
        }
        
        response = requests.post(self.api_url, headers=headers, data=json.dumps(payload))
        
        if response.status_code != 200:
            raise Exception(f"Request to Slack API failed with status code {response.status_code}. Response: {response.text}")
        
        return response.json()