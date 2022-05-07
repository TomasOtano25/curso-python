import tkinter as tk


def main():
    root = tk.Tk()
    root.title('Catalogo de Peliculas')
    # root.iconbitmap('img/cp-logo.ico')
    root.resizable(0, 0)

    frame = tk.Frame(root)
    frame.pack()
    frame.config()

    root.mainloop()


if __name__ == '__main__':
    main()
