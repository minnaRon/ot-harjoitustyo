from tkinter import Tk
from ui.ui import UI


def main():

    window = Tk()
    window.title("Sanastotreeni")
    window.resizable(0,0)

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == '__main__':
    main()
