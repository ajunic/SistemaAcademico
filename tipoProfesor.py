from turno import *
class Tipo_profesor:
    def __init__(self, tipo_profesor):
        self.__tipo_profesor = tipo_profesor
        self.__turno = Turno()

    def get_tipo_profesor(self):
        return self.__tipo_profesor 

    def set_tipo_profesor(self, tipo_profesor):
        self.__tipo_profesor = tipo_profesor

    tipo_profesor = property(get_tipo_profesor, set_tipo_profesor)