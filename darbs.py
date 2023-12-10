import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

def create_table():
    try:
        conn = sqlite3.connect('ads.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS sludinājumi (
                id INTEGER PRIMARY KEY,
                kategorija TEXT,
                marka TEXT,
                modelis TEXT,
                izlaiduma_gads TEXT,
                motors TEXT,
                motora_tilpums TEXT,
                ātrumskārba TEXT,
                nobraukums TEXT,
                krāsa TEXT,
                virsbūves_tips TEXT,
                tehniskā_apskate TEXT,
                cena TEXT,
                apraksts TEXT,
                datums TEXT
            )
        ''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

create_table()

create_button = None
new_window = None


def create_ad():
    open_create_ad_window()


def open_create_ad_window():
    global new_window


    new_window = tk.Toplevel(root)
    new_window.title("Izveidot sludinājumu")

    kategorija_var = tk.StringVar(new_window, "Automašīna")
    kategorija_options = ["Automašīna"]
    kategorija_dropdown = tk.OptionMenu(new_window,kategorija_var, *kategorija_options)
    kategorija_dropdown.pack()

    marka_label = tk.Label(new_window, text="Marka:")
    marka_label.pack()

    marka_entry = tk.Entry(new_window)
    marka_entry.pack()

    modelis_label = tk.Label(new_window, text="Modelis:")
    modelis_label.pack()

    modelis_entry = tk.Entry(new_window)
    modelis_entry.pack()

    izlaiduma_gads_label = tk.Label(new_window, text="Izlaiduma gads:")
    izlaiduma_gads_label.pack()

    izlaiduma_gads_entry = tk.Entry(new_window)
    izlaiduma_gads_entry.pack()

    motors_label = tk.Label(new_window, text="Motors:")
    motors_label.pack()
    motors_var = tk.StringVar(new_window, "None")
    motors_options = ["hybrid", "dīzelis", "benzīns", "elektromašīna"]
    motors_dropdown = tk.OptionMenu(new_window,motors_var, *motors_options)
    motors_dropdown.pack()

    motora_tilpums_label = tk.Label(new_window, text="Motora tilpums:")
    motora_tilpums_label.pack()

    motora_tilpums_entry = tk.Entry(new_window)
    motora_tilpums_entry.pack()

    atrumskarba_label = tk.Label(new_window, text="Ātrumskārba:")
    atrumskarba_label.pack()

    atrumkarba_var = tk.StringVar(new_window, "None")
    atrumkarba_options = ["automāts", "maunuālais"]
    atrumkarba_dropdown = tk.OptionMenu(new_window,atrumkarba_var, *atrumkarba_options)
    atrumkarba_dropdown.pack()

    nobraukums_label = tk.Label(new_window, text="Nobraukums km:")
    nobraukums_label.pack()

    nobraukums_entry = tk.Entry(new_window)
    nobraukums_entry.pack()

    krasa_label = tk.Label(new_window, text="Krāsa:")
    krasa_label.pack()

    krasa_entry = tk.Entry(new_window)
    krasa_entry.pack()

    virsbuves_tips_label = tk.Label(new_window, text="Virsbūves tips:")
    virsbuves_tips_label.pack()
    virsbuves_tips_var = tk.StringVar(new_window, "None")
    virsbuves_tips_options = ["Kupeja", "Universāls", "Sedans", "Pikaps"]
    virsbuves_tips_dropdown = tk.OptionMenu(new_window,virsbuves_tips_var, *virsbuves_tips_options)
    virsbuves_tips_dropdown.pack()

    tehniska_apskate_label = tk.Label(new_window, text="Tehniskā apskate:")
    tehniska_apskate_label.pack()

    tehniska_apskate_entry = tk.Entry(new_window)
    tehniska_apskate_entry.pack()

    cena_label = tk.Label(new_window, text="Cena EUR:")
    cena_label.pack()

    cena_entry = tk.Entry(new_window)
    cena_entry.pack()

    apraksts_label = tk.Label(new_window, text="Apraksts:")
    apraksts_label.pack()

    apraksts_entry = tk.Text(new_window, height=5, width=30)
    apraksts_entry.pack()

    save_button = tk.Button(new_window, text="Saglabāt", command=lambda: save_ad(
        kategorija_var.get(), marka_entry.get(), modelis_entry.get(), izlaiduma_gads_entry.get(),
        motors_var.get(), motora_tilpums_entry.get(), atrumkarba_var.get(),
        nobraukums_entry.get(), krasa_entry.get(), virsbuves_tips_var.get(),
        tehniska_apskate_entry.get(), cena_entry.get(), apraksts_entry.get("1.0", tk.END)
    ))
    save_button.pack()
