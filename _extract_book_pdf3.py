import PyPDF2

pdf_path = 'Resource/1785405026411.pdf'
reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
total = len(reader.pages)

# Extract pages 40-70
for i in range(40, min(70, total)):
    text = reader.pages[i].extract_text()
    print(f'\n--- PAGE {i+1} ---')
    print(text[:2000])
