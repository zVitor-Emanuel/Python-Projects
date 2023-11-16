#libraries
from tkinter import *
from tkinter import ttk 

#colors
background_color = '#1d1c29'
white = '#ffffff'
purple = '#00ff33'
red = '#ff0400'
cian = '#00fbff'
purplegray = '#37364d'

#window
window = Tk()
window.title('Calculator')
window.geometry('370x415')
window.config(bg=background_color)

#Frames
screen_frame = Frame(window, width=360, height=50, bg=purplegray)
screen_frame.grid(row=0, column=0)

keyboard_frame = Frame(window, width=360, height=395, bg=background_color)
keyboard_frame.grid(row=1, column=0)

#variables
all_values = ''
text_value = StringVar()

#functions
def math(value):
    
    global all_values

    all_values += str(value)
    
    #value on screen
    text_value.set(all_values)


def calculate():
    global all_values
    result = eval(all_values)
    all_values = str(result)
    text_value.set(result)


def clean_screen():

    global all_values
    all_values = ''
    text_value.set('')
    
#Label
app_label = Label(screen_frame, textvariable=text_value, width=23, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 bold'), bg=purplegray, fg=white)
app_label.place(x=0, y=0)


#Buttons
b1 = Button(keyboard_frame, command = clean_screen, text='C', width='21', height='4', bg=purplegray, fg=white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=8, y=10)
b2 = Button(keyboard_frame, command = lambda: math('%'), text='%', width='8', height='4', bg=purplegray, fg=white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=188, y=10)
b3 = Button(keyboard_frame, command = lambda: math('/'), text='÷', width='8', height='4', bg=cian, fg=purplegray, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=278, y=10)
b4 = Button(keyboard_frame, command = lambda: math('7'),  text='7', width='8', height='4', bg=purplegray, fg=white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=8, y= 80)
b5 = Button(keyboard_frame, command = lambda: math('8'), text='8', width='8', height='4', bg=purplegray, fg=white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=98, y=80)
b6 = Button(keyboard_frame, command = lambda: math('9'), text='9', width='8', height='4', bg=purplegray, fg=white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=188, y=80)
b7 = Button(keyboard_frame, command = lambda: math('*'), text='X', width='8', height='4', bg=cian, fg=purplegray, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x= 278, y=80)
b8 = Button(keyboard_frame, command = lambda: math('4'), text='4', width='8', height='4', bg=purplegray, fg=white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=8, y= 150)
b9 = Button(keyboard_frame, command = lambda: math('5'), text='5', width='8', height='4', bg=purplegray, fg=white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=98, y=150)
b10 = Button(keyboard_frame, command = lambda: math('6'), text='6', width='8', height='4', bg=purplegray, fg=white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=188, y=150)
b11 = Button(keyboard_frame, command = lambda: math('-'), text='-', width='8', height='4', bg=cian, fg=purplegray, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=278, y=150)
b12 = Button(keyboard_frame, command = lambda: math('1'), text='1', width='8', height='4', bg=purplegray, fg=white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=8, y= 220)
b13 = Button(keyboard_frame, command = lambda: math('2'), text='2', width='8', height='4', bg=purplegray, fg=white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=98, y=220)
b14 = Button(keyboard_frame, command = lambda: math('3'), text='3', width='8', height='4', bg=purplegray, fg=white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=188, y=220)
b15 = Button(keyboard_frame, command = lambda: math('+'), text='+', width='8', height='4', bg=cian, fg=purplegray, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=278, y=220)
b16 = Button(keyboard_frame, command = lambda: math('0'), text='0', width=21, height='4', bg=purplegray, fg=white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=8, y=290)
b17 = Button(keyboard_frame, command = lambda: math('.'), text='.', width='8', height='4', bg=purplegray, fg=white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=188, y=290)
b18 = Button(keyboard_frame, command = lambda: calculate(), text='=', width='8', height='4', bg=cian, fg=purplegray, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=278, y=290)

window.mainloop()

