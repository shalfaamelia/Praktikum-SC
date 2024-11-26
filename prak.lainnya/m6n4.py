import pyttsx3

engine = pyttsx3.init()

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')

rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 70)

volume = engine.getProperty('volume')
engine.setProperty('volume', volume * 0.5)

engine.say("buenos dias como estas amigo?")
engine.runAndWait()