def save_ad(kategorija, marka, modelis, izlaiduma_gads, motors, motora_tilpums, atrumkarba,
            nobraukums, krasa, virsbuves_tips, tehniska_apskate, cena, apraksts):
    if not all([kategorija, marka, modelis, izlaiduma_gads, motors, motora_tilpums,
                atrumkarba, nobraukums, krasa, virsbuves_tips, tehniska_apskate, cena]):
        messagebox.showerror("Kļūda", "Visi lauki ir jāaizpilda!")
        return

    if not all([c.isalpha() or c.isspace() for c in marka]):
        messagebox.showerror("Kļūda", "Marka var saturēt tikai burtus!")
        return

    if not re.match(r'^\d{4}$', izlaiduma_gads):
        messagebox.showerror("Kļūda", "Izlaiduma gadam jābūt četrus ciparus saturīgam!")
        return

    if motors == "None" or atrumkarba == "None" or virsbuves_tips == "None":
        messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus izvēles laukus!")
        return

    if not re.match(r'^\d{2}-\d{4}$', tehniska_apskate):
        messagebox.showerror("Kļūda", "Tehniskā apskate jābūt formātā MM-GGGG!")
        return

    if not cena.isdigit():
        messagebox.showerror("Kļūda", "Cenai jāsatur tikai cipari!")
        return

    if not re.match(r'^\d+\.\d+$', motora_tilpums):
        messagebox.showerror("Kļūda", "Motora tilpumam jābūt formātā X.X!")
        return

    if not nobraukums.isdigit():
        messagebox.showerror("Kļūda", "Nobraukumam jāsatur tikai cipari!")
        return

    if not all([c.isalpha() or c.isspace() for c in krasa]):
        messagebox.showerror("Kļūda", "Krāsa var saturēt tikai burtus!")
        return

    try:
        conn = sqlite3.connect('ads.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO sludinājumi (
                kategorija, marka, modelis, izlaiduma_gads, motors, motora_tilpums, ātrumskārba,
                nobraukums, krāsa, virsbūves_tips, tehniskā_apskate, cena, apraksts, datums
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
        ''', (kategorija, marka, modelis, izlaiduma_gads, motors, motora_tilpums, atrumkarba,
              nobraukums, krasa, virsbuves_tips, tehniska_apskate, cena, apraksts))
        conn.commit()
        conn.close()

        update_ads()
    except sqlite3.Error as e:
        messagebox.showerror("Kļūda", f"Datubāzes kļūda: {e}")


def save_edit(ad_id, kategorija, marka, modelis, izlaiduma_gads, motors, motora_tilpums, atrumkarba,
            nobraukums, krasa, virsbuves_tips, tehniska_apskate, cena, apraksts):
    if not all([kategorija, marka, modelis, izlaiduma_gads, motors, motora_tilpums,
                atrumkarba, nobraukums, krasa, virsbuves_tips, tehniska_apskate, cena]):
        messagebox.showerror("Kļūda", "Visi lauki ir jāaizpilda!")
        return
    if not all([c.isalpha() or c.isspace() for c in marka]):
        messagebox.showerror("Kļūda", "Marka var saturēt tikai burtus!")
        return



    if not re.match(r'^\d{4}$', izlaiduma_gads):
        messagebox.showerror("Kļūda", "Izlaiduma gadam jābūt četrus ciparus saturīgam!")
        return

    if motors == "None" or atrumkarba == "None" or virsbuves_tips == "None":
        messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus izvēles laukus!")
        return

    if not re.match(r'^\d{2}-\d{4}$', tehniska_apskate):
        messagebox.showerror("Kļūda", "Tehniskā apskate jābūt formātā MM-GGGG!")
        return

    if not cena.isdigit():
        messagebox.showerror("Kļūda", "Cenai jāsatur tikai cipari!")
        return

    if not re.match(r'^\d+\.\d+$', motora_tilpums):
        messagebox.showerror("Kļūda", "Motora tilpumam jābūt formātā X.X!")
        return

    if not nobraukums.isdigit():
        messagebox.showerror("Kļūda", "Nobraukumam jāsatur tikai cipari!")
        return

    if not all([c.isalpha() or c.isspace() for c in krasa]):
        messagebox.showerror("Kļūda", "Krāsa var saturēt tikai burtus!")
        return

    try:
        conn = sqlite3.connect('ads.db')
        c = conn.cursor()
        c.execute('''
            UPDATE sludinājumi SET
            kategorija=?, marka=?, modelis=?, izlaiduma_gads=?, motors=?, motora_tilpums=?, ātrumskārba=?,
            nobraukums=?, krāsa=?, virsbūves_tips=?, tehniskā_apskate=?, cena=?, apraksts=?
            WHERE id=?
        ''', (kategorija, marka, modelis, izlaiduma_gads, motors, motora_tilpums, atrumkarba,
              nobraukums, krasa, virsbuves_tips, tehniska_apskate, cena, apraksts, ad_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Info", "Sludinājums ir veiksmīgi rediģēts!")
        update_ads()
    except sqlite3.Error as e:
        messagebox.showerror("Kļūda", f"Datubāzes kļūda: {e}")


def edit_ad(ad_id):
    edit_window = tk.Toplevel(root)
    edit_window.title("Rediģēt sludinājumu")

    conn = sqlite3.connect('ads.db')
    c = conn.cursor()
    selected_ad = c.execute("SELECT * FROM sludinājumi WHERE id=?", (ad_id,)).fetchone()
    conn.close()

    kategorija_var = tk.StringVar(edit_window, selected_ad[1])
    kategorija_options = ["Automašīna"]
    kategorija_dropdown = tk.OptionMenu(edit_window, kategorija_var, *kategorija_options)
    kategorija_dropdown.pack()

    marka_label = tk.Label(edit_window, text="Marka:")
    marka_label.pack()

    marka_entry = tk.Entry(edit_window)
    marka_entry.insert(0, selected_ad[2])
    marka_entry.pack()

    modelis_label = tk.Label(edit_window, text="Modelis:")
    modelis_label.pack()

    modelis_entry = tk.Entry(edit_window)
    modelis_entry.insert(0, selected_ad[3])
    modelis_entry.pack()

    izlaiduma_gads_label = tk.Label(edit_window, text="Izlaiduma gads:")
    izlaiduma_gads_label.pack()

    izlaiduma_gads_entry = tk.Entry(edit_window)
    izlaiduma_gads_entry.insert(0, selected_ad[4])
    izlaiduma_gads_entry.pack()

    motors_label = tk.Label(edit_window, text="Motors:")
    motors_label.pack()
    motors_var = tk.StringVar(edit_window, selected_ad[5])
    motors_options = ["hybrid", "dīzelis", "benzīns", "elektromašīna"]
    motors_dropdown = tk.OptionMenu(edit_window, motors_var, *motors_options)
    motors_dropdown.pack()

    motora_tilpums_label = tk.Label(edit_window, text="Motora tilpums:")
    motora_tilpums_label.pack()

    motora_tilpums_entry = tk.Entry(edit_window)
    motora_tilpums_entry.insert(0, selected_ad[6])
    motora_tilpums_entry.pack()

    atrumkarba_label = tk.Label(edit_window, text="Ātrumkārba:")
    atrumkarba_label.pack()

    atrumkarba_var = tk.StringVar(edit_window, selected_ad[7])
    atrumkarba_options = ["automāts", "maunuālais"]
    atrumkarba_dropdown = tk.OptionMenu(edit_window, atrumkarba_var, *atrumkarba_options)
    atrumkarba_dropdown.pack()

    nobraukums_label = tk.Label(edit_window, text="Nobraukums km:")
    nobraukums_label.pack()

    nobraukums_entry = tk.Entry(edit_window)
    nobraukums_entry.insert(0, selected_ad[8])
    nobraukums_entry.pack()

    krasa_label = tk.Label(edit_window, text="Krāsa:")
    krasa_label.pack()

    krasa_entry = tk.Entry(edit_window)
    krasa_entry.insert(0, selected_ad[9])
    krasa_entry.pack()

    virsbuves_tips_label = tk.Label(edit_window, text="Virsbūves tips:")
    virsbuves_tips_label.pack()

    virsbuves_tips_var = tk.StringVar(edit_window, selected_ad[10])
    virsbuves_tips_options = ["Kupeja", "Universāls", "Sedans", "Pikaps"]
    virsbuves_tips_dropdown = tk.OptionMenu(edit_window, virsbuves_tips_var, *virsbuves_tips_options)
    virsbuves_tips_dropdown.pack()

    tehniska_apskate_label = tk.Label(edit_window, text="Tehniskā apskate:")
    tehniska_apskate_label.pack()

    tehniska_apskate_entry = tk.Entry(edit_window)
    tehniska_apskate_entry.insert(0, selected_ad[11])
    tehniska_apskate_entry.pack()

    cena_label = tk.Label(edit_window, text="Cena EUR:")
    cena_label.pack()

    cena_entry = tk.Entry(edit_window)
    cena_entry.insert(0, selected_ad[12])
    cena_entry.pack()

    apraksts_label = tk.Label(edit_window, text="Apraksts:")
    apraksts_label.pack()

    apraksts_entry = tk.Text(edit_window, height=5, width=30)
    apraksts_entry.insert(tk.END, selected_ad[13])
    apraksts_entry.pack()

    save_button = tk.Button(edit_window, text="Saglabāt izmaiņas", command=lambda: save_edit(
        ad_id, kategorija_var.get(), marka_entry.get(), modelis_entry.get(), izlaiduma_gads_entry.get(),
        motors_var.get(), motora_tilpums_entry.get(), atrumkarba_var.get(),
        nobraukums_entry.get(), krasa_entry.get(), virsbuves_tips_var.get(),
        tehniska_apskate_entry.get(), cena_entry.get(), apraksts_entry.get("1.0", tk.END)
    ))
    save_button.pack()


def update_ads():
    global create_button

    for widget in root.winfo_children():
        if isinstance(widget, tk.Button):
            widget.destroy()

    if create_button:
        create_button = tk.Button(root, text="Izveidot sludinājumu", command=create_ad)
        create_button.pack()

    conn = sqlite3.connect('ads.db')
    c = conn.cursor()
    ads = c.execute("SELECT * FROM sludinājumi").fetchall()
    conn.close()

    for ad in ads:
        ad_button = tk.Button(root, text=f"{ad[1]} {ad[2]}", command=lambda ad=ad: show_ad(ad))
        ad_button.pack()


def delete_ad(ad_id):
    try:
        conn = sqlite3.connect('ads.db')
        c = conn.cursor()
        c.execute("DELETE FROM sludinājumi WHERE id=?", (ad_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Izdzēsts", "Sludinājums ir izdzēsts veiksmīgi!")
        update_ads()
    except sqlite3.Error as e:
        messagebox.showerror("Kļūda", f"Datubāzes kļūda: {e}")


def show_ad(ad):
    ad_window = tk.Toplevel(root)
    ad_window.title("Sludinājuma informācija")

    info_text = f"Kategorija: {ad[1]}\nMarka: {ad[2]}\nModelis: {ad[3]}\nIzlaiduma gads: {ad[4]}\nMotors: {ad[5]}\nMotora tilpums: {ad[6]}\nĀtrumkārba: {ad[7]}\nNobraukums: {ad[8]}\nKrāsa: {ad[9]}\nVirsbūves tips: {ad[10]}\nTehniskā apskate: {ad[11]}\nCena: {ad[12]}\n"

    if len(ad) > 13 and ad[13]:
        info_text += f"Apraksts: {ad[13]}\n"

    info_text += f"Datums: {ad[14]}"

    delete_button = tk.Button(ad_window, text="Dzēst sludinājumu", command=lambda: delete_ad(ad[0]))
    delete_button.pack()

    edit_button = tk.Button(ad_window, text="Rediģēt sludinājumu", command=lambda ad_id=ad[0]: edit_ad(ad_id))
    edit_button.pack()

    info_label = tk.Label(ad_window, text=info_text)
    info_label.pack()



root = tk.Tk()
root.title("Sludinājumi")

create_button = tk.Button(root, text="Izveidot sludinājumu", command=create_ad)
create_button.pack()

update_ads()
create_table()

root.mainloop()