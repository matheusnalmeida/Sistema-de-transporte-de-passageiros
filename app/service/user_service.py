from flask_login import login_user
from app.models.result import Result
from app.models.entities.user import User
from app.extensions import db

class UserService:
    def __init__(self) -> None:
        pass
    
    def login(self, username, password):
        if not username or not password:
            return Result(success=False, message="É necessário informar o usuário e senha para logar!")
        
        user = User.query.filter_by(login=username).first()

        if user and user.check_password(password):
            login_user(user, remember='y')
            return Result(success=True)
        else:
            return Result(success=False, message="Não foi encontrado usuário com o usuário e senha informados!")

    def insert_user(self, user: User) -> Result:
        result = user.is_valid()
        if not result.success:
            return result
        
        userAlreadyExistsByName =  User.query.filter_by(name=user.name).first()
        if userAlreadyExistsByName:
           return Result(success=False, message="Ja existe um usuário cadastrado com o nome informado!")

        userAlreadyExistsByCPF =  User.query.filter_by(cpf=user.cpf).first()
        if userAlreadyExistsByCPF:
           return Result(success=False, message="Ja existe um usuário cadastrado com o cpf informado!")
        
        userAlreadyExistsByLogin =  User.query.filter_by(login=user.login).first()
        if userAlreadyExistsByLogin:
           return Result(success=False, message="Ja existe um usuário cadastrado com o login informado!")
        
        db.session.add(user)
        db.session.commit()
        return Result(success= True, message= "Usuário registrado com sucesso!")
        