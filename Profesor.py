from datetime import date

from aula import Aula
from curso import Curso
from Persona import Persona
from programa import Programa


class Profesor(Persona):
    contador_profesor = 0
    listaProfesor = []

    def __init__(self, tipo, nombre, apellido, cedula, direccion, telefono, fecha_nacimiento,
                 email, codigo_profesor, obj_programa, obj_curso):#none
        Profesor.contador_profesor = + 1
        super().__init__(tipo, nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email)
        self.__id_profesor = Profesor.contador_profesor
        self.codigo_profesor = codigo_profesor
        self.obj_programa = obj_programa
        self.obj_curso = obj_curso

    def __str__(self):
        return f"""\nProfesor:[ ID: {self.__id_profesor}
        #Carnet: {self.codigo_profesor}
        #Programa: {self.obj_programa}
        #Curso: {self.obj_curso}]
        {super().__str__()}
        """

    def registrar_docente():
        print("Registro de Docente")
        nombre = input("Ingrese el nombre del docente: ")
        apellido = input("Ingrese el apellido del docente: ")
        cedula = input("Ingrese la cedula del docente: ")
        direccion = input("Ingrese la direccion del docente: ")
        telefono = input("Ingrese el telefono del docente: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del docente: ")
        email = input("Ingrese el email del docente: ")
        codigo_profesor = input("Ingrese el codigo del docente: ")
        obj_programa = Programa.registrar_programa()
        obj_curso = Curso.crear_curso()
        obj_profesor = Profesor("Docente", nombre, apellido, cedula, direccion, telefono, fecha_nacimiento,email,codigo_profesor,obj_curso,obj_programa)
        Profesor.listaProfesor.append(obj_profesor)

    def mostrar_docente():
        for i in Profesor.listaProfesor:
            print(i)

        
    # define setter and getter methods for Estudiante attributes
    def get_codigo_profesor(self):
        return self.__codigo_profesor

    def set_codigo_profesor(self, codigo_profesor):
        self.__codigo_profesor = codigo_profesor
    #Property
    codigo_profesor = property(get_codigo_profesor, set_codigo_profesor)
