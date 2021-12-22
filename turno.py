from tipoProfesor import Tipo_profesor


class Turno:
    listaTurno = []

    def __init__(self, turno):
        self.__turno = turno
        
    def registrar_turno():
        print("Registrar turno\n")
        turno = input("Ingrese el nombre del turno: ")
        objTurno = Turno(turno)
        Turno.listaTurno.append(objTurno)

    def elimninar_turno():
        print("Eliminar turno\n")
        borrar = input("Escriba el nombre del turno que desea eliminar: ")
        bo = Turno.listaTurno.pop(borrar)
        print("-------------------")
        print("------------------------")
        print("Se ha eliminado con exito")
    
    def buscar_turno():
        print("Buscar turno\n")
        buscar = input("Escriba el nombre del turno que desea encontrar: ")
        bu = Turno.listaTurno.index(buscar)
        print("-------------------")
        print("Buscando------------------------")
        print(f"El turno que busca se encuentra en: {bu}")
    
    def modificar_turno():
        print("Modificar turno\n")
        numi = int(input("Ingrese el indice que desea modificar: "))
        print(Turno.listaTurno[: numi])
        modi = input("Ingrese la modificacion que desea realizar: ")
        Turno.listaTurno[:numi] = [modi]
        print(Turno.listaTurno)

#prueba de la agregacion entre clase turno contiene a tipo_profesor
# fff = Tipo_profesor("Horario")
# p = Turno("Matutino", fff)
# print(p)
