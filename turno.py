
class Turno:

    lista_turno = []

    def __init__(self, turno):
        self.__turno = turno
        

    def agregar_turno ():
        print("Agregar turno \n")
        turno = input("Ingrese un turno: ")
        obj_turno = turno
        Turno.lista_turno.append(obj_turno)

    def eliminar_turno():
        print("Eliminar Turno\n")
        trn = input("Ingrese el turno a eliminar")
        for j in Turno.lista_turno:
            if trn == j:
                Turno.lista_turno.remove(j)

    def mostrar_turnos():
        print("Mostrar Turnos\n")
        for i in Turno.lista_turno:
            print(i)

    def get_turno(self):
        return self.__turno

    def set_turno(self, turno):
        self.__turno = turno

    turno = property(get_turno, set_turno)