
# coding: utf-8

# In[2]:


import pandas as pd
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import *

#def run_main():
    
    #global local_file
    #local = pd.read_csv(local_file, delimiter=",",decimal = b".", usecols=[0,1,2,3,4,5])
    #local = local[['x [nm]', 'y [nm]', 'frame', 'intensity [photon]']]
    #local = local.rename(columns={'frame':'t [frame]', 'intensity [photon]':'I [A.D. counts]'})
    #local = local.round(decimals=2)
    #print(local)
    #export_file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    #local.to_csv(export_file_path, header=None, index=None, sep='\t', mode='a')

def open_file():
  
    try:
        Tk().withdraw()
        local_file = askopenfilename()
        print("Current file: " + local_file)
    except FileNotFoundError:
        print("No file selected.")
        sys.exit(1)
    except:
        local_file = ""
    local = pd.read_csv(local_file, delimiter=",",decimal = b".", usecols=[0,1,2,3,4,5])
    local = local[['x [nm]', 'y [nm]', 'frame', 'intensity [photon]']]
    local = local.rename(columns={'frame':'t [frame]', 'intensity [photon]':'I [A.D. counts]'})
    convf = float(txt.get()) 
    local['I [A.D. counts]'] = local['I [A.D. counts]'].astype(float)
    local['I [A.D. counts]'] = local['I [A.D. counts]'] * convf
    #local = local.round(decimals=2)
    #print(local)
    export_file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    local.to_csv(export_file_path, header=None, index=None, sep='\t', mode='a')
    
def gui_openfile():

    open_file()


def gui_run():
    run_main()
    done_box()

def done_box():
    messagebox.showinfo('TStoMALK', 'Done!')

window = Tk()
window.title("TS to MALK")
window.geometry('265x75')

lbl = Label(window, text="Thunderstorm .csv file")
lbl.grid(column=0, row=0)

lbl1 = Label(window, text="Conversion Factor")
lbl1.grid(column=0, row=1)

lbl2 = Label(window, text="(Gain: 200, red = 13.00, green = 12.95)")
lbl2.grid(column=0, row=2)


var = IntVar()
var.set(13.00)
txt = Entry(window, width=8, textvariable=var)
txt.grid(column=1, row=1)

btn = Button(window, text="Load file", command= gui_openfile)
btn.grid(column=1, row=0)

window.mainloop()


