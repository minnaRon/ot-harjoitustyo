import tkinter as tk
from tkinter import Text, ttk, constants, StringVar
from services.word_service import (
    word_service as default_word_service
)

class AddWordsView:
    def __init__(self, root, handle_main,
                 word_service=default_word_service
                 ):
        self._root = root
        self.__handle_main = handle_main
        self.__frame1 = None
        self.__frame2 = None
        self.__word_service = word_service
        self.lang_orig = 'suomi'
        self.lang_transl = 'suomi'
        self.lang_options = ('suomi', 'englanti')
        self.option_var = None
        self.__message_variable = None
        self.__message_label = None

        self.__initialize()


    def pack(self):
        self.__frame1.pack(fill=constants.X)
        self.__frame2.pack(fill=constants.X)


    def destroy(self):
        self.__frame1.destroy()
        self.__frame2.destroy()


    def _show_message(self, message):
        self.__message_variable.set(message)
        self.__message_label.grid(row=6, column=0, columnspan=5)


    def _hide_message(self):
        self.__message_variable.set('')
        self.__message_label.grid_remove()


    def __initialize(self):
        self._add_frame1()
        self._add_frame2()


    def _add_frame1(self):
        self.__frame1 = ttk.Frame(master=self._root, padding=(0,30,30,30))
        label_headline = ttk.Label(master=self.__frame1, text="LISÄÄ SANOJA")

        self._create_message_button()

        label_lang1 = ttk.Label(master=self.__frame1, text="valitse kielet,")
        label_lang2 = ttk.Label(master=self.__frame1, text="kopioi tai kirjoita")
        label_lang3 = ttk.Label(master=self.__frame1, text="sanat kenttiin")
        label_lang4 = ttk.Label(master=self.__frame1, text="allekkain")
        label_lang5 = ttk.Label(master=self.__frame1, text=" ")

        button_main = ttk.Button(
            master=self.__frame1,
            text="takaisin päävalikkoon",
            command=self.__handle_main
        )
        button_submit = ttk.Button(
            master=self.__frame1,
            text="TALLENNA",
            command=lambda: self.__save_words()
        )

        self.create_option_menus()

        label_headline.grid(row=0, column=3)

        button_main.grid(row=0, column=5, sticky='e')

        button_submit.grid(row=2, column=5, sticky='e')

        label_lang1.grid(row=1, column=3)
        label_lang2.grid(row=2, column=3)
        label_lang3.grid(row=3, column=3)
        label_lang4.grid(row=4, column=3)
        label_lang5.grid(row=5, column=3)

        self.option_menu_orig.grid(row=5, column=1, sticky='e')
        self.option_menu_transl.grid(row=5, column=5, sticky='w')


    def _add_frame2(self):
        self.__frame2 = ttk.Frame(master=self._root, padding=(30,0,30,30), width=80)

        self.textarea_words_orig = Text(master=self.__frame2, height=25, width=40)
        self.textarea_words_transl = Text(master=self.__frame2, height=25, width=40)

        self.textarea_words_orig.pack(side='left')
        self.textarea_words_transl.pack(side='left')


    def _create_message_button(self):
        self.__message_variable = StringVar(self.__frame1)
        self.__message_label = ttk.Label(
            master=self.__frame1,
            textvariable=self.__message_variable,
            foreground='green'
        )


    def create_option_menus(self):
        self.option_var_orig = tk.StringVar(self.__frame1)
        self.option_var_transl = tk.StringVar(self.__frame1)

        self.label_orig = ttk.Label(master=self.__frame1,
                                    text='     valitse käännettävä kieli')

        self.label_orig.grid(row=5, column=0, sticky='w')
        self.option_menu_orig = ttk.OptionMenu(
                                            self.__frame1,
                                            self.option_var_orig,
                                            self.lang_options[0],
                                            *self.lang_options,
                                            command=self.option_changed_orig
        )
        self.label_transl = ttk.Label(master=self.__frame1,
                                        text='valitse käännöksen kieli')

        self.label_transl.grid(row=5, column=4, sticky='w')
        self.option_menu_transl = ttk.OptionMenu(
                                            self.__frame1,
                                            self.option_var_transl,
                                            self.lang_options[0],
                                            *self.lang_options,
                                            command=self.option_changed_transl
        )
        self._hide_message()


    def option_changed_orig(self, lang_orig='suomi'):
        self.lang_orig = lang_orig


    def option_changed_transl(self, lang_transl='englanti'):
        self.lang_transl = lang_transl


    def __save_words(self):
        words_orig = self.textarea_words_orig.get('1.0', 'end')
        words_transl = self.textarea_words_transl.get('1.0', 'end')

        words_orig = AddWordsView._prepare_input__to_list_of_words(words_orig)
        words_transl = AddWordsView._prepare_input__to_list_of_words(words_transl)

        if self._check_words_input_ok(words_orig, words_transl):

            self.__word_service._add_words(
                words_orig, self.lang_orig, words_transl, self.lang_transl)

            self.textarea_words_orig.delete('1.0', 'end')
            self.textarea_words_transl.delete('1.0', 'end')

            self._show_message("Sanat tallennettiin sanastoon")


    @classmethod
    def _prepare_input__to_list_of_words(cls, words):
        return list([word for word in words.strip().split('\n') if word != ''])


    def _check_words_input_ok(self, words_orig, words_transl):

        if len(words_orig) == 0 or len(words_orig) != len(words_transl):
            self._show_message("Sanoja ei tallennettu, tarkista sanalistojen pituudet")
            return False

        elif self.lang_orig == self.lang_transl:
            self._show_message(f"sanojen kielet olivat {self.lang_orig} ja {self.lang_transl}, tarkista kielivalinnat")
            return False

        return True
