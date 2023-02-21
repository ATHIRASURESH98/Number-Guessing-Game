from tkinter import *
window=Tk()#TO CREATE THE BASIC WINDOW
window.geometry("800x900")

window.title("NUMBER GUESSING GAME")

#TO CREATE THE FIRST LABEL "!!!GUESS YOUR NUMBER!!!"
l1=Label(window,text="!!!GUESS YOUR NUMBER!!!",fg="green",bg="#FFFF63",font=("bold",30))
l1.grid(column=1,row=0)
#Labe2 for Enter the name
l2=Label(window,text="Enter your name:",fg="#0000FF",bg="#FFFF63",font=("bold",20))
l2.grid(column=0,row=1)
#ENTRY BUTTOM TO ENTER THE NAME
e1=Entry(window,font=("normal",20),width=20,bd=5)
e1.grid(column=1,row=1)
#For enter button
B1=Button(window,text="Enter")
B1.grid(column=2,row=1)
#Label3 for select the mode
l3=Label(window,text="Select the mode:",fg="#0000FF",bg="#FFFF63",font=("bold",20))
l3.grid(column=0,row=2)
#Radio buttons to select the mode
R1=Radiobutton(window,text="Easy")
R1.grid(column=0,row=3)
R2=Radiobutton(window,text="Medium")
R2.grid(column=1,row=3)
R3=Radiobutton(window,text="Hard")
R3.grid(column=2,row=3)
#A start button to start the game
B2=Button(window,text="START THE GAME",font=("bold",10),bd=10,bg="green")
B2.grid(column=1,row=6)
#Label4 for Enter the number
l4=Label(window,text="Enter the number:",fg="#0000FF",bg="#FFFF63",font=("bold",20))
l4.grid(column=0,row=8)
#ENTRY BUTTOM TO ENTER THE NUMBER
e2=Entry(window,font=("normal",20),width=20,bd=5)
e2.grid(column=1,row=8)
#Button for guessing the number
B2=Button(window,text="GUESS",bg="green",bd=5)
B2.grid(column=3,row=8)
#Label5 for showing the result
l5=Label(window,text="#game status",fg="#0000FF",bg="#FFFF63",font=("bold",20))
l5.grid(column=1,row=9)
#A exit button to start the game
B2=Button(window,text="EXIT",font=("bold",10),bd=10,bg="red")
B2.grid(column=1,row=10)
window.config(bg="#FFFF63")#TO ADD BACKGROUND COLOR TO THE WINDOW
window.mainloop()
