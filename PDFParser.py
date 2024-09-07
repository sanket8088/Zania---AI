import os
import fitz

class PDFParser:
    def __init__(self, path: str):
        self.file_path = path
        self.__validate_pdf()

    def __validate_pdf(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File {self.file_path} does not exist.")
        if not self.file_path.lower().endswith('.pdf'):
            raise ValueError(f"File {self.file_path} is not a valid PDF.")

    def extract_text(self):
        """Extracts text from the PDF document."""
        try:
            text = ""
            with fitz.open(self.file_path) as doc:
                for page_num in range(doc.page_count):
                    page = doc[page_num]
                    text += page.get_text("text")
            return text
        except Exception as e:
            raise RuntimeError(f"Error processing PDF file: {str(e)}")