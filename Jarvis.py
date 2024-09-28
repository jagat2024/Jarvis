import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am your jarvis sir, please let me know how may I help you sir")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Processing ...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir said: {query}\n")
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sraghaw130@gmail.com', '9433977471')
    server.sendmail('sraghaw130@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")    

        elif 'open drive' in query:
            webbrowser.open("https://drive.google.com/drive/u/0/my-drive")    

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com/")    

        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=486386870127&hvpos=&hvnetw=g&hvrand=855387192114904562&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=20472&hvtargid=kwd-10573980&hydadcr=14453_2154373&gclid=CjwKCAjwhaaKBhBcEiwA8acsHAj5ZPqTX5NodhQVtcFIdmFvdumqB2BJIg55-Yb57BXJvkXkq5GpZxoCdxMQAvD_BwE")  

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")       
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open maths' in query:
            webbrowser.open("https://byjus.com/ncert-solutions-class-11-maths/")     

        elif 'what is the temperature' in query:
            webbrowser.open("https://weather.com/en-IN/weather/today/l/bc58512ac5255d8eb962ce2ab32db3b949f44aa7143ef6c44891ac39258a10fb")    
        
        elif 'open mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?ogbl#inbox") 
            
        elif 'open map' in query:
            webbrowser.open("https://www.google.co.in/maps/place/23%C2%B000'44.6%22N+88%C2%B024'48.5%22E/@23.0118882,88.4132775,180m/data=!3m1!1e3!4m6!3m5!1s0x39f8eb43746b8b83:0x6818455d3dae1195!7e2!8m2!3d23.012391!4d88.4134828")

        elif 'open index' in query:
           webbrowser.open("https://pypi.org/") 

        elif 'play movie' in query:
           webbrowser.open("https://www.hotstar.com/in")

        elif 'play music' in query:
           webbrowser.open("https://www.youtube.com/watch?v=rtTI1rh9U5M")

        elif 'open village' in query:
           webbrowser.open("https://www.google.co.in/maps/place/Sonkali+Yadunandan+Vansi/@25.5655224,82.9460482,223m/data=!3m1!1e3!4m5!3m4!1s0x3991d5425c1a2d6b:0x3d5abba8fd9e56b3!8m2!3d25.5655891!4d82.9467072")  

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email to Sam' in query:
            try:
                speak("What should I say sir?")
                content = takeCommand()
                to = "sam689533977471@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email Can you Say that again please.")