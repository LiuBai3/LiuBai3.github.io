import PyPDF2

with open('2026-课程大作业1.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()

print(text)