from tkinter import *
from tkinter import messagebox

# the main app window :
root = Tk()

# Change the title :
root.title('Calculate age app')

# Dimension :
root.geometry('500x250')

# Age label :
label = Label(root,text=('write your age'),font=('fantastic',20),height=2,bg='gray')
label.pack()

# Age variables :
age = StringVar()

# Default value :
age.set('00')

# Input for age:
age_input = Entry(root,width=2,font=('Fantastic',30),textvariable=age)
age_input.pack()

# the function :
def calculator():
    age_value = age.get()
    
    months = int(age_value) * 12
    weeks = int(months) * 4
    days = int(age_value) * 365
    hours = int(days) * 24 

    months_line = f"Your age in months is : {months}"
    weeks_line = f"Your age in weeks is : {weeks}"
    days_line = f"Your age in days is : {days}"
    hours_line = f"Your age in hours : {hours} "

    all_lines = [months_line,weeks_line,days_line,hours_line]

    messagebox.showinfo("Your age ","\n".join(all_lines))

# Button :
button = Button(root,text="Calculate age",width=20,height=2,bg="blue",fg="white",borderwidth=0,command=calculator)
button.pack()
# Run infinitely :
root.mainloop()