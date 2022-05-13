from tkinter import ttk, constants
from services.user_service import (
    user_service as default_user_service
)


class MainView:
    def __init__(self, root, handle_login, handle_register,  handle_main,
        handle_practise, handle_add_words, user_service=default_user_service
            ):
        self.__root = root
        self.__user_service = user_service
        self.__handle_main = handle_main
        self.__handle_login = handle_login
        self.__handle_register = handle_register
        self.__handle_practise = handle_practise
        self.__handle_add_words = handle_add_words
        self.__user = self.__user_service.get_current_user()
        self.__frame = None
        self.__initialize()


    def pack(self):
        self.__frame.pack(fill=constants.X)


    def destroy(self):
        self.__frame.destroy()


    def __logout_handler(self):
        self.__user_service.logout()
        self.__user = None
        self.__handle_main()


    def __initialize(self):
        self.__frame = ttk.Frame(master=self.__root, padding=30)

        label_welcome = ttk.Label(
            master=self.__frame,
            text="Tervetuloa sanastotreeniin!",
            font=('default', 12, 'bold')
        )

        if self.__user:

            label_username = ttk.Label(
            master=self.__frame,
            text=f"Kirjautuneena {self.__user.name}"
                )

            button_add_words = ttk.Button(
                master=self.__frame,
                text="Lisää sanoja",
                width=12,
                command=self.__handle_add_words
                )

            button_logout = ttk.Button(
                master=self.__frame,
                text="Kirjaudu ulos",
                width=12,
                command=self.__logout_handler
                )

        button_practise = ttk.Button(
            master=self.__frame,
            text="HARJOITTELE",
            width=12,
            command=self.__handle_practise
            )

        button_login = ttk.Button(
            master=self.__frame,
            text="KIRJAUDU",
            width=12,
            command=self.__handle_login
            )

        button_register = ttk.Button(
            master=self.__frame,
            width=12,
            text="rekisteröidy",
            command=self.__handle_register
            )

        label_info = ttk.Label(
            master=self.__frame,
            foreground='green',
            text="""Kirjautuneena voit lisätä sanoja
            ja edistymisesi tallentuu\n
            voit harjoitella sanastoa
            myös ilman kirjautumista"""
        )

        if self.__user:
            label_username.grid(row=1, column=0, pady=10, sticky='w')
            button_logout.grid(row=0, column=1)
            button_add_words.grid(row=1, column=1)

        else:
            button_login.grid(row=0, column=1, padx=25)
            button_register.grid(row=1, column=1, padx=25)
            label_info.grid(row=1, column=0)

        label_welcome.grid(row=0, column=0)
        button_practise.grid(row=2, column=1, padx=25)
