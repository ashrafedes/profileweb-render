import PyPDF2

pdf_path = 'Resource/Kluwer - Project Management for Telecommunication Managers.pdf'
reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
print(f'Total pages: {len(reader.pages)}')
if reader.metadata:
    print(f'Title: {reader.metadata.title}')
    print(f'Author: {reader.metadata.author}')

# Extract first 15 pages to understand structure
for i in range(min(15, len(reader.pages))):
    text = reader.pages[i].extract_text()
    print(f'\n--- PAGE {i+1} ---')
    print(text[:2000])
