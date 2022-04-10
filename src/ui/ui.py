from tkinter import Tk
from services.practise_service import (
    practise_service as default_practise_service
)
from ui.main_view import MainView
from ui.practise_view import PractiseView
from ui.add_words_view import AddWordsView


class UI:
    def __init__(self, root, practise_service=default_practise_service):
        self.__root = root
        self.__current_view = None
        self.__practise_service = practise_service

    def start(self):
        self.__show_main_view()

    def __hide_current_view(self):
        if self.__current_view:
            self.__current_view.destroy()
        self.__current_view = None

    def handle_button_click(self, button_number):
        self.__practise_service.check_word_pair(button_number - 1)
        # poista vvv kun sanojen vaihto muuttujilla
        self.__show_practise_view()

    def __handle_main(self):
        self.__show_main_view()

    def __handle_add_words(self):
        self.__show_add_words_view()

    def __handle_practise(self):
        self.__practise_service._set_words_to_practise("Finnish", "English")
        self.__show_practise_view()

    def __show_main_view(self):
        self.__hide_current_view()
        self.__current_view = MainView(
            self.__root, self.__handle_practise, self.__handle_add_words)
        self.__current_view.pack()

    def __show_add_words_view(self):
        self.__hide_current_view()
        self.__current_view = AddWordsView(self.__root, self.__handle_main)
        self.__current_view.pack()

    def __show_practise_view(self):
        self.__hide_current_view()
        self.__current_view = PractiseView(
            self.__root, self.__handle_main, self.handle_button_click)
        self.__current_view.pack()
