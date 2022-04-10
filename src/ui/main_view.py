from tkinter import Tk, ttk, constants


class MainView:
    def __init__(self, root, handle_practise, handle_add_words):
        self.__root = root
        self.__handle_practise = handle_practise
        self.__handle_add_words = handle_add_words
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
        button_add_words = ttk.Button(
            master=self.__frame,
            text="Lisää sanoja",
            command=self.__handle_add_words)

        button_practise = ttk.Button(
            master=self.__frame,
            text="HARJOITTELE",
            command=self.__handle_practise)

        label.grid(row=0, column=0)
        button_add_words.grid(row=1, column=0)
        button_practise.grid(row=2, column=0)
