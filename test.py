import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha
import time
import re
from selenium import webdriver

engine=pyttsx3.init()
wolframalpha_app_id='5K24LY-8RE5JPP3H7'
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time_():
    time1=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time  ")
    speak(time1)
def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak(date)
    speak(month)
    speak(year)
def wishme():
    speak("hello anudeep")
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
    elif hour>=18 and hour<24:
        speak("good evening sir")
    else:
        speak("good night sir")

    speak("james at your service please tell me how can i help you today")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening ......")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("say that again sir please...")
        return "None"
    return query
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com',to,content)
    server.close()
def screenshot():
    img=pyautogui.screenshot()
    img.save('C:/Users/Sai Ram/Pictures/Screenshots/Screenshot.png')


def cpu():
    usage=str(psutil.cpu_percent())
    speak("spu usage sir"+usage)
    battery=psutil.sensors_battery()
    speak("battery is at sir")
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())


if __name__ == '__main__':
    while True:
        query=takecommand().lower()
        if 'hello james' in query:
            wishme()
        elif "time" in query:
            time1 = datetime.datetime.now().strftime("%I:%M:%S")
            speak("the current time  ")
            speak(time1)

        elif "date" in query:
            date_()
        elif 'wikipedia' in query:
            speak("searching .......")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("what should i send")
                content=takecommand()
                speak("who is the reciever")
                reciever=input("enter reciever's email")
                to=reciever
                sendemail(to,content)
                speak(content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("unable to send email")

        elif 'chrome' in query:
            speak('what should i search sir')
            chromepath='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search=takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')


        elif 'search youtube' in query:
            speak("what should i search sir")
            search_Term=takecommand().lower()
            speak('here we go to youtube sir')
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search google' in query:
            speak("what should i search sir")
            search_Term=takecommand().lower()
            speak("searching....... sir")
            wb.open('https://www.google.com/search?q='+search_Term)
        elif 'thank you' in query:
            speak("it's my pleasure sir")
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            joke()
        elif 'go offline' in query:
            speak('going offline sir!')
            quit()
        elif 'word' in query:
            speak("opening ms word sir")
            ms_word=r'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/Microsoft Office Word 2007.lnk'
            os.startfile(ms_word)
        elif 'write a note' in query:
            speak("what should i write,sir?")
            notes=takecommand()
            file=open('notes.txt','w')
            speak("sir should i include date and time")
            ans=takecommand()
            if 'yes' in ans or 'sure' in ans or 's' in ans:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(":-")
                file.write(notes)
                speak("done taking notes,sir")
            else:
                file.write(notes)
        elif 'show note' in query:
            speak("showing notes sir")
            file=open('notes.txt','r')
            print(file.read())
            speak(file.read())
        elif 'screenshot' in query:
            screenshot()
        elif 'play music' in query:
            songs_dir='C:/Users/Sai Ram/Music/tamil songs/New folder'
            music=os.listdir(songs_dir)
            speak("what should i play")
            speak("select a number")
            ans=takecommand().lower()
            while('number' not in ans and ans!='random' and ans!='you choose'):
                speak("i could not understand you .please say again sir")
                ans=takecommand().lower()
            if 'number' in ans:
                no=int(ans.replace('number',''))
            elif 'random' or 'you choose' in ans:
                no=random.randint(1,20)
            os.startfile(os.path.join(songs_dir,music[no]))
        elif 'i need something to focus' in query:
            speak("you should say that first")
            songs_dir='C:/Users/Sai Ram/Music/tamil songs/New folder'
            music=os.listdir(songs_dir)
            no=random.randint(1,50)
            os.startfile(os.path.join(songs_dir,music[no]))
        elif 'what did you say now' in query:
            speak("nothing sir")
        elif 'you are doing too much' in query:
            speak('not more than you sir')

        elif 'play another song' in query:
            speak("what about this ")
            songs_dir = 'C:/Users/Sai Ram/Music/tamil songs/New folder'
            music = os.listdir(songs_dir)
            no = random.randint(1, 50)
            os.startfile(os.path.join(songs_dir, music[no]))
        elif 'hit some music' in query or 'music' in query:
            speak("would you like this")
            songs_dir = 'C:/Users/Sai Ram/Music/tamil songs/New folder'
            music = os.listdir(songs_dir)
            no = random.randint(1,50)
            os.startfile(os.path.join(songs_dir, music[no]))
        elif 'remember that' in query:
            speak("what should i remember")
            memory=takecommand()
            speak("you asked to remember that"+memory)
            remember=open('memory.txt','w')
            remember.write(memory)
            remember.close()
        elif 'do you remember anything' in query:
            remember=open('memory.txt','r')
            speak("you asked me to remember that"+remember.read())

        elif 'news' in query:
            try:
                jsonObj=urlopen("https://news.google.com/topstories?tab=mn&hl=en-IN&gl=IN&ceid=IN:en")
                data=json.load(jsonObj)
                i=1
                speak("here are some top headlines")
                print("-------------top headlines---"+'\n')
                for item in data['articles']:
                    print(str(i)+'_'+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i+=1
            except Exception as e:
                print(str(e))
        elif 'where is' in query:
            query=query.replace('where is','')
            location=query
            speak("user asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/"+location)

        elif 'calculate' in query:
            client=wolframalpha.Client(wolframalpha_app_id)
            indx=query.lower().split().index('calculate')
            query=query.split()[indx+1:]
            res=client.query("".join(query))
            answer=next(res.results).text
            print('the answer is :'+answer)
            speak('the answer is '+answer)
        elif 'what is' in query or 'who is' in query:
            client=wolframalpha.Client(wolframalpha_app_id)
            res=client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("no results")


        elif 'stop listening' in query:
            speak("for how many seconds you want me to stop listening to your command sir")
            ans=int(takecommand())
            time.sleep(ans)
            print(ans)
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif  'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif "good bye" in query or "ok bye" in query or "stop" in query:
            speak('your personal assistant mark is shutting down,Good bye sir')
            print('your personal assistant mark is shutting down,Good bye sir')
            break
        elif 'open gmail' in query:
            wb.open_new_tab("https://mail.google.com/")
            speak("Google Mail open now sir")
            time.sleep(5)
        elif 'search' in query:
            statement = query.replace("search", "")
            wb.open_new_tab(statement)
            time.sleep(5)
        elif 'ask' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question = takecommand()
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        elif 'who are you' in query or 'what can you do' in query:
            speak('I am james version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by anudeep")
            print("I was built by anudeep")
        elif 'tell me about' in query:
            reg_ex = re.search('tell me about (.*)', query)
            try:
                if reg_ex:
                    topic = reg_ex.group(1)
                    ny = wikipedia.page(topic)
                    speak(ny.content[:500].encode('utf-8'))
            except Exception as e:
                speak(e)

        elif 'open google' in query:
            speak("opening google sir")
            wb.open_new_tab("www.google.com")
        elif 'open youtube' in query:
            speak("opening youtube sir")
            wb.open_new_tab('www.youtube.com')
        elif 'open facebook' in query:
            speak('looks like you are all caught up sir')
            wb.open_new_tab('https://www.facebook.com/')
        elif 'go to sleep' in query:
            speak("as yoou like sir")
            quit()
        elif 'wake up' in query:
            speak('online and ready sir')
        elif 'i hate you so much' in query:
            speak("it's my pleasure sir")
        elif 'open whatsapp' in query:
            speak("opening whatsapp sir")
            wb.open_new_tab("https://web.whatsapp.com/")
        elif 'brother' in query:
            speak("your brother sairam")
















