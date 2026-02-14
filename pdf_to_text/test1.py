import pdfplumber
import pytesseract
from pdf2image import convert_from_path


PDF_PATH = "CVmalakSobhy.pdf"

def is_scanned_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text and len(text.strip()) > 50:
                return False
    return True


def extract_scanned_pdf_text(pdf_path):
    images = convert_from_path(pdf_path, dpi=300)
    full_text = ""

    for img in images:
        img = img.convert("L")
        text = pytesseract.image_to_string(
            img,
            lang="eng",
            config="--oem 3 --psm 6"
        )
        full_text += text + "\n"

    return full_text


if __name__ == "__main__":
    if is_scanned_pdf(PDF_PATH):
        print("Scanned PDF detected → Using OCR")
        text = extract_scanned_pdf_text(PDF_PATH)
    else:
        print("Not scanned (unexpected case)")

    with open("cv_output.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("Done ✅")
