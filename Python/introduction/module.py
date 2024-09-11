import pyjokes
# print("printing_jokes----")
joke = pyjokes.get_joke()
print(joke) 

import pyttsx3
engine = pyttsx3.init()
engine.say("teri maa ki chut")
engine.runAndWait()