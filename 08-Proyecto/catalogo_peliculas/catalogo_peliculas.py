import tkinter as tk
from client.gui_app import Frame, barra_menu


def main():
    root = tk.Tk()
    root.title('Catalogo de Peliculas')
    # root.iconbitmap('img/cp-logo.ico')
    root.resizable(1, 1)

    app = Frame(root=root)

    barra_menu(root)

    app.mainloop()


if __name__ == '__main__':
    main()
