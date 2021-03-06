from tkinter import ttk, constants, StringVar
from tkinter.messagebox import askyesno
from services.practise_service import (
    practise_service as default_practise_service
)
from services.user_service import (
    user_service as default_user_service
)
from services.practise_login_service import (
    practise_login_service as default_practise_login_service
)

class PractiseView:
    def __init__(self, root, handle_main,
                 practise_service=default_practise_service,
                 user_service=default_user_service,
                 practise_login_service=default_practise_login_service
                 ):
        self.__root = root
        self.__frame = ttk.Frame(master=self.__root, padding=30)
        
        self.__handle_main = handle_main
        
        self.__user_service = user_service
        self.__user = self.__user_service.get_current_user()
        self.already_learned = None
        self.learning_progress_variable = StringVar()
        self.__practise_service = practise_service
        self.__practise_login_service = practise_login_service
        
        self.__response = None
        self.__response_variable = StringVar()
        self.__response_label = None

        self.__words = []
        self.__button_word_index_orig = []
        self.__button_word_index_transl = []
        self.__word_buttons = []
        self.__button_vars = {i:StringVar() for i in range(1,11)}
        self.__button_commands = {1:lambda: self.__handle_word_button_click(1),
                                2:lambda: self.__handle_word_button_click(2),
                                3:lambda: self.__handle_word_button_click(3),
                                4:lambda: self.__handle_word_button_click(4),
                                5:lambda: self.__handle_word_button_click(5),
                                6:lambda: self.__handle_word_button_click(6),
                                7:lambda: self.__handle_word_button_click(7),
                                8:lambda: self.__handle_word_button_click(8),
                                9:lambda: self.__handle_word_button_click(9),
                                10:lambda: self.__handle_word_button_click(10)
                                }
    
        self.__initialize()


    def pack(self):
        self.__frame.pack(fill=constants.X)


    def destroy(self):
        self.__frame.destroy()


    def __logout_handler(self):
        self.__practise_login_service.save_points(self.__words)
        self.__practise_service._response = None
        self.already_learned = None
        self.__user_service.logout()
        self.__user = None
        self.__handle_main()


    def __practice_handler(self):
        self.__practise_login_service.save_points(self.__words)
        self.__practise_service._response = None
        self.already_learned = None
        self.__handle_main()
    

    def __handle_word_button_click(self, button_number):
        self.__practise_service.check_word_pair(button_number - 1)
        self._set_word_buttons()
        self._set_response()
        self._set_learning_progress()


    def __delete_this_session_progress_handler(self):
        self.__practise_service.set_words_to_practise("English", "Finnish")
        self._set_word_buttons()
        self._set_response()
        self._set_learning_progress()


    def __delete_all_progress_handler(self):
        self.__practise_login_service.delete_all_progress()
        self.__practise_service.set_words_to_practise("English", "Finnish")
        self._set_word_buttons()
        self._set_response()
        self._set_learning_progress()


    def __initialize(self):
        self._welcome_label = ttk.Label(
            master=self.__frame,
            text="Sanastotreeni, valitse sanaparit",
            foreground='green',
            font=('default', 12, 'bold')
        )

        if self.__user:
            self._add_widgets_for_login_user()

        self._set_response()

        self._set_word_buttons()

        self._back_to_main_button = ttk.Button(
            master=self.__frame,
            text="takaisin p????valikkoon",
            command=self.__practice_handler
        )

        self._place_widgets()


    def _set_response(self):
        self._check_response()
        self._create_response_label()


    def _check_response(self):
        self.__response = self.__practise_service.get_response()
        if self.__response:
            self.__response_variable.set(self.__response)
        else:
            self.__response_variable.set("")


    def _create_response_label(self):
        self.__response_label = ttk.Label(
            master=self.__frame,
            textvariable=self.__response_variable,
            foreground='green'
        )


    def _set_word_buttons(self):
        self.__words = self.__practise_service.get_words_to_practise()
        self.__button_word_index_orig = self.__practise_service.get_word_orig_indexes()
        self.__button_word_index_transl = self.__practise_service.get_word_transl_indexes()

        self._set_words_to_buttons()
        self.__create_word_buttons()


    def _set_words_to_buttons(self):
        for i, word_pair_i in enumerate(self.__button_word_index_orig, start=1):
            self.__button_vars[i].set(self.__words[word_pair_i].word_orig)

        for i, word_pair_i in enumerate(self.__button_word_index_transl, start=6):
            self.__button_vars[i].set(self.__words[word_pair_i].word_transl)


    def __create_word_buttons(self):
        for i in range(1,11):
            self.__word_buttons.append( 
            ttk.Button(
            master=self.__frame,
            textvariable=self.__button_vars[i],
            command=self.__button_commands[i],
            style='words.TButton'
        ))


    def _place_word_buttons(self):

        for i in range(10):
            self.__word_buttons[i].grid(
                row = i+4 if i < 5 else i-1,
                column = 0 if i < 5 else 1,
                padx=10, pady=5,
                sticky = 'e' if i < 5 else 'w'
                )


    def _add_widgets_for_login_user(self):
            self._set_learning_progress()

            self._label_username = ttk.Label(
            master=self.__frame,
            text=f"Kirjautuneena {self.__user.name}"
                )

            self._label_progress = ttk.Label(
            master=self.__frame,
            textvariable=self.learning_progress_variable
                )

            self._button_logout = ttk.Button(
                master=self.__frame,
                text="Kirjaudu ulos",
                command=self.__logout_handler
                )

            self._button_delete_this_session_progress = ttk.Button(
                master=self.__frame,
                text="Nollaa t??m??n harjoittelukerran edistyminen",
                command=self.__delete_this_session_progress_handler
                )

            self._button_delete_all_progress = ttk.Button(
                master=self.__frame,
                text="Nollaa kaikki tallennettu edistyminen",
                command=self.confirm
                )

    def confirm(self):
        message_ask = 'Olet poistamassa kaikki tiedot harjoittelusi edistymisest??, '
        message_ask = message_ask +'haluatko varmasti poistaa edistymistiedot ja aloittaa alusta?'
        answer = askyesno(title='HUOM! varmistus', message=message_ask)
        if answer:
            self.__delete_all_progress_handler()

    def _set_learning_progress(self):
        self.already_learned = self.__practise_login_service.get_already_learned()
        count_already_learned = len(self.already_learned) if self.already_learned else 0
        self.learning_progress_variable.set(f"kokonaan opitut {count_already_learned}")


    def _place_widgets(self):
        self._welcome_label.grid(row=0, column=0, sticky='w', pady=30)
        self._back_to_main_button.grid(row=0, column=2, sticky='e')

        if self.__user:
            self._button_logout.grid(row=1, column=2, sticky='e')
            self._label_username.grid(row=1, column=0, sticky='w')
            self._label_progress.grid(row=2, column=0, sticky='w')
            self._button_delete_this_session_progress.grid(row=10, column=0, pady=5, columnspan=2, sticky='w')
            self._button_delete_all_progress.grid(row=11, column=0, pady=5, columnspan=2, sticky='w')

        self._place_word_buttons()

        self.__response_label.grid(row=9, column=1)

