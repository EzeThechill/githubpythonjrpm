import PyPDF2

with open("abc.pdf", "rb") as f:
    pdf_reader = PyPDF2.PdfReader(f)

    num_pages = len(pdf_reader.pages)

    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        print(text)
        print("-------------------")
    