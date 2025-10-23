import customtkinter as ctk
from view.tela_principal import TelaPrincipal

if __name__ == '__main__':
    app = ctk.CTk()
    app.geometry('700x700')

    TelaPrincipal(app)
    app.mainloop()