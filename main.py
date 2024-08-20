import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
#pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak (text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
        speak("opening google")
    elif "search in google" in command.lower():
        search_query = command.replace("search in google","").strip() #remove space or newlines  # Extract the search query
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        speak(f"Searching for {search_query} in google")
        
    elif "open instagram" in command.lower():
        webbrowser.open("https://instagram.com")
        speak("opening instagram")
        
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com") 
    
    elif "open github" in command.lower():
        webbrowser.open("https://github.com")    
        speak("opening nerd site")   
     
    elif command.lower(). startswith ("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
   
    
    
if __name__=="__main__":
    speak("Initializing jarvis.... ")
    while True:
     #listen for wake word "X"
     #obtain audio from microphone
        r=sr.Recognizer()
        
        print("recognizing...")
        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
                audio = r.listen(source, timeout=3, phrase_time_limit=  3)
                word = r.recognize_google(audio)
                print(f"recognized word: {word} ")
            
            if(word.lower()=="jarvis"):
                speak("Yes bro")
                #listen command
                with sr.Microphone() as source:
                    speak ("jarvis is active...")
                    print("activated, listening for commands...")
                    audio = r.listen(source, timeout=3, phrase_time_limit=3)
                    command = r.recognize_google(audio)
                    print(f"recognized command: {command}")
                    
                    processCommand(command)
            #recognize_google is a function works better than
            # sphinx or cloud
                
                #error handling
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(" error; {0}".format(e))
