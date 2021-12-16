from aula import *


class Curso:
    contador_curso = 0
    lista_curso = []

    def __init__(self, nombre_curso, creditos, horas_semanales, 
    programa, nota, aulas):

        Curso.contador_curso += 1
        self.__nota = nota  # agregada para punto 7
        self.__nombre_curso = nombre_curso
        self.__creditos = creditos
        self.__horas_semanales = horas_semanales
        self.__programa = programa
        self.__aulas = list(aulas)
        self.__id_curso = Curso.contador_curso

    def __str__(self):
        return f"""\nCurso[
        Id: {self.__id_curso}
        Nombre del curso: {self.__nombre_curso}
        Creditos: " {self.__creditos}
        Horas semanales: " {self.__horas_semanales}
        Programa: " + {self.__programa}
        Nota: " {self.__nota}]"""

    def __del__(self):
        print(
            f"""Curso: {self.__nombre_curso} {self.__creditos} 
            {self.__horas_semanales}""")

    # define getter and setter for nombre_curso
    def get_nombre_curso(self):
        return self.__nombre_curso

    def set_nombre_curso(self, nombre_curso):
        self.__nombre_curso = nombre_curso

    # define getter and setter for creditos
    def get_creditos(self):
        return self.__creditos

    def set_creditos(self, creditos):
        self.__creditos = creditos

    # define getter and setter for horas_semanales
    def get_horas_semanales(self):
        return self.__horas_semanales

    def set_horas_semanales(self, horas_semanales):
        self.__horas_semanales = horas_semanales

    # define getter and setter for programa
    def get_programa(self):
        return self.__programa

    def set_programa(self, programa):
        self.__programa = programa

    # define getter and setter for nota
    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        self.__nota = nota

    # Property definitions for each attribute.
    nombre_curso = property(get_nombre_curso, set_nombre_curso)
    creditos = property(get_creditos, set_creditos)
    horas_semanales = property(get_horas_semanales, set_horas_semanales)
    programa = property(get_programa, set_programa)
    nota = property(get_nota, set_nota)

    # Mostrar nombre del curso
    def show(self):
        print("Nombre del curso: ", self.nombre_curso)

    # Agregar aula de manera independiente a la orden
    def agregar_aula(self, aula):  # Devolvera None
        self.__aulas.append(aula)

    # Ver curso con sus aulas
    def __str__(self) -> str:
        aulas_str = ''

        for aula in self.__aulas:
            aulas_str += aula.__str__() + '|'

        return f"Curso: {self.__id_curso}, Aulas: {aulas_str}"

    # CrearCurso
    def crear_curso():
        print("Crear curso\n")
        nombre_curso = input("Ingrese nombre del curso: ")
        creditos = input("Ingrese la cantidad de creditos: ")
        horas_semanales = input("Ingrese la cantidad de horas semanales: ")
        curso = Curso(nombre_curso=nombre_curso, creditos=creditos,
                      horas_semanales=horas_semanales, aulas='')

        return curso

    # EditarCurso
    def editar_curso(curso):
        print("Editar curso\n")
        curso.nombre_curso = input("Ingrese el nuevo nombre del curso: ")
        curso.creditos = input("Ingrese la nueva direccion del curso: ")
        curso.horas_semanales = input(
            "Ingrese la nueva cantidad de horas semanales: ")

        return curso
    
    #BuscarCurso
    def buscar_curso():
        print("Buscar curso\n")
        buscar = input("Escriba el nombre del curso que desea encontrar: ")
        curso_bu = Curso.lista_curso.index(buscar)
        print("-------------------")
        print("Buscando------------------------")
        print(f"El edificio que busca se encuentra en: {curso_bu}")

    # EliminarCurso
    def eliminar_curso():
        print("Eliminar curso\n")
        borrar = input("Escriba el nombre del curso que desea eliminar: ")
        curso_bo = Curso.lista_curso.pop(borrar)
        print("-------------------")
        print("------------------------")
        print("Se ha eliminado con exito", curso_bo)
  

    def show(self):
        print ("Nombre del curso: ", self.nombre_curso)

    def listar_cursos(lista_curso):
        for i in range(len(lista_curso)):
            print(lista_curso[i])

    def administrar_Curso(): #Devolvera None
        pass

