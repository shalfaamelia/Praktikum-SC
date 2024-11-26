from gtts import gTTS
from playsound import playsound

tts = gTTS(text="Selamat pagi Amel", lang="id", slow=True)
tts.save("morning.mp3")
playsound("morning.mp3")