import os, sys, tempfile, traceback
from pathlib import Path
from PIL import Image
from pypdf import PdfReader, PdfWriter

resources = Path(__file__).parent.resolve()
out_pdf = resources / 'consolidated_application_support.pdf'
tmpdir = Path(tempfile.mkdtemp())

def file_to_pdf(src, tmp_root):
    suffix = src.suffix.lower()
    if suffix == '.pdf':
        return str(src)
    if suffix in ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif', '.webp'):
        out = tmp_root / (src.stem + '.pdf')
        img = Image.open(src)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.save(out, 'PDF', resolution=100.0)
        return str(out)
    if suffix == '.docx':
        print(f'  Skipping DOCX (will handle separately): {src.name}')
        return None
    print(f'Skipping unsupported file type: {src.name}')
    return None

files = [f for f in resources.iterdir() if f.is_file() and f != out_pdf and not f.name.startswith('_')]

def sort_key(f):
    lower = f.name.lower()
    if 'badge' in lower or 'certif' in lower or 'award' in lower or 'apprec' in lower or 'تقدير' in lower or 'شهادة' in lower:
        return (0, lower)
    if 'cv' in lower or 'سيرة' in lower or 'curriculum' in lower:
        return (2, lower)
    if 'profile' in lower and lower.endswith('.pdf'):
        return (3, lower)
    return (1, lower)

files.sort(key=sort_key)

writer = PdfWriter()
bookmarks = []
for f in files:
    print(f'Processing: {f.name} ...', flush=True)
    try:
        pdf_path = file_to_pdf(f, tmpdir)
        if not pdf_path:
            continue
        reader = PdfReader(pdf_path)
        start_page = len(writer.pages)
        for page in reader.pages:
            writer.add_page(page)
        end_page = len(writer.pages)
        bookmarks.append((f.name, start_page))
        print(f'  OK: {f.name} ({end_page - start_page} pages)', flush=True)
    except Exception as e:
        print(f'  ERROR processing {f.name}: {e}', flush=True)
        traceback.print_exc()

for title, page in bookmarks:
    writer.add_outline_item(title, page)

with open(out_pdf, 'wb') as fout:
    writer.write(fout)

print(f'\nConsolidated PDF saved: {out_pdf}')
print(f'Total pages: {len(writer.pages)}')
print(f'Total files included: {len(bookmarks)}')
