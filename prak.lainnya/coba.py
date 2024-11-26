import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Tampilkan semua suara yang tersedia
for voice in voices:
    print(f"Voice: {voice.name}, ID: {voice.id}, Languages: {voice.languages}")