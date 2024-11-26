from gtts import gTTS
from playsound import playsound
import os

def speak(text):
    tts = gTTS(text=text, lang='id')
    filename = "temp_audio.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)  

nama = input("Masukkan nama Anda: ")

if nama:
    speak(f"Baik {nama}, silakan memilih menu selanjutnya")
    
    hobi = input("Masukkan hobi Anda: ")
    
    if hobi:
        speak(f"Wow, hobi anda adalah {hobi}")
    else:
        pass

speak("Terima kasih")