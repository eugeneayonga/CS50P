import cowsay
import pyttsx3

engine = pyttsx3.init()

phrase = input("Enter phrase: ")

cowsay.cow(phrase)
engine.say(phrase * 46)
engine.runAndWait()

