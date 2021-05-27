#Create a Window
#Create a 8x8 Grid
#Color the Grid
#Place Sprites in the Grid
#Assign all Rules of the Game to each Pawn

from tkinter import *
window=Tk()
window.title(text="Chess Game")

elephant_white_right=Button(window, text='Elephant', height=10, width=10)
elephant_white_right.grid(row=0, column=0)

window.mainloop()
