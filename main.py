import tkinter as tk
from Cadastro import Cadastro
from AgendarConsulta import AgendarConsulta

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema da Clínica")
    root.geometry("600x500")
    root.configure(bg="#f5f7fa")

    def show_menu():
        menu_frame.tkraise()

    def show_cadastro():
        cadastro_frame.tkraise()

    def show_agendamento():
        agendamento_frame.tkraise()

    menu_frame = tk.Frame(root, bg="#f5f7fa")
    cadastro_frame = Cadastro(root, show_menu)
    agendamento_frame = AgendarConsulta(root, show_menu)

    btn_style = {
        "bg": "#4CAF50",
        "fg": "white",
        "activebackground": "#45a049",
        "font": ("Arial", 14, "bold"),
        "width": 25,
        "bd": 0,
        "relief": "raised"
    }

    tk.Label(menu_frame, text="Clínica Médica", font=("Arial", 24, "bold"),
             bg="#f5f7fa", fg="#333").pack(pady=40)

    tk.Button(menu_frame, text="Cadastro Usuário", command=show_cadastro, **btn_style).pack(pady=15)
    tk.Button(menu_frame, text="Agendar Consulta", command=show_agendamento, **btn_style).pack(pady=15)
    tk.Button(menu_frame, text="Ver Consultas", command=agendamento_frame.ver_consultas, **btn_style).pack(pady=15)

    for frame in (menu_frame, cadastro_frame, agendamento_frame):
        frame.place(x=0, y=0, relwidth=1, relheight=1)

    menu_frame.tkraise()

    root.mainloop()