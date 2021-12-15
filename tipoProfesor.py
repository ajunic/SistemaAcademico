from turno import *
class Tipo_profesor:

    lista_tipo_profesor = []

    
    #Metodo para registrar un nuevo Tipo de profesor
    def registrar_tipos_profesor():
        print("Registro de Tipo de profesor\n")
        t_profesor = input("Ingrese un tipo de profesor")
        objtipoProfesor = t_profesor

        Tipo_profesor.lista_tipo_profesor.append(objtipoProfesor)

    def mostrar_tipos_profesor():
        for i in Tipo_profesor.lista_turnos:
            print (i)

    def eliminar_tipo_profesor():
        print("Eliminar Tipo de profesor\n")
        t_profesor = input("Ingrese el tipo de profesor a eliminar: ")
        for i in Tipo_profesor.lista_tipo_profesor:
            if t_profesor == i:
                Tipo_profesor.lista_tipo_profesor.remove(i)

    
    def __init__(self, tipo_profesor):
        self.__tipo_profesor = tipo_profesor
        self.__turno = Turno()

    def get_tipo_profesor(self):
        return self.__tipo_profesor 

    def set_tipo_profesor(self, tipo_profesor):
        self.__tipo_profesor = tipo_profesor

    tipo_profesor = property(get_tipo_profesor, set_tipo_profesor)


