import tkinter as tk
from tkinter import Tk, Text, ttk, constants, StringVar
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
        # vvvtähän haku/oma lisäys, kun oma sanasto
        self.lang_options = ('suomi', 'englanti')
        self.textarea_content_orig = None
        self.textarea_content_transl = None
        self.option_var = None

# TEE framet tälle; grid ja pack
        self.__initialize()

    def pack(self):
        self.__frame.pack(fill=constants.X)

    def destroy(self):
        self.__frame.destroy()

    def __initialize(self):
        self.__frame = ttk.Frame(master=self._root)
        label_headline = ttk.Label(master=self.__frame, text="LISÄÄ SANOJA")

        self.option_var_orig = tk.StringVar(self.__frame)
        self.option_var_transl = tk.StringVar(self.__frame)
        self.create_widgets()
        label_lang1 = ttk.Label(master=self.__frame, text="valitse kielet,")
        label_lang2 = ttk.Label(master=self.__frame,
                                text="kopioi tai kirjoita")
        label_lang3 = ttk.Label(master=self.__frame, text="sanat kenttiin")
        label_lang4 = ttk.Label(master=self.__frame, text=" ")
        label_lang5 = ttk.Label(master=self.__frame, text=" ")

        # text_words_orig.geometry = ('200x300')'
        self.textarea_words_orig = Text(
            master=self.__frame, height=25, width=40)
        # text_words_orig.title('Sanalista')
        self.textarea_words_transl = Text(
            master=self.__frame, height=25, width=40)

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

        label_headline.pack()
        #label_headline.place(x=500, y=10)
        button_main.pack()
        button_main.place(x=1000, y=10)

        button_submit.pack()
        button_submit.place(x=1000, y=70)

        label_lang1.pack()
        label_lang2.pack()
        label_lang3.pack()
        label_lang4.pack()
        label_lang5.pack()

        #text_words_orig.insert('1.0', 'Kirjoita/siirrä sanat tänne')
        self.textarea_words_orig.pack(side='left')
        self.textarea_words_transl.pack(side='left')

    def create_widgets(self):
        paddings = {'padx': 5, 'pady': 5}

        label_orig = ttk.Label(master=self.__frame,
                               text='valitse käännettävä kieli')
        label_orig.pack()
        # VVVVVVVmuutin
        label_orig.place(x=10, y=155)
        option_menu_orig = ttk.OptionMenu(
            self.__frame,
            self.option_var_orig,
            self.lang_options[0],
            *self.lang_options,
            command=self.option_changed_orig
        )
        option_menu_orig.pack()
        option_menu_orig.place(x=340, y=150)

        label_transl = ttk.Label(
            master=self.__frame, text='valitse käännöksen kieli')
        label_transl.pack()
        label_transl.place(x=680, y=155)
        option_menu_transl = ttk.OptionMenu(
            self.__frame,
            self.option_var_transl,
            self.lang_options[0],
            *self.lang_options,
            command=self.option_changed_transl
        )
        option_menu_transl.pack()
        option_menu_transl.place(x=1000, y=150)

        #self.output_label = ttk.Label(master=self.__frame, foreground='green')
        # self.output_label.pack()

    def option_changed_orig(self, lang_orig='suomi'):
        self.lang_orig = lang_orig
        #self.output.label['text'] = f'valitsit: {self.option_var.get()}'

    def option_changed_transl(self, lang_transl='englanti'):
        self.lang_transl = lang_transl
        #self.output.label['text'] = f'valitsit: {self.option_var.get()}'

    def __save_words(self):

        words_orig = self.textarea_words_orig.get('1.0', 'end')
        words_transl = self.textarea_words_transl.get('1.0', 'end')

        words_orig = list(
            [word for word in words_orig.strip().split('\n') if word != ''])
        words_transl = list(
            [word for word in words_transl.strip().split('\n') if word != ''])
        #print("------------save wo--",words_orig)
        #print("------------save wt--",words_transl)
        # TEE errorviest VVVVVVVVVVVVVVVVVVVVVV
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
