import PyPDF2

pdf_path = 'Resource/Cyber Security Essentials ( PDFDrive ).pdf'
reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
total = len(reader.pages)

# Extract pages 10-15 for more TOC and chapter starts
for i in range(9, 15):
    text = reader.pages[i].extract_text()
    print(f'\n--- PAGE {i+1} ---')
    print(text[:3000])

# Extract sample pages from key chapters
for i in [20, 50, 80, 120, 150, 200, 250, 300, 350, 400]:
    if i < total:
        text = reader.pages[i].extract_text()
        print(f'\n--- PAGE {i+1} ---')
        print(text[:2000])
