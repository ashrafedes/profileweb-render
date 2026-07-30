import PyPDF2

pdf_path = 'Resource/Kluwer - Project Management for Telecommunication Managers.pdf'
reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
total = len(reader.pages)

# Extract pages 5-8 for full TOC
for i in range(4, 8):
    text = reader.pages[i].extract_text()
    print(f'\n--- PAGE {i+1} ---')
    print(text)

# Extract key chapter pages for content details
chapter_pages = [24, 25, 70, 71, 114, 115, 152, 153, 172, 173, 210, 211, 226, 227, 236, 237, 244, 245, 248, 249, 258, 259, 260, 261]
for i in chapter_pages:
    if i < total:
        text = reader.pages[i].extract_text()
        print(f'\n--- PAGE {i+1} ---')
        print(text[:2000])
