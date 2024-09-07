import pytest
from unittest.mock import patch, Mock
from Notifier import SlackNotifier
import json

class TestSlackNotifier:
    
    @pytest.fixture
    def notifier(self):
        """Fixture to create a SlackNotifier instance."""
        return SlackNotifier(token="test-token")
    
    @patch('requests.post')
    def test_send_message_success(self, mock_post, notifier):
        """Test sending a message to Slack successfully."""
        # Mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"ok": True}
        mock_post.return_value = mock_response
        
        channel = 'CD449Q2EG3D'
        text = "Hello, world!"
        
        response = notifier.send_message(channel, text)
        
        # Verify the request was made correctly
        mock_post.assert_called_once_with(
            'https://slack.com/api/chat.postMessage',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer test-token'
            },
            data=json.dumps({
                'channel': channel,
                'text': text,
                "parse": "full"
            })
        )
        
        # Verify the response from the Slack API
        assert response == {"ok": True}
    
    @patch('requests.post')
    def test_send_message_failure(self, mock_post, notifier):
        """Test handling of failed message sending."""
        # Mock response
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response
        
        channel = 'CD449Q2EG3D'
        text = "Hello, world!"
        
        with pytest.raises(Exception) as excinfo:
            notifier.send_message(channel, text)
        
        assert str(excinfo.value) == "Request to Slack API failed with status code 400. Response: Bad Request"
