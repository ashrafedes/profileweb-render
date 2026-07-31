import PyPDF2

pdf_path = 'Resource/Cyber Security Essentials ( PDFDrive ).pdf'
reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
total = len(reader.pages)
print(f'Total pages: {total}')
if reader.metadata:
    print(f'Title: {reader.metadata.title}')
    print(f'Author: {reader.metadata.author}')

# Extract first 10 pages for TOC/structure
for i in range(min(10, total)):
    text = reader.pages[i].extract_text()
    print(f'\n--- PAGE {i+1} ---')
    print(text[:3000])
