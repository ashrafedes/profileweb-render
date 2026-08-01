import PyPDF2

pdf_path = 'Resource/1785405026411.pdf'
reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
total = len(reader.pages)

# Extract pages 15-40 for more content
for i in range(15, min(40, total)):
    text = reader.pages[i].extract_text()
    print(f'\n--- PAGE {i+1} ---')
    print(text[:2500])
