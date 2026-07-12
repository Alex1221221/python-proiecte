import tkinter as tk
from tkinter import messagebox
import random as rd



def pornire_joc_nou():
    global numar_secret
    numar_secret = rd.randint(1, 100) #generarea numarului
    scor.set(5) #numarul sanselor,poate fi modificat
    indiciu.set("Introdu un numar intre 1 și 100")
    incercare.set(0)


def verifica_ghicitul():
    x = incercare.get()
    sanse_ramase = scor.get()

    if sanse_ramase > 0:
        if x > 100 or x < 1:
            indiciu.set("Numarul trebuie să fie între 1 și 100") #validare
            return

        sanse_ramase -= 1
        scor.set(sanse_ramase)

        if x == numar_secret:
            indiciu.set("Bravo! Ai ghicit numarul!")
            messagebox.showinfo("Victorie", f"Ai castigat! Numarul era {numar_secret}.")
            pornire_joc_nou()
        elif sanse_ramase == 0:
            indiciu.set(f"Game Over! Numarul era {numar_secret}.")
            messagebox.showerror("Game Over", f"Ai pierdut! Numarul corect era {numar_secret}.")
        elif x < numar_secret:
            indiciu.set("Prea mic! Incearca un numar mai mare.")
        elif x > numar_secret:
            indiciu.set("Prea mare! Incearca un numar mai mic.")


#initializeaza fereastra principala
win = tk.Tk()
win.geometry("500x600")
win.title("Number Guessing Game")
win.configure(bg="#f0f4f8")

#variabile librarie Tkinter
incercare = tk.IntexplVar()
scor = tk.IntVar()
indiciu = tk.StringVar()

#titlu
tk.Label(
    win, text="Ghiceste Numarul", font=("Helvetica", 24, "bold"),
    bg="#f0f4f8", fg="#102a43"
).pack(pady=30)

#caseta text incercare
tk.Entry(
    win, textvariable=incercare, width=4, font=("Helvetica", 40, "bold"),
    justify="center", relief="solid", bd=2
).pack(pady=10)

#buton verificare
tk.Button(
    win, text="CHECK", font=("Helvetica", 14, "bold"), bg="#1992d4", fg="white",
    width=12, height=1, relief="flat", command=verifica_ghicitul, cursor="hand2"
).pack(pady=15)

#caseta indicii
tk.Label(
    win, textvariable=indiciu, font=("Helvetica", 12, "italic"),
    bg="#e4e7eb", fg="#486581", width=45, height=2, wraplength=350, relief="groove"
).pack(pady=20)

#sanse ramase
cadru_scor = tk.Frame(win, bg="#f0f4f8")
cadru_scor.pack(pady=10)

tk.Label(cadru_scor, text="Sanse ramase:", font=("Helvetica", 14), bg="#f0f4f8", fg="#627d98").pack(side="left")
tk.Label(cadru_scor, textvariable=scor, font=("Helvetica", 16, "bold"), bg="#f0f4f8", fg="#d32f2f").pack(side="left",
                                                                                                         padx=5)

#buton control/iesire
cadru_butoane = tk.Frame(win, bg="#f0f4f8")
cadru_butoane.pack(side="bottom", pady=40)

tk.Button(
    cadru_butoane, text="Reset", font=("Helvetica", 10, "bold"), bg="#9fb3c8", fg="white",
    width=8, command=pornire_joc_nou, relief="flat"
).pack(side="left", padx=10)

tk.Button(
    cadru_butoane, text="Iesire", font=("Helvetica", 10, "bold"), bg="#ba1f1f", fg="white",
    width=8, command=win.quit, relief="flat"
).pack(side="left", padx=10)

#apelare functie pornire joc
pornire_joc_nou()
#bucla pentru a mentine fereastra pana la inchidere
win.mainloop()