import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Silakan bicara...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language='id')
            print(f"Anda berkata: {text}")
            return text
        except:
            return None

def main():
    print("Input suara [nama]:")
    name = listen()

    if name:
        print(f"Baik, Selamat datang {name}, silakan memilih menu selanjutnya")
        print("Input suara [hobi]:")
        hobi = listen()

        if hobi:
            print(f"Waw keren, hobi anda adalah {hobi}")
            print("Terima kasih")

if __name__ == "__main__":
    main()