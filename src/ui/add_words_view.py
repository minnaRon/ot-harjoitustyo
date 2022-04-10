import tkinter as tk
from tkinter import Text, ttk, constants
from services.word_service import (
    WordAddingError,
    word_service as default_word_service
)


class AddWordsView:
    def __init__(self, root, handle_main,
                 word_service=default_word_service
                 ):
        self._root = root
        self.__handle_main = handle_main
        self.__frame = None
        self.__word_service = word_service
        self.lang_orig = 'suomi'
        self.lang_transl = 'suomi'
        self.lang_options = ('suomi', 'englanti')
        self.textarea_content_orig = None
        self.textarea_content_transl = None
        self.option_var = None

        self.__initialize()

    def pack(self):
        self.__frame.pack(fill=constants.X)

    def destroy(self):
        self.__frame.destroy()

    def __initialize(self):
        self.__frame = ttk.Frame(master=self._root)
        label_headline = ttk.Label(master=self.__frame, text="LISÄÄ SANOJA")

        label_lang1 = ttk.Label(master=self.__frame, text="valitse kielet,")
        label_lang2 = ttk.Label(master=self.__frame, text="kopioi tai kirjoita")
        label_lang3 = ttk.Label(master=self.__frame, text="sanat kenttiin")
        label_lang4 = ttk.Label(master=self.__frame, text=" ")
        label_lang5 = ttk.Label(master=self.__frame, text=" ")

        button_main = ttk.Button(
            master=self.__frame,
            text="takaisin päävalikkoon",
            command=self.__handle_main
        )
        button_submit = ttk.Button(
            master=self.__frame,
            text="TALLENNA",
            command=lambda: self.__save_words()
        )
        self.textarea_words_orig = Text(master=self.__frame, height=25, width=40)
        self.textarea_words_transl = Text(master=self.__frame, height=25, width=40)
        self.option_var_orig = tk.StringVar(self.__frame)
        self.option_var_transl = tk.StringVar(self.__frame)
        self.create_option_menus()

        label_headline.pack()
        button_main.pack()
        button_main.place(x=1000, y=10)

        button_submit.pack()
        button_submit.place(x=1000, y=70)

        label_lang1.pack()
        label_lang2.pack()
        label_lang3.pack()
        label_lang4.pack()
        label_lang5.pack()

        self.textarea_words_orig.pack(side='left')
        self.textarea_words_transl.pack(side='left')
        self.option_menu_orig.pack()
        self.option_menu_orig.place(x=340, y=150)
        self.option_menu_transl.pack()
        self.option_menu_transl.place(x=1000, y=150)

    def create_option_menus(self):
        paddings = {'padx': 5, 'pady': 5}

        self.label_orig = ttk.Label(master=self.__frame,
                                    text='valitse käännettävä kieli')
        self.label_orig.pack()
        self.label_orig.place(x=10, y=155)
        self.option_menu_orig = ttk.OptionMenu(
                                            self.__frame,
                                            self.option_var_orig,
                                            self.lang_options[0],
                                            *self.lang_options,
                                            command=self.option_changed_orig
        )

        self.label_transl = ttk.Label(master=self.__frame,
                                        text='valitse käännöksen kieli')
        self.label_transl.pack()
        self.label_transl.place(x=680, y=155)
        self.option_menu_transl = ttk.OptionMenu(
                                            self.__frame,
                                            self.option_var_transl,
                                            self.lang_options[0],
                                            *self.lang_options,
                                            command=self.option_changed_transl
        )

    def option_changed_orig(self, lang_orig='suomi'):
        self.lang_orig = lang_orig

    def option_changed_transl(self, lang_transl='englanti'):
        self.lang_transl = lang_transl

    def __save_words(self):
        words_orig = self.textarea_words_orig.get('1.0', 'end')
        words_transl = self.textarea_words_transl.get('1.0', 'end')

        words_orig = list(
            [word for word in words_orig.strip().split('\n') if word != ''])
        words_transl = list(
            [word for word in words_transl.strip().split('\n') if word != ''])

        # TEE näkymässä näkyvä virheviesti näille vv
        if self.lang_orig == self.lang_transl:
            raise WordAddingError(
                f"sanojen kielet olivat {self.lang_orig} ja {self.lang_transl}, tarkista kielivalinnat")

        if len(words_orig) == len(words_transl):
            self.textarea_content_orig = words_orig
            self.textarea_content_transl = words_transl
            self.__word_service._add_words(
                words_orig, self.lang_orig, words_transl, self.lang_transl)
        else:
            raise WordAddingError(
                "Sanalistat ovat eripituiset, tarkista sanalistat")
        self.textarea_words_orig.delete('1.0', 'end')
        self.textarea_words_transl.delete('1.0', 'end')
