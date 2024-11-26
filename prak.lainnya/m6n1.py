from gtts import gTTS
from playsound import playsound

tts = gTTS(text="Good Morning Amel", lang="en")
tts.save("morning.mp3")
playsound("morning.mp3")