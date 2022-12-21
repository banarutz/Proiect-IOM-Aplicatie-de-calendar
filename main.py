from imports import *


root = Tk()
root.title('IOM project calendar')
root.iconbitmap('')
root.geometry('600x400')

cal = Calendar (root, selectmode = 'day', year = 2023, month = 1, day = 15)
cal.pack()

def grab_date ():
    my_label.config (text = "Today's date is: " + cal.get_date())

myButton = Button (root, text= 'Selectare data', command = grab_date)
myButton.pack(pady = 20)

my_label = Label (root, text='')
my_label.pack (pady = 20)

root.mainloop()