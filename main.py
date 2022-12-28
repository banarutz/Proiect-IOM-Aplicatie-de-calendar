from imports import *
from constants import *

######################################
# Date is formatted as month/day/year#
######################################

global EventData

root = Tk()
root.title(app_title)
root.iconbitmap(app_icon)
root.geometry('600x400')

cal = Calendar(root, selectmode='day', year=default_year, month=default_month, day=default_day)
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
    RemoveTextBoxAndButton()
    pass


def grab_date():
    my_label.config(text=date_label_text + cal.get_date())


InsertEventButton = Button(root, text=insert_button_text, command=ShowInsertEventTextBox).place(x=125, y=200)
SpeechEventButton = Button(root, text=speech_button_text, command=speech_event).place(x=350, y=200)

myButton = Button(root, text='Selectare data', command=grab_date)
myButton.pack(pady=20)

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
