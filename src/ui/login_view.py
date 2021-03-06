from tkinter import ttk, constants, StringVar
from services.user_service import (
    user_service as default_user_service,
    CredentialsError
)

class LoginView:
    def __init__(self, root, handle_main,
                     user_service=default_user_service
                ):
        self.__root = root
        self.__user_service = user_service
        self.__handle_main = handle_main
        self.__frame = None
        self.__entry_username = None
        self.__entry_password = None
        self.__error_variable = None
        self.__error_label = None

        self.__initialize()


    def pack(self):
        self.__frame.pack(fill=constants.X)


    def destroy(self):
        self.__frame.destroy()


    def __login_handler(self):
        username = self.__entry_username.get()
        password = self.__entry_password.get()

        if username:
            
            try:
                self.__user_service.login(username, password)
                self.__handle_main()
            
            except CredentialsError:
                self._show_error('kirjautuminen ei onnistunut, tarkista tunnus ja salasana')          
        
        else:
            self._show_error('anna tunnus')


    def _show_error(self, message):
        self.__error_variable.set(message)
        self.__error_label.grid(row=0, column=0, columnspan=3)


    def _hide_error(self):
        self.__error_variable.set('')
        self.__error_label.grid_remove()    


    def __initialize(self):

        self.__frame = ttk.Frame(master=self.__root, padding=30)
        
        self.__error_variable = StringVar(self.__frame)

        self.__error_label = ttk.Label(
            master=self.__frame,
            textvariable=self.__error_variable,
        )
        button_main = ttk.Button(
            master=self.__frame,
            text="takaisin päävalikkoon",
            width=18,
            command=self.__handle_main
        )
        label_title = ttk.Label(
            master=self.__frame,
            text="Kirjaudu",
            font=('default', 12, 'bold')
        )
        label_username = ttk.Label(
            master=self.__frame,
            text="tunnus: "
        )
        label_password = ttk.Label(
            master=self.__frame,
            text="salasana: "
        )
        self.__entry_username = ttk.Entry(
            master=self.__frame,
            width=20
        )
        self.__entry_password = ttk.Entry(
            master=self.__frame,
            show="*", width=20
        )
        button_login = ttk.Button(
            master=self.__frame,
            text="kirjaudu",
            command=self.__login_handler
        )

        label_title.grid(row=1, column=0, padx=5, pady=5)
        button_main.grid(row=4, column=0, columnspan=2, padx=5, pady=15, sticky='w')
        label_username.grid(row=2, column=0, padx=5, pady=5)
        self.__entry_username.grid(row=2, column=1, padx=5, pady=5, sticky='e')
        label_password.grid(row=3, column=0, padx=5, pady=5)
        self.__entry_password.grid(row=3, column=1, padx=5, pady=5, sticky='e')
        button_login.grid(row=4, column=1, sticky='e', padx=5, pady=15)

        self._hide_error()
