import tkinter as Tkinter
from stopwatch_logic import Start, Stop, Reset

def setup_ui():
    root = Tkinter.Tk()
    root.title("Stopwatch")

    # Fixing the window size.
    root.minsize(width=250, height=70)
    label = Tkinter.Label(root, text='Ready!', fg='black', font='Verdana 30 bold')
    label.pack()
    f = Tkinter.Frame(root)
    start = Tkinter.Button(f, text='Start', width=6, command=lambda: Start(label))
    stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
    reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))
    f.pack(anchor='center', pady=5)
    start.pack(side='left')
    stop.pack(side='left')
    reset.pack(side='left')
    root.mainloop()

    return label, start, stop, reset
