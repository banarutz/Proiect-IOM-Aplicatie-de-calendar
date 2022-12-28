from constants import *
from imports import *

######################################
# Date is formatted as month/day/year#
######################################

root = Tk()
root.title(APP_TITLE)
root.iconbitmap(APP_ICON)
root.geometry('600x400')

cal = Calendar(root, selectmode='day', year=DEFAULT_YEAR, month=DEFAULT_MONTH, day=DEFAULT_DAY)
cal.pack()


def InsertEvent():  # Momentan insereaza un singur eveniment
    # global EventInfo, data
    data = cal.get_date()
    event = InsertEventText.get(1.0, END)  # EVENTUL ARE UN \N DUPA EL, NU STIU DE CE? TREBUIE SCOS
    formatted_event = event.rstrip(event[-1])
    InsertedData = [data, formatted_event]
    print(InsertedData)
    # my_label.config (InsertedData)
    with open('EventData.csv', 'a') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow([data, formatted_event])
    RemoveTextBoxAndButton()  # Functie care scoate text box-ul si anunta ca evenimentul a fost introdus cu succes!


def ShowInsertEventTextBox():
    global InsertIntoCSVButton, InsertEventLabel, data, InsertEventText
    InsertEventLabel = Label(root, text='Introduceți evenimentul:')
    InsertEventLabel.place(x=125, y=235)
    InsertEventText = Text(root, height=5, width=25)
    InsertEventText.place(x=125, y=260)
    InsertIntoCSVButton = Button(root, text='Introduceti textul', command=InsertEvent)
    InsertIntoCSVButton.place(x=125, y=350)


def RemoveTextBoxAndButton():
    InsertIntoCSVButton.place_forget()
    InsertEventText.place_forget()
    InsertEventLabel.place_forget()


def speech_event():
    global EventData
    EventData = GetAllScheduledEvents()
    current_events = EMPTY_STRING
    for event_date, text in EventData:
        if event_date == cal.get_date():
            current_events = current_events + text + ", "
    ReadEventText(current_events)
    RemoveTextBoxAndButton()


def GetAllScheduledEvents():
    schedule = []
    with open('EventData.csv', 'r') as file:
        scheduled_events = csv.reader(file)
        for row in scheduled_events:
            schedule.append((row[0], row[1]))
    return schedule


def ReadEventText(text):
    try:
        eventRead = gTTS(text, lang="en-US", slow=False)
        eventRead.save("event.mp3")
        playsound('event.mp3')
    except:
        my_label.config(text="Something went wrong")


def grab_date():
    my_label.config(text=DATE_LABEL_TEXT + cal.get_date())


InsertEventButton = Button(root, text=INSERT_BUTTON_TEXT, command=ShowInsertEventTextBox).place(x=125, y=200)
SpeechEventButton = Button(root, text=SPEECH_BUTTON_TEXT, command=speech_event).place(x=350, y=200)

myButton = Button(root, text='Selectare data', command=grab_date)
myButton.pack(pady=20)

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
