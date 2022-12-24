from imports import *
######################################
# Date is formatted as month/day/year#
######################################

global EventData

root = Tk()
root.title('IOM project calendar')
root.iconbitmap('')
root.geometry('600x400')

cal = Calendar (root, selectmode = 'day', year = 2023, month = 1, day = 15)
cal.pack()


def InsertEvent (): # Momentan insereaza un singur eveniment 
    # global EventInfo, data
    data = cal.get_date()   
    event = InsertEventText.get(1.0, tk.END) # EVENTUL ARE UN \N DUPA EL, NU STIU DE CE? TREBUIE SCOS
    InsertedData = [data, event]
    print(InsertedData)
    # my_label.config (InsertedData)
    with open('EventData.csv', 'w') as file:
        writer = csv.writer(file, lineterminator= '\n')
        writer.writerow([data, event])
    RemoveTextBoxAndButton()
    # Functie care scoate text box-ul si anunta ca evenimentul a fost introdus cu succes!


def ShowInsertEventTextBox ():
    global InsertIntoCSVButton, InsertEventLabel, data, InsertEventText
    InsertEventLabel = Label (root, text = 'Introduceți evenimentul:')
    InsertEventLabel.place (x = 125, y = 235)
    InsertEventText = Text(root, height = 5, width = 25)
    InsertEventText.place( x = 125, y = 260)
    InsertIntoCSVButton = Button (root, text= 'Introduceti textul', command = InsertEvent)
    InsertIntoCSVButton.place (x = 125, y = 350)

def RemoveTextBoxAndButton():
    InsertIntoCSVButton.place_forget()
    InsertEventText.place_forget()
    InsertEventLabel.place_forget()

def speech_event ():
    RemoveTextBoxAndButton()
    pass

InsertEventButton = Button (root, text= 'Insereaza eveniment', command = ShowInsertEventTextBox).place (x = 125, y = 200)
SpeechEventButton = Button (root, text= 'Rostește eveniment', command = speech_event).place (x = 350, y = 200)

# myButton.pack(pady = 20)

def grab_date ():
    my_label.config (text = "Today's date is: " + cal.get_date())

myButton = Button (root, text= 'Selectare data', command = grab_date)
myButton.pack(pady = 20)

my_label = Label (root, text='')
my_label.pack (pady = 20)

root.mainloop() 