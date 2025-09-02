import tkinter as tk
from tkinter import messagebox

class AgendarConsulta(tk.Frame):
    def __init__(self, root, voltar_callback):
        super().__init__(root, bg="#f5f7fa")
        self.root = root
        self.voltar_callback = voltar_callback
        self.consultas = []

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

        tk.Label(self, text="Agendar Consulta", font=("Arial", 20, "bold"),
                 bg="#f5f7fa", fg="#333").pack(pady=20)

        form_frame = tk.Frame(self, bg="#f5f7fa")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Médico:", font=("Arial", 12), bg="#f5f7fa").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_medico = tk.Entry(form_frame, width=30)
        self.entry_medico.grid(row=0, column=1, pady=5, padx=10)

        tk.Label(form_frame, text="Paciente:", font=("Arial", 12), bg="#f5f7fa").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_paciente = tk.Entry(form_frame, width=30)
        self.entry_paciente.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(form_frame, text="Data (dd/mm/aaaa):", font=("Arial", 12), bg="#f5f7fa").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_data = tk.Entry(form_frame, width=30)
        self.entry_data.grid(row=2, column=1, pady=5, padx=10)

        tk.Button(self, text="Salvar", command=self.salvar_consulta, **self.btn_style).pack(pady=10)
        tk.Button(self, text="Ver Consultas", command=self.ver_consultas, **self.btn_style).pack(pady=5)
        tk.Button(self, text="Voltar", command=self.voltar_callback, **self.btn_style).pack(pady=20)

    def salvar_consulta(self):
        medico = self.entry_medico.get()
        paciente = self.entry_paciente.get()
        data = self.entry_data.get()

        if not medico or not paciente or not data:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
            return

        self.consultas.append({
            "medico": medico,
            "paciente": paciente,
            "data": data
        })

        messagebox.showinfo("Consulta Agendada",
                            f"Médico: {medico}\nPaciente: {paciente}\nData: {data}")

        self.entry_medico.delete(0, tk.END)
        self.entry_paciente.delete(0, tk.END)
        self.entry_data.delete(0, tk.END)

    def ver_consultas(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Consultas Agendadas", font=("Arial", 20, "bold"),
                 bg="#f5f7fa", fg="#333").pack(pady=20)

        if not self.consultas:
            tk.Label(self, text="Nenhuma consulta agendada.", font=("Arial", 12), bg="#f5f7fa").pack(pady=10)
        else:
            for c in self.consultas:
                tk.Label(
                    self,
                    text=f"Dr(a). {c['medico']} \nPaciente: {c['paciente']} \nData: {c['data']}",
                    font=("Arial", 12), bg="#f5f7fa", justify="left"
                ).pack(pady=5)

        tk.Button(self, text="Voltar", command=self.voltar_callback, **self.btn_style).pack(pady=20)