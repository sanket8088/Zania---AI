import pytest
from unittest.mock import patch, Mock
from GPTClient import GPTClient  # Import the GPTClient class from your module
from utils import chunk_text  # Import chunk_text function if necessary

class TestGPTClient:
    
    @pytest.fixture
    def gpt_client(self):
        """Fixture to create a GPTClient instance."""
        return GPTClient(api_key="test-api-key")
    

    @patch.object(GPTClient, '_GPTClient__get_answer_with_confidence')
    def test_answer_questions_with_high_confidence(self, mock_get_answer_with_confidence):
        api_key = 'fake-api-key'
        gpt_client = GPTClient(api_key)
        text = "Sample Context"
        questions = ['What is the name of the company?']

        # Mock the __get_answer_with_confidence method
        mock_get_answer_with_confidence.return_value = {
            "answer": 'Sample Answer',
            "confidence": 100.0
        }

        # Call the method under test
        answers = gpt_client.answer_questions(text, questions)
        # Assert that the correct answer is returned
        assert answers == {'What is the name of the company?': 'Sample Answer'}

    @patch('instructor.patch')
    @patch('openai.OpenAI')
    def test_answer_questions_with_low_confidence(self, mock_openai, mock_instructor, gpt_client):
        """Test the answer_questions method when confidence is low."""
        # Mock the response from OpenAI API
        mock_client = Mock()
        mock_openai.return_value = mock_client
        mock_response = Mock()
        mock_response.answer = "Sample Answer"
        mock_response.confidence_score = 20.0
        mock_client.chat.completions.create.return_value = mock_response
        
        # Define the text and questions
        text = "This is a sample context. It contains the answer."
        questions = ["What is the answer?"]
        
        # Mock chunk_text function
        with patch('utils.chunk_text', return_value=[text]):
            answers = gpt_client.answer_questions(text, questions)

        # Verify the answers
        assert answers == {"What is the answer?": "Data Not Available"}
