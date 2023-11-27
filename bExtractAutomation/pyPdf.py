from PyPDF2 import PdfReader
# from pdfminer.high_level import extract_text as fallback_text_extraction

text = ""
reader = PdfReader("medical bill.pdf")
for page in reader.pages:
    text += page.extract_text()
    # print("asdf")
    # text = fallback_text_extraction("example.pdf")
print(text)