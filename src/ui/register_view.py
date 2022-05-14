from tkinter import ttk, constants, StringVar
from services.user_service import (
    user_service as default_user_service,
    CredentialsError
)

class RegisterView:
    def __init__(self, root, handle_main,
                    user_service=default_user_service
        ):
        self.__root = root
        self.__user_service = user_service
        self.__handle_main = handle_main
        self.__frame = None
        self.__entry_username = None
        self.__entry_password1 = None
        self.__entry_password2 = None
        self.__error_variable = None
        self.__error_label = None

        self.__initialize()


    def pack(self):
        self.__frame.pack(fill=constants.X)


    def destroy(self):
        self.__frame.destroy()


    def __register_handler(self):
        username = self.__entry_username.get()
        password1 = self.__entry_password1.get()
        password2 = self.__entry_password2.get()

        if self.__check_correct_input(username, password1, password2):
            try:
                self.__user_service.register(username, password1)
                self.__handle_main()

            except CredentialsError:
                    self._show_error(f"antamasi tunnus {username} on jo käytössä, anna uusi tunnus")


    def _show_error(self, message):
        self.__error_variable.set(message)
        self.__error_label.grid(row=0, column=0, columnspan=3, sticky='w')


    def _hide_error(self):
        self.__error_variable.set('')
        self.__error_label.grid_remove()


    def __initialize(self):

        self.__frame = ttk.Frame(master=self.__root, padding=30)

        self.__error_variable = StringVar(self.__frame)

        self.__error_label = ttk.Label(
            master=self.__frame,
            textvariable=self.__error_variable,
            foreground='green'
        )
        label_title = ttk.Label(
            master=self.__frame,
            text="Rekisteröityminen",
            font=('default', 12, 'bold')
        )
        button_main = ttk.Button(
            master=self.__frame,
            text="takaisin päävalikkoon",
            command=self.__handle_main
        )
        label_username = ttk.Label(
            master=self.__frame,
            text="tunnus: "
        )
        label_password1 = ttk.Label(
            master=self.__frame,
            text="salasana: "
        )
        label_password2 = ttk.Label(
            master=self.__frame,
            text="salasana uudelleen: "
        )
        self.__entry_username = ttk.Entry(
            master=self.__frame,
            width=20
        )
        self.__entry_password1 = ttk.Entry(
            master=self.__frame,
            show="*", width=20
        )
        self.__entry_password2 = ttk.Entry(
            master=self.__frame,
            show="*", width=20
        )
        button_login = ttk.Button(
            master=self.__frame,
            text="tallenna",
            command=self.__register_handler
        )

        label_title.grid(row=1, column=0)
        button_main.grid(row=5, column=0, sticky='w', padx=5, pady=15)
        label_username.grid(row=2, column=0)
        self.__entry_username.grid(row=2, column=1, padx=5, pady=5, sticky='e')
        label_password1.grid(row=3, column=0)
        self.__entry_password1.grid(row=3, column=1, padx=5, pady=5, sticky='e')
        label_password2.grid(row=4, column=0)
        self.__entry_password2.grid(row=4, column=1, padx=5, pady=5, sticky='e')
        button_login.grid(row=5, column=1, padx=5, pady=15, sticky='e')

        self._hide_error()


    def __check_correct_input(self, username, password1, password2):
        error_message = ""
        if len(username) < 2 or len(username) > 20:
            error_message += "tunnuksen pituuden tulee olla 2-20 merkkiä\n"
        if not username:
            error_message += "anna tunnus\n"
        if (password1 or password2) and password1 != password2:
            error_message += "salasanoissa oli eroa"
        if error_message:
            self._show_error(error_message)
        return error_message == ""
