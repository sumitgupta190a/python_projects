# pip install pyttsx3
import speech_recognition as sr
import pyttsx3

def say(text):
    engine = pyttsx3.init()  # This starts the tool.
    engine.say(text)        # This tells the tool what text to say.
    engine.runAndWait()     # This makes the tool actually speak the text.
    
def takecommand():
    r = sr.Recognizer()

    

if __name__ == '__main__':
    while 1:
        # say("Hello, I am Jarvis, an A.I. created by Sumit.")
        s = input()
        
