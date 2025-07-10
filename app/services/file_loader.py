import fitz

def extract_text_from_pdf(file_path: str) -> str:
    try:
        doc = fitz.open(file_path)
        full_text = []

        for page in doc:
            text = page.get_text()
            if text.strip():
                full_text.append(text)

        return "\n".join(full_text)

    except Exception as e:
        print(f"[ERROR] Failed to extract text from PDF: {e}")
        return ""