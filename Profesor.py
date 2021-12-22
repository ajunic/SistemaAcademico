from datetime import date

from aula import Aula
from curso import Curso
from Persona import Persona
from programa import Programa


class Profesor(Persona):
    contador_profesor = 0
    listaProfesor = []

    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_nacimiento,
                 email):#none
        Profesor.contador_profesor = + 1
        super().__init__(nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email)
        self._id_profesor = Profesor.contador_profesor
        self._obj_curso = []
        self._obj_tipo = []

    def __str__(self):
        return f"""\nProfesor:[ ID: {self._id_profesor}
        #Carnet: {self._codigo_profesor}
        #Programa: {self._obj_programa}
        #Curso: {self._obj_curso}]
        {super().__str__()}
        """

    def registrar_docente(self):
        print("Registro de Docente")
        nombre = input("Ingrese el nombre del docente: ")
        apellido = input("Ingrese el apellido del docente: ")
        cedula = input("Ingrese la cedula del docente: ")
        direccion = input("Ingrese la direccion del docente: ")
        telefono = input("Ingrese el telefono del docente: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del docente: ")
        email = input("Ingrese el email del docente: ")
        #obj_programa = Programa.registrar_programa()
        #obj_curso = Curso.crear_curso()
        obj_profesor = Profesor(nombre, apellido, cedula, direccion, telefono, fecha_nacimiento,email)
        Profesor.listaProfesor.append(obj_profesor)

    def mostrar_docente(self):
        for i in Profesor.listaProfesor:
            print(i)


    def elimninar_docente(self):
        print("Eliminar docente\n")
        borrar = input("Escriba el nombre del profesor que desea eliminar: ")
        bo = Profesor.listaProfesor.pop(borrar)
        print("-------------------")
        print("------------------------")
        print("Se ha eliminado con exito")
    
    def buscar_docente(self):
        print("Buscar Docente\n")
        buscar = input("Escriba el nombre del profesor que desea encontrar: ")
        bu = Profesor.listaProfesor.index(buscar)
        print("-------------------")
        print("Buscando------------------------")
        print(f"El edificio que busca se encuentra en: {bu}")
    
    def modificar_docente(self):
        print("Modificar docente\n")
        numi = int(input("Ingrese el indice que desea modificar: "))
        print(Profesor.listaProfesor[: numi])
        modi = input("Ingrese la modificacion que desea realizar: ")
        Profesor.listaProfesor[:numi] = [modi]
        print(Profesor.listaProfesor)

    # define setter and getter methods for Estudiante attributes
    def get_codigo_profesor(self):
        return self._codigo_profesor

    def set_codigo_profesor(self, codigo_profesor):
        self._codigo_profesor = codigo_profesor

    def get_tipo(self):
        return self._obj_tipo
    #Property
    codigo_profesor = property(get_codigo_profesor, set_codigo_profesor)
