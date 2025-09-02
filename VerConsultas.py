import tkinter as tk
from tkinter import ttk

class VerConsultas(tk.Frame):
    def __init__(self, root, voltar_callback):
        super().__init__(root, bg="#f5f7fa")
        self.voltar_callback = voltar_callback

        self.btn_style = {
            "bg": "#4CAF50",
            "fg": "white",
            "activebackground": "#45a049",
            "font": ("Arial", 12, "bold"),
            "width": 20,
            "bd": 0,
            "relief": "raised",
            "pady": 5
        }

        tk.Label(self, text="Consultas Agendadas", font=("Arial", 20, "bold"),bg="#f5f7fa", fg="#333").pack(pady=20)

        self.tree = ttk.Treeview(self, columns=("Médico", "Paciente", "Data"), show="headings")
        self.tree.heading("Médico", text="Médico")
        self.tree.heading("Paciente", text="Paciente")
        self.tree.heading("Data", text="Data")
        self.tree.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        tk.Button(self, text="Voltar", command=self.voltar, **self.btn_style).pack(pady=20)

    def carregar_consultas(self, consultas):

        for item in self.tree.get_children():
            self.tree.delete(item)

        for c in consultas:
            self.tree.insert("", tk.END, values=(c["medico"], c["paciente"], c["data"]))

    def ver_consultas(self, consultas):

        self.tkraise()
        self.carregar_consultas(consultas)

    def voltar(self):

        for item in self.tree.get_children():
            self.tree.delete(item)
        self.voltar_callback()
