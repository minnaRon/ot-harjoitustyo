from tkinter import Tk, ttk, constants

class MainView:
    def __init__(self, root, handle_practise):

        self.__root = root
        self.__handle_practise = handle_practise
        self.__frame = None

        self.__initialize()

    def pack(self):
        self.__frame.pack(fill=constants.X)

    def destroy(self):
        self.__frame.destroy()

    def __initialize(self):

        self.__frame = ttk.Frame(master=self.__root)

        label = ttk.Label(
                master=self.__frame, 
                text="Tervetuloa sanastotreeniin!"
                )

        button = ttk.Button(
                master=self.__frame, 
                text="HARJOITTELE", 
                command=self.__handle_practise)

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)
