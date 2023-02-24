from tkinter import *

#Create variable for screen
screen = Tk()
#Name on track bar
screen.title("Python From")
#Size of screen
screen.geometry('500x500')
#Set BAckground color for background screen
screen.config(bg="purple")
#Main topic on screen
Label(screen, text='Python From').place(x=150, y=65)

#Create function for run the game
def Story1(win):
    def End(tl: Toplevel, firstName, lastName, nickname, Age):
        text = f'''
        Name : {firstName} {lastName}
        Nickname : {nickname}
        Age : {Age}
        '''
        
        tl.geometry(newGeometry='500x500')
        
        Label(tl, text='Story', wraplength=tl.winfo_width()).place(x=160, y=310)
        Label(tl, text=text, wraplength=tl.win0f_width()).place(x=0, y=330)

    #Crete new screen for second page
    newScreen = Toplevel(win, bg='blue')
    newScreen.title("MAin second topic")
    #Set size of new screen
    newScreen.geometry('500x500')

    #create top title in new screen
    Label(newScreen, text='Personal').place(x=150, y=0)
    #Crete a field for filling out information
    Label(newScreen, text='Firstname : ').place(x=0, y=50)
    Label(newScreen, text='Lastname : ').place(x=0, y=100)
    Label(newScreen, text='Nickname : ').place(x=0, y=150)
    Label(newScreen, text='Age : ').place(x=0, y=200)
    
    #Create a textbox for filling out information
    FirstName = Entry(newScreen, width=17)
    FirstName.place(x=250, y=50)
    
    LastName = Entry(newScreen, width=17)
    LastName.place(x=250, y=100)
    
    Nickname = Entry(newScreen, width=17)
    Nickname.place(x=250, y=150)
    
    age = Entry(newScreen, width=17)
    age.place(x=250, y=200)
    
    submitButton = Button(newScreen, text="Submit", background="Gray", font=('Times', 12), command=lambda:End(newScreen, FirstName.get(), LastName.get(), Nickname.get(), age.get()))
    submitButton.place(x=150, y=230)
    
    newScreen.mainloop()
    
def Story2(win):
    pass

#Creating buttons
Story1Button = Button(screen, text='> Basic Information! <', command=lambda: Story1(screen), bg='orange')
#Set size of buttons
Story1Button.place(x=150, y=110)

#Creating buttons
Story2Button = Button(screen, text='> Address! <', command=lambda: Story2(screen), bg='orange')
#Set size of buttons
Story2Button.place(x=150, y=150)

#make loop for open screen always
screen.update()
screen.mainloop()