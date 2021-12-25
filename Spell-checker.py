from textblob import TextBlob  #used for spelling correction
from tkinter import *       #used for Graphical User Interface


#function to check and correct the wrong spelling
def check():
    b = TextBlob(e.get())
    corrected_text = Label(root, text=str(b.correct()))
    corrected_text.pack()


#main function
if __name__ == "__main__" :

    # makeing a window
    root=Tk()

    # giving title to the window
    root.title("Shivani's SpellChecker")

    # specifying it's size
    root.geometry("400x200")

    # giving background-color
    root.configure(bg='light pink')
    
    #heading of our window
    head = Label(root, text="Enter your text", font=('helvetica',10,'bold'))
    head.pack()
    
    #input text
    e = Entry(root, width=200, bg='light blue')
    e.pack()
    
    #button used to call the check function
    b = Button(root, text='Check', font=('helvetica',8,'bold'), fg='black', bg='red' ,command=check)
    b.pack()
    
    #closing the mainloop
    root.mainloop()
