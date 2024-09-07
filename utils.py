import textwrap

def chunk_text(text: str, chunk_size: int = 2000) -> list:
        """Divide text into chunks of a specified size."""
        return textwrap.wrap(text, chunk_size)