from tkinter import Tk, ttk, constants, StringVar
from services.practise_service import (
    practise_service as default_practise_service
)
from services.user_service import (
    user_service as default_user_service
)


class PractiseView:
    def __init__(self, root, handle_main, handle_button_click,
                 practise_service=default_practise_service,
                 user_service=default_user_service
                 ):
        self.__root = root
        self.__frame = None
        self.__handle_main = handle_main
        self.__handle_button_click = handle_button_click
        self.__user_service = user_service
        self.__practise_service = practise_service
        self.__words = None
        self.__button_word_index_orig = None
        self.__button_word_index_transl = None
        self.__user = self.__user_service.get_current_user()

        self.__response = None
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

    def __logout_handler(self):
        self.__practise_service.save_points()
        self.__user_service.logout()
        self.__user = None
        self.__handle_main()

    def __practice_handler(self):
        self.__practise_service.save_points()
        self.__handle_main()

    def _show_response(self, message):
        self._response_variable.set(message)
        self._response_label.grid()

    def _hide_response(self):
        self._response_label.grid_remove()

    def __initialize(self):
        self.__frame = ttk.Frame(master=self.__root)
        self.__frame['padding'] = (5, 5, 5, 10)
        label = ttk.Label(
            master=self.__frame,
            text="Tervetuloa sanastotreeniin!"
        )
        if self.__user:

            label_username = ttk.Label(
            master=self.__frame,
            text=f"Kirjautuneena {self.__user.name}"
                )

            button_logout = ttk.Button(
                master=self.__frame,
                text="Kirjaudu ulos",
                command=self.__logout_handler
                )

        self.__words = self.__practise_service.get_words_to_practise()
        self.__button_word_index_orig = self.__practise_service.get_word_orig_indexes()
        self.__button_word_index_transl = self.__practise_service.get_word_transl_indexes()

        self.__response = self.__practise_service.get_response()
        self._response_variable = StringVar()
        self._response_variable.set("testi")

        self._response_label = ttk.Label(
            master=self.__frame,
            textvariable=self._response_variable,
            foreground='green'
        )

        word_button1 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_orig[0]].word_orig,
            command=lambda: self.__handle_button_click(1)
        )

        word_button2 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_orig[1]].word_orig,
            command=lambda: self.__handle_button_click(2)
        )

        word_button3 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_orig[2]].word_orig,
            command=lambda: self.__handle_button_click(3)
        )

        word_button4 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_orig[3]].word_orig,
            command=lambda: self.__handle_button_click(4)
        )

        word_button5 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_orig[4]].word_orig,
            command=lambda: self.__handle_button_click(5)
        )

        word_button6 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_transl[0]].word_transl,
            command=lambda: self.__handle_button_click(6)
        )

        word_button7 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_transl[1]].word_transl,
            command=lambda: self.__handle_button_click(7)
        )

        word_button8 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_transl[2]].word_transl,
            command=lambda: self.__handle_button_click(8)
        )

        word_button9 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_transl[3]].word_transl,
            command=lambda: self.__handle_button_click(9)
        )

        word_button10 = ttk.Button(
            master=self.__frame,
            text=self.__words[self.__button_word_index_transl[4]].word_transl,
            command=lambda: self.__handle_button_click(10)
        )

        button = ttk.Button(
            master=self.__frame,
            text="takaisin päävalikkoon",
            command=self.__practice_handler
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)
        if self.__user:
            label_username.grid(row=0, column=2)
            button_logout.grid(row=1, column=2)

        word_button1.grid(row=2, column=0)
        word_button2.grid(row=3, column=0)
        word_button3.grid(row=4, column=0)
        word_button4.grid(row=5, column=0)
        word_button5.grid(row=6, column=0)

        word_button6.grid(row=2, column=2, sticky='w')
        word_button7.grid(row=3, column=2, sticky='w')
        word_button8.grid(row=4, column=2, sticky='w')
        word_button9.grid(row=5, column=2, sticky='w')
        word_button10.grid(row=6, column=2, sticky='w')

        self._response_label.grid(row=7, column=0)

        self._hide_response()
