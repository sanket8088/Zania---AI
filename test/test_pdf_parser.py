import pytest
import os
from PDFParser import PDFParser  # Import your PDFParser class

class TestPDFParser:

    @pytest.fixture(autouse=True)
    def setup_files(self, tmpdir):
        """Create test files for PDFParser tests"""
        self.valid_pdf_path = "test/fixture/handbook.pdf"
        self.invalid_file_path = "test/fixture/invalid_file.txt"

        # Create a valid PDF file with simple text content

    def test_pdf_validation_success(self):
        """Test PDF validation when the file exists and is valid"""
        parser = PDFParser(self.valid_pdf_path)
        assert parser.file_path == self.valid_pdf_path
    
    def test_pdf_not_found(self):
        """Test that FileNotFoundError is raised when the file does not exist"""
        with pytest.raises(FileNotFoundError):
            PDFParser("non_existent_file.pdf")
    
    def test_invalid_file_format(self):
        """Test that ValueError is raised when file is not a PDF"""
        with pytest.raises(ValueError):
            PDFParser(self.invalid_file_path)
    
    def test_extract_text_success(self):
        """Test that extract_text correctly reads data from a PDF and starts with 'Zania, Inc'"""
        parser = PDFParser(self.valid_pdf_path)
        extracted_text = parser.extract_text()
        assert extracted_text.startswith("Zania, Inc")

