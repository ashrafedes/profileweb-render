import PyPDF2

pdf_path = 'Resource/012017-4-6-pp.1-13.pdf'
reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
print(f'Total pages: {len(reader.pages)}')
if reader.metadata:
    print(f'Title: {reader.metadata.title}')
    print(f'Author: {reader.metadata.author}')

for i in range(len(reader.pages)):
    text = reader.pages[i].extract_text()
    print(f'\n--- PAGE {i+1} ---')
    print(text[:3000])
