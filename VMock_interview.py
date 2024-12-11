# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3 
import openai


# Set your OpenAI API key 
openai.api_key = "###"  

messages = [ {"role": "system", "content": "You are an intelligent chatbot to respond to text messages."} ]

def chat_with_chatgpt(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message["content"] 

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech

def SpeakText(command):   
    # Initialize the engine
    # engine = pyttsx3.init()
    engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[4].id)
    engine.say(command) 
    engine.runAndWait()
    
    
# Loop infinitely for user to
# speak

while(1):    
    
    # Exception handling to handleC:\Users\sharv\VMock_interview.py
    # exceptions at the runtime
    try:
        
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            #listens for the user's input 
            audio2 = r.listen(source2)
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print(MyText)
            
            output = chat_with_chatgpt(MyText)
            
            SpeakText(output)
            
    except sr.RequestError as e:
        print(f"Could not request results : {e}")
        
    except sr.UnknownValueError as e:
        # print("unknown error occurred")
        print(e)
        
        

