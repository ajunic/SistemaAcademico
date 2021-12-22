
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

    def get_turno(self):
        return self.__turno

    def set_turno(self, turno):
        self.__turno = turno

    turno = property(get_turno, set_turno)

    def administrar_turno():
        while (numero <= 4):
            print("\t MENU")
            print("1. Registrar nuevos turnos")
            print("2. Eliminar turnos")
            print("3. Buscar turnos")
            print("4. SALIR")
            numero=int(input("Ingrese el numero de servicios que desea verificar: "))

            if numero==1:
                print("\t Registrar nuevo turno")
                Turno.registrar_turno()
                                        
            elif numero==2:
                print("\t Eliminar turno")
                Turno.elimninar_turno()
                                        
            elif numero==3:
                print("\t Buscar turno")
                Turno.buscar_turno()
                                        
            elif numero==4:
                break