import PyPDF2

pdf_path = 'Resource/Kluwer - Project Management for Telecommunication Managers.pdf'
reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
total = len(reader.pages)

# Extract table of contents pages (typically pages 5-11)
for i in range(4, 11):
    text = reader.pages[i].extract_text()
    print(f'\n--- PAGE {i+1} ---')
    print(text[:3000])

# Extract chapter start pages
for i in range(150, 310, 50):
    if i < total:
        text = reader.pages[i].extract_text()
        print(f'\n--- PAGE {i+1} ---')
        print(text[:1500])

# Last pages
for i in range(total-5, total):
    text = reader.pages[i].extract_text()
    print(f'\n--- PAGE {i+1} ---')
    print(text[:1500])
