import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
from ttkbootstrap import Style

class AutoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto andmete haldamine")
        self.root.geometry("600x400")
        
        self.style = Style(theme="darkly")
        
        self.autod = [
            {"värv": "punane", "tootja": "Audi", "kiirus": 0},
            {"värv": "sinine", "tootja": "BMW", "kiirus": 50},
            {"värv": "roheline", "tootja": "Toyota", "kiirus": 80},
            {"värv": "hall", "tootja": "Ford", "kiirus": 120},
            {"värv": "must", "tootja": "Mercedes", "kiirus": 150}
        ]
        
        self.pealkirjad = ["Värv", "Tootja", "Kiirus (km/h)"]
        
        self.otsingu_tekst = tk.StringVar()
        
        self.lehekülje_suurus = 3
        self.aktiivne_leht = 1
        
        self.loo_widgets()
    
    def loo_widgets(self):
        # Raam
        self.raam = ttk.Frame(self.root)
        self.raam.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Otsingu ja lisamise väljad
        otsingu_raam = ttk.Frame(self.raam)
        otsingu_raam.pack(pady=5, fill="x")
        
        ttk.Label(otsingu_raam, text="Otsi:").pack(side="left", padx=(0, 5))
        ttk.Entry(otsingu_raam, textvariable=self.otsingu_tekst).pack(side="left", fill="x", expand=True, padx=(0, 5))
        ttk.Button(otsingu_raam, text="Otsi", command=self.otsi_andmeid).pack(side="left")
        ttk.Button(otsingu_raam, text="Lisa", command=self.lisa_andmeid).pack(side="right")
        ttk.Button(otsingu_raam, text="Uuenda", command=self.uuenda_andmeid).pack(side="right")
        
        # Andmete kuvamine
        self.andmeidekst = ScrolledText(self.raam, wrap="none", height=15)
        self.andmeidekst.pack(fill="both", expand=True)
        self.kuva_andmed()
        
        # Leheküljepaneel
        lehekülje_nuppude_rahv = ttk.Frame(self.raam)
        lehekülje_nuppude_rahv.pack(pady=5)
        
        ttk.Button(lehekülje_nuppude_rahv, text="Eelmine", command=self.eelmine_leht).pack(side="left")
        ttk.Label(lehekülje_nuppude_rahv, text=f"Leht {self.aktiivne_leht}").pack(side="left", padx=10)
        ttk.Button(lehekülje_nuppude_rahv, text="Järgmine", command=self.järgmine_leht).pack(side="left")
    
    def kuva_andmed(self):
        self.andmeidekst.delete("1.0", "end")
        algus = (self.aktiivne_leht - 1) * self.lehekülje_suurus
        lõpp = self.aktiivne_leht * self.lehekülje_suurus
        näidatavad_andmed = self.autod[algus:lõpp]
        for pealkiri in self.pealkirjad:
            self.andmeidekst.insert("end", pealkiri + "\t")
        self.andmeidekst.insert("end", "\n" + "-"*50 + "\n")
        for auto in näidatavad_andmed:
            for väärtus in auto.values():
                self.andmeidekst.insert("end", str(väärtus) + "\t")
            self.andmeidekst.insert("end", "\n")
    
    def otsi_andmeid(self):
        otsing = self.otsingu_tekst.get().lower()
        otsitud_autod = []
        for auto in self.autod:
            if otsing in str(auto).lower():
                otsitud_autod.append(auto)
        if otsitud_autod:
            self.autod = otsitud_autod
            self.aktiivne_leht = 1
            self.kuva_andmed()
        else:
            messagebox.showinfo("Otsing", "Andmeid ei leitud.")
    
    def lisa_andmeid(self):
        värv = input("Sisesta auto värv: ")
        tootja = input("Sisesta auto tootja: ")
        kiirus = int(input("Sisesta auto kiirus (km/h): "))
        self.autod.append({"värv": värv, "tootja": tootja, "kiirus": kiirus})
        self.kuva_andmed()
    
    def uuenda_andmeid(self):
        rida = int(input("Sisesta rea number, mida soovid uuendada: "))
        värv = input("Sisesta uus auto värv: ")
        tootja = input("Sisesta uus auto tootja: ")
        kiirus = int(input("Sisesta uus auto kiirus (km/h): "))
        self.autod[rida-1] = {"värv": värv, "tootja": tootja, "kiirus": kiirus}
        self.kuva_andmed()
    
    def järgmine_leht(self):
        viimane_leht = len(self.autod)
