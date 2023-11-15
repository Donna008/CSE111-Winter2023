import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry, FloatEntry
import math
def main():
    root = tk.Tk()
    # frame = window
    frm_main = Frame(root)
    frm_main.master.title('gui')
    frm_main.pack(padx =4, pady =3,fill = tk.BOTH, expand = 1)
    # call the populate function
    populate_main_window(frm_main)
    # start the tkinter loop
    root.mainloop()

    # creat a graph
def populate_main_window(frm_main):
    lbl_width = Label(frm_main, text = 'Width (80 - 300):')
    lbl_ratio = Label(frm_main, text = 'Aspect Ratio (30 - 90):')
    lbl_diam = Label(frm_main, text = 'Diameter (7 - 30):')
    lbl_volume = Label(frm_main, text = 'Volume:')
    # create three number entries
    ent_width = IntEntry(frm_main, width = 5, lower_bound=80, upper_bound=300)
    ent_ratio = IntEntry(frm_main, width =5, lower_bound=30, upper_bound=90)
    ent_diam = FloatEntry(frm_main, width=5, lower_bound=7, upper_bound=30)
    # create a label to display the result
    txt_volume = Label(frm_main,width=5, anchor='e')
    # create labels to display the units
    lbl_width_units = Label(frm_main, text = 'millimeters')
    # ratios don't habe units
    lbl_diam_units=Label(frm_main, text='inches')
    lbl_vol_units=Label(frm_main, text='liters')
    # create the clear button
    btn_clear= Button(frm_main, text='Clear')
    # layout all thelabels. number entries, and buttons in agrid
    lbl_width.grid(row=0,column=0, padx=3,pady=2, sticky='e')
    ent_width.grid(row=0, column=1, padx=3, pady=2, sticky='w')
    lbl_width_units.grid(row=0, column=2, padx=0, pady=2, sticky='w')
    
    lbl_ratio.grid(row=1, column=0, padx=3, pady=2,sticky='e')
    ent_ratio.grid(row=1, column=1, padx=3, pady=2, sticky='w')
    # ratios don't have units

    lbl_diam.grid(row=2, column=0, padx=3, pady=2, sticky='e')
    ent_diam.grid(row=2,column=1, padx=3, pady=2, sticky='w')
    lbl_diam_units.grid(row=2, column=2, padx=0, pady=2, sticky='w')
    
    lbl_volume.grid(row=3, column=0, padx=3, pady=2, sticky ='e')
    txt_volume.grid(row=3, column=1, padx=3,pady=2, sticky='w')
    lbl_vol_units.grid(row=3, column=2,padx=0, pady=2, sticky='w' )
    btn_clear.grid(row=3, column=3, padx=3, pady=2)

    #  function call each time
    def calculate(event):
        try:
            # get the user input
            w = ent_width.get()
            a = ent_ratio.get()
            d = ent_diam.get()

            # compute the tire volume in liters
            v = (math.pi * w * w * a * (w * a + 2540 * d))/ 10000000000

            # display the volume rounded to one digit
            # after the decimal for the user to see
            txt_volume.config(text=f'{v:.2f}')
            
        except ValueError:
            # when the user deletes all the digits in one
            # of the number entries, clear the result
            txt_volume.config(text='')

    # this function is called each time
    # the user clicks the 'clear button
    def clear():
        'clear all the inputs and outputs'
        btn_clear.focus()
        ent_width.clear()
        ent_ratio.clear()
        ent_diam.clear()
        txt_volume.config(text='')
        ent_width.focus()

    # 
    ent_width.bind('<KeyRelease>', calculate)
    ent_ratio.bind('<KeyRelease>', calculate)
    ent_diam.bind('<KeyRelease>', calculate)



    #
    btn_clear.config(command=clear)
    #
    ent_width.focus()

if __name__ == '__main__':
    main()