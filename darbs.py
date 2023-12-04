import tkinter as tk
from tkinter import ttk
import sqlite3

def izveidot_sludinājumu():

    marka = marka_entry.get()
    modelis = modelis_entry.get()
    tehniska_apskate = tehniska_apskate_entry.get()
    sludinājums = sludinājums_entry.get()

    conn = sqlite3.connect('automasinas.db')
    c = conn.cursor()


    c.execute("INSERT INTO automasinas (Marka, Modelis, Tehniska_apskate, Sludinājums) VALUES (?, ?, ?, ?)",
              (marka, modelis, tehniska_apskate, sludinājums))
    conn.commit()


    marka_entry.delete(0, tk.END)
    modelis_entry.delete(0, tk.END)
    tehniska_apskate_entry.delete(0, tk.END)
    sludinājums_entry.delete(0, tk.END)


    conn.close()


window = tk.Tk()
window.title('Automašīnu sludinājumu pārvaldība')

frame = ttk.Frame(window, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

marka_label = ttk.Label(frame, text="Marka:")
marka_label.grid(row=0, column=0, sticky=tk.W)
marka_entry = ttk.Entry(frame, width=20)
marka_entry.grid(row=0, column=1)

modelis_label = ttk.Label(frame, text="Modelis:")
modelis_label.grid(row=1, column=0, sticky=tk.W)
modelis_entry = ttk.Entry(frame, width=20)
modelis_entry.grid(row=1, column=1)

tehniska_apskate_label = ttk.Label(frame, text="Tehniska apskate:")
tehniska_apskate_label.grid(row=2, column=0, sticky=tk.W)
tehniska_apskate_entry = ttk.Entry(frame, width=20)
tehniska_apskate_entry.grid(row=2, column=1)

sludinājums_label = ttk.Label(frame, text="Sludinājums:")
sludinājums_label.grid(row=3, column=0, sticky=tk.W)
sludinājums_entry = ttk.Entry(frame, width=20)
sludinājums_entry.grid(row=3, column=1)

submit_button = ttk.Button(frame, text="Izveidot sludinājumu", command=izveidot_sludinājumu)
submit_button.grid(row=4, column=0, columnspan=2)

window.mainloop()