import PyPDF2

pdf_path = 'Resource/1785405026411.pdf'
reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
total = len(reader.pages)

# Extract pages 110-end
for i in range(110, total):
    text = reader.pages[i].extract_text()
    print(f'\n--- PAGE {i+1} ---')
    print(text[:2000])
