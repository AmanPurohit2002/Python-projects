import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyaudio
import datetime

r=sr.Recognizer()

def speak(command):
    engine=pyttsx3.init()  # give text to speech
    voices= engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening... Ask now ...")

            audio_in=r.listen(source)

            my_text=r.recognize_google(audio_in)
            my_text=my_text.lower()
            print(my_text)
            # speak(my_text)

            # 1- > ask to play song
            if 'play' in my_text:
                my_text=my_text.replace("play",'')
                print(my_text)
                speak("Playing "+ my_text)
                pywhatkit.playonyt(my_text)


            # 2--> ask date

            elif "date" in my_text:
                today=datetime.date.today()
                speak(today)

            # 3--> ask time

            elif "time" in my_text:
                time=datetime.datetime.now().strftime("%H:%M")
                speak(time)


            # 4--> ask details about an other person

            elif "who is" in my_text:
                person=my_text.replace("who is","")
                info=wikipedia.summary(person,1)
                speak(info)

            else:
                speak("Please ask correct question")


    except :

        print("Error in capturing microphone ...")

# speak("Welcome to the Project")

while True:
    commands()



