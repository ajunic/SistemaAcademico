
class Turno:
    def __init__(self, turno):
        self.__turno = turno
        


    def get_turno(self):
        return self.__turno

    def set_turno(self, turno):
        self.__turno = turno

    turno = property(get_turno, set_turno)