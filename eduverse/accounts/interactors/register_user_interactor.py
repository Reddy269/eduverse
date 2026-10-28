from accounts.interactors.dtos import RequestRegisterUserDTO, RequestCreateUserDTO
from accounts.interactors.core import CreateUserInteractor
from accounts.interactors.ports import  PublishEventInerface
from django.db import transaction
from accounts.interactors.ports.publish_interfaces import StudentRegistredDTO

from accounts.interactors.ports.publish_interfaces import StudentRegistredDTO


class RegisterUserInteractor:
    def __init__(self,
                 request:RequestRegisterUserDTO,
                 signal :PublishEventInerface,
                 create_user : CreateUserInteractor,
                 ):
        self.request = request
        self.signal = signal
        self.create_user = create_user

    def execute(self,):
        create_request = RequestCreateUserDTO(name=self.request.name,email=self.request.email,password=self.request.password,usertype="student")
        with transaction.atomic():
            #first the storage part is dealt with
            user_data = self.create_user.create(request=create_request)
            #then the signal is sent if user_data is successfully created
            register_user = StudentRegistredDTO(id = user_data.id, name=user_data.name, email=user_data.email)
            self.signal.send_signal(register_user)
        return user_data








