#imports
from tkinter import *

#making gui 
#intro
# window = tk.Tk()




# opening = tk.Label(text="Welcome! \
#                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~\
#                     Launching Program",
#                     bg = "#294e55",
#                     fg = "#b5d4da",
#                     height= 30,
#                     width = 120) 
# btn_hist = tk.Button(text="Previous Usage",
#                         )
# opening.pack()
# window.mainloop()

root =  Tk()
root.title("Use Tracker")

opening = Label(text="Welcome! \
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~\
                    Usage Tracker",
                    bg = "#294e55",
                    fg = "#b5d4da",
                    height= 15,
                    width = 85)
opening.grid(row=0,column=0,columnspan=3) 

#history page button w/ charts
def histBtn():

    return

btn_hist = Button(root, text="Useage History",
                  padx=40,
                  pady=20,
                  command=histBtn,
                  ) 
btn_hist.grid(row=2, column=1)


#log of activities page
def logBtn():

    return

btn_log = Button(root, text="Useage Log",
                 padx=40,
                 pady=20,
                 command=logBtn
                 )
btn_hist.grid(row=4, column=1)

root.mainloop()


