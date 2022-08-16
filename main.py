import pyttsx3
import webbrowser
import datetime
import PyPDF2
engine = pyttsx3.init()
books = ['book','bad','good']
inp=input('enter what should be said to the assistant').lower()
def greeting(inp):
    if inp == 'hello':
        text='hi there'
    elif inp == 'how are you':
        text = 'i am doing fine'
    elif inp == 'good morning':
        text = 'rise and shine'
    else:
        text = ''
    engine.say(text)
    engine.runAndWait()
def websites(inp):
    if inp == 'open google':
        url = 'google.com'
        text = 'opening google dot com'
    elif inp == 'open youtube':
        url = 'youtube.com'
        text = 'opening youtube dot com'
    elif inp == 'open gmail':
        url = 'gmail.com'
        text = 'opening gmail dot com'
    else:
        text = ''
        url = ''
    webbrowser.open_new_tab(url)
    engine.say(text)
    engine.runAndWait()
def questions(inp):
    if inp == 'what is bill gates net worth':
        text = 'one hundred and fourteen point two billion dollars'
    elif inp =='what is the best show of all time':
        text = 'breaking bad directed by vince gilligan'
    elif inp =='who is the president of the united states':
        text = 'joe biden'
    elif inp =='what is the day today':
        text = 'the date today is' + str(datetime.datetime.today())
    elif inp =='what year was the uae founded':
        text = 'nineteen seventy one '
    else:
        text = ''
    engine.say(text)
    engine.runAndWait()
def narrator(inp):
    if inp == 'read a file':
        engine.say(text='enter the file name which should be read')
        engine.runAndWait()
        book= input('enter')
        if book in books:
            reader = book + '.pdf'
            pdfreader=PyPDF2.PdfFileReader(open(reader,'rb'))
            for pagenumber in range(pdfreader.numPages):
                text = pdfreader.getPage(pagenumber).extractText()
                engine.say(text)
                engine.runAndWait()
            engine.stop()
        else:
            engine.say(text='book does not exist')
            engine.runAndWait()
greeting(inp)
websites(inp)
questions(inp)
narrator(inp)
