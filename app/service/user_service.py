class UserService:
    def __init__(self) -> None:
        self.database = MemoryDatabase.instance()

    def insert_user(self, user: User) -> ServiceResponse:
        userAlreadyExists = self.__get_user_by_username(user.usuario)
        if userAlreadyExists:
            return ServiceResponse(success= False,message= "Ja existe um usuário cadastrado com este nome de usuário!")

        if (user.is_valid()):
           self.database.users_table[user.id] = user 
           return ServiceResponse(success=True, message="Usuário registrado com sucesso!")

        return ServiceResponse(success= False,message= "Existem informações inválidas!")

    def login(self, username: str, password: str) -> ServiceResponse:
        user  = self.__get_user_by_username_pass(username, password)
        if user:
            user.senha = None
            return ServiceResponse(success=True, data=user)
        else:
            return ServiceResponse(success=False, message="Usuário ou senha inválidos!")
    
    def __get_user_by_username(self, username: str) -> User:
        for id in self.database.users_table:
            user = self.database.users_table[id]
            if user.usuario == username:
                return copy.copy(user)   

    def __get_user_by_username_pass(self, username: str, password: str) -> User:
        for id in self.database.users_table:
            user = self.database.users_table[id]
            if user.usuario == username and user.senha == password:
                return copy.copy(user)             