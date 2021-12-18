from turno import *
class Tipo_profesor:
    listatipoprofesor = []

    def __init__(self, tipo_profesor):
        self.__tipo_profesor = tipo_profesor
        self.__turno = Turno()

    def registrar_tipo_profesor():
        print("Registrar tipo de profesor\n")
        tipo_profesor = input("Ingrese el tipo de profesor: ")
        turno = input("Introduzca el turno del profesor: ")
        objTipoProfesor = Tipo_profesor(tipo_profesor, turno)
        Tipo_profesor.listatipoprofesor.append(objTipoProfesor)

    def elimninar_tipo_profesor():
        print("Eliminar tipo de profesor\n")
        borrar = input("Escriba el tipo de profesor que desea eliminar: ")
        bo = Tipo_profesor.listatipoprofesor.pop(borrar)
        print("-------------------")
        print("------------------------")
        print("Se ha eliminado con exito")
    
    def buscar_tipo_profesor():
        print("Buscar tipo profesor\n")
        buscar = input("Escriba el tipo de profesor que desea encontrar: ")
        bu = Tipo_profesor.listatipoprofesor.index(buscar)
        print("-------------------")
        print("Buscando------------------------")
        print(f"El edificio que busca se encuentra en: {bu}")
    
    def modificar_edificio():
        print("Modificar tipo de profesor\n")
        numi = int(input("Ingrese el indice que desea modificar: "))
        print(Tipo_profesor.listatipoprofesor[: numi])
        modi = input("Ingrese la modificacion que desea realizar: ")
        Tipo_profesor.listatipoprofesor[:numi] = [modi]
        print(Tipo_profesor.listatipoprofesor)

    def get_tipo_profesor(self):
        return self.__tipo_profesor 

    def set_tipo_profesor(self, tipo_profesor):
        self.__tipo_profesor = tipo_profesor

    tipo_profesor = property(get_tipo_profesor, set_tipo_profesor)