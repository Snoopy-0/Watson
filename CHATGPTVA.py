# python Program to translate
# speech to text and text to speech
import speech_recognition as sr 
import pyttsx3

import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = " Enter OPENAI_API_KEY here"

from openai import OpenAI

client = OpenAI(api_key=OPENAI_KEY)

# Function to convert text to 
# Speech
def SpeakText(command):
    
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Initialize the recognizer
r= sr.Recognizer()

def record_text():
# Loop in case of errors
    while(1):
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:

                #prepare recognize to recieve text
                r.adjust_for_ambient_noise(source2,duration=0.2)

                print("I'm Listening")

                # listens for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                print("Schmozelstien: " + MyText)
                return MyText
            
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        
        except sr.UnknownValueError:
            print("unknown error occured")

def send_to_chatGPT(messages, model="gpt-3.5-turbo"):

    response = client.chat.completions.create(model=model,
    messages=messages,
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.5)

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message
    
messages = []
while[1]:
    text = record_text()
    messages.append({"role": "user", "content": text})
    response = send_to_chatGPT(messages)
    SpeakText(response)
    print("GPT: " + response)