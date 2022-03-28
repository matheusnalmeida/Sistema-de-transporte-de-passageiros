class UserViewModel():
    def __init__(self, name = '', birth_date = '', cpf = '', address = '', login = '', password = '') -> None:
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf
        self.address = address
        self.login = login
        self.password = password