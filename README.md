# Zania---AI

## Project Description

This project is designed to answer user questioons related to a doc. User can define the questions in constant.py. Agent will try to answer those question based on pdf file input when running the main code

## Key features include:

1. Load pdf file
2. Break PDF file into chunks
3. Use chunks to answer the questions
4. Post answer on slack

## Installation

Clone the project from github

```bash
git clone <repository-url>
cd <repository-directory>
```

Create and activate a virtual env

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

## Craeting a .env file

There is a .env.sample file present. Rename it to .env and add OPENAI_KEY and SLACK_OAUTH_KEY to it.

## Running the code

```bash
python main.py handbook.pdf
```
