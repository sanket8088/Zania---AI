import argparse
import os
from PDFParser import PDFParser
from GPTClient import GPTClient
from Notifier import SlackNotifier
from dotenv import load_dotenv
from constant import QUESTIONS

def main(pdf_file):
    # Load environment variables
    load_dotenv()

    # Retrieve API keys from environment variables
    OPENAI_KEY = os.getenv("OPENAI_KEY")
    OAUTH_TOKEN = os.getenv("OAUTH_TOKEN")

    # Check if environment variables are loaded
    if not OPENAI_KEY or not OAUTH_TOKEN:
        raise ValueError("API keys are not set in the environment variables.")

    # Extract text from PDF
    try:
        pdf_client = PDFParser(pdf_file)
        text = pdf_client.extract_text()
    except Exception as e:
        raise RuntimeError(f"Failed to extract text from PDF: {e}")

    # Initialize GPT client
    try:
        gpt_client = GPTClient(OPENAI_KEY)
    except Exception as e:
        raise RuntimeError(f"Failed to initialize GPT client: {e}")

    try:
        answers = gpt_client.answer_questions(text, QUESTIONS)
    except Exception as e:
        raise RuntimeError(f"Failed to get answers from GPT client: {e}")

    # Initialize Slack notifier
    try:
        notifier = SlackNotifier(token=OAUTH_TOKEN)
        # Format the message
        formatted_answers = "\n".join(f"{question}: {answer}" for question, answer in answers.items())
        notifier.send_message("C0449Q2EG3D", formatted_answers)
    except Exception as e:
        raise RuntimeError(f"Failed to send message to Slack: {e}")

    print("Process completed successfully.")

if __name__ == "__main__":
    # Set up argparse to accept the PDF file as a command-line argument
    parser = argparse.ArgumentParser(description="Process a PDF, extract text, and send answers to Slack.")
    parser.add_argument("pdf_file", help="The path to the PDF file you want to process.")
    
    # Parse arguments
    args = parser.parse_args()

    # Run the main function with the provided PDF file
    main(args.pdf_file)
