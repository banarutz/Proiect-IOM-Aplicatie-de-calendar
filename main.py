from constants import *
from imports import *

######################################
# Date is formatted as month/day/year#
######################################
root = Tk()
root.title(APP_TITLE)
root.iconbitmap(APP_ICON)
# root.geometry('600x600')
root.geometry('600x600')
root.resizable(False, False)
date = datetime.now()
cal = Calendar(root, selectmode='day', year=date.year, month=date.month, day=date.day)
cal.pack()

def open_file():
    global IntroducedEvent
    filepath = filedialog.askopenfilename(title = 'pen')
    file_name = filepath.split('/')[-1]
    InsertEventPath.insert (END, file_name)
    # aici introduce in text box

    SpeechRecognizer = sr.Recognizer()
    myaudiofile = sr.AudioFile(filepath)

    with myaudiofile as source:
        myaudio = SpeechRecognizer.record(myaudiofile)
        IntroducedEvent = SpeechRecognizer.recognize_google (myaudio, language = "ro-RO", show_all = False)
        print('Evenimentul introdus vocal este:', IntroducedEvent)

    InsertEventText.insert(END, IntroducedEvent)
    
    
def NewWindow(date, text):
    UpcomingEventsWindow = Toplevel()
    UpcomingEventsWindow.grab_set()
    UpcomingEventsWindow.title(NEXT_DAY_TITLE)
    UpcomingEventsWindow.resizable(False, False)
    UpcomingEventsWindow.geometry("350x350")
    EventsText = Text(UpcomingEventsWindow, width=40, height=20)
    EventsText.insert('end', "Evenimtentele din data de " + date + " sunt:\n")
    EventsText.insert('end', text)
    EventsText.configure(state='disabled')
    EventsText.place(x=10, y=10)


def CheckNextDayEvents():
    Events = GetAllScheduledEvents()
    tommorow = (date + timedelta(1)).strftime('%#m/%#d/%#y')
    current_events = ""
    index = 0
    for event_date, text in Events:
        if event_date == tommorow:
            index += 1
            current_events = current_events + str(index) + '.' + text + "\n"
    if current_events != "":
        NewWindow(tommorow, current_events)


def InsertEvent(): 
    global insert_label
    data = cal.get_date()
    event = InsertEventText.get(1.0, END)
    formatted_event = event.rstrip(event[-1])
    InsertedData = [data, formatted_event]
    print(InsertedData)
    with open('EventData.csv', 'a') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow([data, formatted_event])
    insert_label = Label(root, text='Eveniment introdus')
    insert_label.place(x=235, y=280)


def ShowInsertEventTextBox():
    global InsertIntoCSVButton, InsertEventLabel, data, InsertEventText
    remove_parts()
    InsertEventLabel = Label(root, text='Introduceți evenimentul:')
    InsertEventLabel.place(x=125, y=300)
    InsertEventText = Text(root, height=5, width=45)
    InsertEventText.place(x=125, y=320)
    InsertIntoCSVButton = Button(root, text='Introduceți textul', command=InsertEvent)
    InsertIntoCSVButton.place(x=125, y=420)

def ShowInsertVocalText():
    global InsertPathButton, InsertEventPath
    InsertEventPath = Text(root, height=3, width=25)
    InsertEventPath.place(x=125, y=510)
    InsertPathButton = Button(root, text='Introduceți calea către eveniment', command=open_file)
    InsertPathButton.place(x=125, y=475)


def speech_event():
    global EventData
    remove_parts()
    EventData = GetAllScheduledEvents()
    current_events = EMPTY_STRING
    for event_date, text in EventData:
        if event_date == cal.get_date():
            current_events = current_events + text + ", "
    ReadEventText(current_events)


def GetAllScheduledEvents():
    schedule = []
    global EventsText
    try:
        with open('EventData.csv', 'r') as file:
            scheduled_events = csv.reader(file)
            for row in scheduled_events:
                schedule.append((row[0], row[1]))
    except:
        print("No events yet!")
    return schedule


def ReadEventText(text):
    global date_label
    remove_parts()
    date_label = Label(root, text='')
    date_label.place(x=220, y=280)
    mp3 = BytesIO()
    mixer.init()
    try:
        eventRead = gTTS(text, lang="ro", slow=False)
        eventRead.write_to_fp(mp3)
        mixer.music.load(mp3, "mp3")
        mixer.music.play()
    except:
        date_label.config(text="Nu există evenimente pentru data selectată!")


def show_events():
    global EventsText
    remove_parts()
    Events = GetAllScheduledEvents()
    EventsText = Text(root, width=45, height=50)
    EventsText.insert('end', "Evenimtentele din data de " + cal.get_date() + " sunt:\n")
    index = 0
    for event_date, text in Events:
        if event_date == cal.get_date():
            index += 1
            numberOfEvent = str(index) + '.'
            EventsText.insert('end', numberOfEvent + text + '\n')
            
    # if index == 0:
    #     EventsText.insert(END, 'Nu există evenimente pentru data selectată!')
    EventsText.configure(state='disabled')
    EventsText.place(x=145, y=300)


def remove_parts():
    try:
        EventsText.place_forget()
    except:
        print("EventsText can't be deleted")
    try:
        date_label.place_forget()
    except:
        print("date_label can't be deleted")
    try:
        InsertIntoCSVButton.place_forget()
    except:
        print("InsertIntoCSVButton can't be deleted")
    try:
        InsertEventLabel.place_forget()
    except:
        print("InsertEventLabel can't be deleted")
    try:
        InsertEventText.place_forget()
    except:
        print("InsertEventText can't be deleted")
    try:
        insert_label.place_forget()
    except:
        print("insert_label can't be deleted")
    try:
        InsertEventPath.place_forget()
    except:
        print("InsertEventPath can't be deleted")
    try: 
        InsertPathButton.place_forget()
    except:
        print('InsertPathButton can\'t be deleted')
    

InsertEventButton = Button(root, text=INSERT_BUTTON_TEXT, command= lambda: [ShowInsertEventTextBox(), ShowInsertVocalText()]).place(x=125, y=200)
# InsertVocalEventButton = Button(root, text=INSERT_VOCAL_BUTTON_TEXT, command = ShowInsertVocalText).place(x=125, y = 500)
SpeechEventButton = Button(root, text=SPEECH_BUTTON_TEXT, command=speech_event).place(x=350, y=200)
ShowEventsButton = Button(root, text=SHOW_EVENTS_BUTTON_TEXT, command=show_events).place(x=235, y=245)

CheckNextDayEvents()
root.mainloop()
