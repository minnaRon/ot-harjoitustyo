from tkinter import Tk, ttk, constants, StringVar
from services.practise_service import (
        practise_service as default_practise_service
)

class PractiseView:
    def __init__(self, root, handle_main, handle_button_click, practise_service = default_practise_service):
        self.__root = root
        self.__handle_main = handle_main
        self.__frame = None
        self.__words = practise_service.get_words_to_practise()
        self.__button_word_index_orig = practise_service.get_word_orig_indexes()
        self.__button_word_index_transl = practise_service.get_word_transl_indexes()
        self.__handle_button_click = handle_button_click
        self.__response = practise_service.get_response()
        self._response_variable = None
        self._response_label = None

        self.__initialize()

        self.__words = practise_service.get_words_to_practise()
        self.__button_word_index_orig = practise_service.get_word_orig_indexes()
        self.__button_word_index_transl = practise_service.get_word_transl_indexes()

        if self.__response:
            self._show_response(self.__response)

    def pack(self):
        self.__frame.pack(fill=constants.X)

    def destroy(self):
        self.__frame.destroy()

    def _show_response(self, message):
        self._response_variable.set(message)
        self._response_label.grid()

    def _hide_response(self):
        self._response_label.grid_remove()

    def __initialize(self):
        self.__frame = ttk.Frame(master=self.__root)

        label = ttk.Label(
                master=self.__frame, 
                text="Tervetuloa sanastotreeniin!"
                )

        self._response_variable = StringVar()
        self._response_variable.set("testi")
        
        self._response_label = ttk.Label(
            master=self.__frame,
            textvariable=self._response_variable,
            foreground='green'
        )

        word_button1 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_orig[0]][0],
            command=lambda: self.__handle_button_click(1)
        )

        word_button2 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_orig[1]][0],
            command=lambda: self.__handle_button_click(2)
        )

        word_button3 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_orig[2]][0],
            command=lambda: self.__handle_button_click(3)
        )

        word_button4 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_orig[3]][0],
            command=lambda: self.__handle_button_click(4)
        )

        word_button5 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_orig[4]][0],
            command=lambda: self.__handle_button_click(5)
        )

        word_button6 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_transl[0]][1],
            command=lambda: self.__handle_button_click(6)
        )

        word_button7 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_transl[1]][1],
            command=lambda: self.__handle_button_click(7)
        )

        word_button8 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_transl[2]][1],
            command=lambda: self.__handle_button_click(8)
        )

        word_button9 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_transl[3]][1],
            command=lambda: self.__handle_button_click(9)
        )

        word_button10 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_transl[4]][1],
            command=lambda: self.__handle_button_click(10)
        )

        button = ttk.Button(
            master=self.__frame,
            text="takaisin päävalikkoon",
            command=self.__handle_main
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)

        word_button1.grid(row=2, column=0)
        word_button2.grid(row=3, column=0)
        word_button3.grid(row=4, column=0)
        word_button4.grid(row=5, column=0)
        word_button5.grid(row=6, column=0)

        word_button6.grid(row=2, column=1)
        word_button7.grid(row=3, column=1)
        word_button8.grid(row=4, column=1)
        word_button9.grid(row=5, column=1)
        word_button10.grid(row=6, column=1)

        self._response_label.grid(row=7, column=0)   

        self._hide_response()
