

import speech_recognition as sr
import time

r = sr.Recognizer()

with sr.AudioFile('C:\\Users\\CECILIA\\OneDrive\\Escritorio\\Reconocimiento de voz - Grabación a Texto\\prueba3.wav') as source:
    
    audio = r.listen(source)

    try:
        print("Preparando el archivo de audio. Por favor, espere un momento...")
        text = r.recognize_google(audio, language='es-ES')
        time.sleep(1.5)
        print(text)
    except:
        print("Lo siento no puedo entenderte!")


#C:\\Users\\CECILIA\\OneDrive\\Escritorio\\Reconocimiento de voz - Grabación a Texto\\prueba3.wav

        




       
