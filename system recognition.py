import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Bom dia")

    elif hour>=12 and hour<18:
        speak("Boa Tarde")   

    else:
        speak("Boa noite")  

    speak("Eu sou seu assistente virtual, no que posso ajudar?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escutando...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconhecendo...")    
        query = r.recognize_google(audio, language='pt-BR')
        print(f"Jarvis: {query}\n")

    except Exception as e:
        # print(e)    
        print("Poderia repetir...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('stormdorgado@gmail.com', 'joas1211')
    server.sendmail('stormdorgado@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Pesquisando no wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("De acordo com wikipedia")
            print(results)
            speak(results)

        elif 'abrir youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'abrir google' in query:
            webbrowser.get(chrome_path).open("google.com")

        elif 'abrir jw' in query:
            webbrowser.get(chrome_path).open("jw.org")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'horas' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Senhor, agora são {strTime}")

        elif 'abrir codigo' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email para felipe' in query:
            try:
                speak("O que devo dizer?")
                content = takeCommand()
                to = "felipe.fg01.fg@gmail.com"    
                sendEmail(to, content)
                speak("Email enviado!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    
        elif 'sair' in query:
            break
