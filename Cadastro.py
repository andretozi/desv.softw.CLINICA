import tkinter as tk
from tkinter import messagebox

class Cadastro(tk.Frame):
    def __init__(self, root, voltar_callback):
        super().__init__(root, bg="#f5f7fa")
        self.root = root
        self.voltar_callback = voltar_callback
        self.usuarios = []

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


        tk.Label(self, text="Cadastro de Usuário", font=("Arial", 20, "bold"),
                 bg="#f5f7fa", fg="#333").pack(pady=20)


        form_frame = tk.Frame(self, bg="#f5f7fa")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Nome: ", font=("Arial", 12), bg="#f5f7fa").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_nome = tk.Entry(form_frame, width=30)
        self.entry_nome.grid(row=0, column=1, pady=5, padx=10)

        tk.Label(form_frame, text="Idade: ", font=("Arial", 12), bg="#f5f7fa").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_idade = tk.Entry(form_frame, width=30)
        self.entry_idade.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(form_frame, text="Cargo (Médico/Paciente): ", font=("Arial", 12), bg="#f5f7fa").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_cargo = tk.Entry(form_frame, width=30)
        self.entry_cargo.grid(row=2, column=1, pady=5, padx=10)

        tk.Label(form_frame, text="CPF: ", font=("Arial", 12), bg="#f5f7fa").grid(row=3, column=0, sticky="w", pady=5)
        self.entry_cpf = tk.Entry(form_frame, width=30)
        self.entry_cpf.grid(row=3, column=1, pady=5, padx=10)

        tk.Button(self, text="Salvar", command=self.salvar_usuario, **self.btn_style).pack(pady=15)
        tk.Button(self, text="Voltar", command=self.voltar_callback, **self.btn_style).pack(pady=10)

    def salvar_usuario(self):
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        cargo = self.entry_cargo.get()
        cpf = self.entry_cpf.get()

        if not nome or not idade or not cargo or not cpf:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
            return

        self.usuarios.append({
            "nome": nome,
            "idade": idade,
            "cargo": cargo,
            "cpf": cpf
        })

        messagebox.showinfo("Cadastro", f"Usuário {nome} cadastrado com sucesso!")

        self.entry_nome.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)
        self.entry_cargo.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
