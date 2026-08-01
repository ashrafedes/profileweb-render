import PyPDF2

pdf_path = 'Resource/1785405026411.pdf'
reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
total = len(reader.pages)

# Extract pages 70-end
for i in range(70, min(total, 110)):
    text = reader.pages[i].extract_text()
    print(f'\n--- PAGE {i+1} ---')
    print(text[:2000])
