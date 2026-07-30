import PyPDF2

pdf_path = 'Resource/Kluwer - Project Management for Telecommunication Managers.pdf'
reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
total = len(reader.pages)
print(f'Total pages: {total}')

# Extract pages 1-11 for table of contents
for i in range(0, 11):
    text = reader.pages[i].extract_text()
    print(f'\n--- PAGE {i+1} ---')
    print(text[:3000])

# Extract sample pages from middle chapters
for i in [20, 21, 50, 51, 100, 101, 150, 151, 200, 201, 250, 251, 300, 301]:
    if i < total:
        text = reader.pages[i].extract_text()
        print(f'\n--- PAGE {i+1} ---')
        print(text[:2000])
