import pdfplumber as pp
from gtts import gTTS

# 1. Extract text from pdf
pdf_text = ''

with pp.open('153877.pdf') as pdf:
    for page in pdf.pages:
        pdf_text += page.extract_text()

# 2. Convert extracted text to speech
tts = gTTS(text=pdf_text, lang='en')
tts.save('audio_book.mp3')
