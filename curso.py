from aula import *

class Curso:
    contador_curso = 0
    __lista_curso = []

    def __init__(self, nombre_curso, creditos, horas_semanales, programa, nota,aulas):

        Curso.contador_curso += 1       
        self.__nota = nota #agregada para punto 7
        self.__nombre_curso = nombre_curso
        self.__creditos = creditos
        self.__horas_semanales = horas_semanales
        self.__programa = programa
        self.__aulas=list(aulas)
        self.__id_curso=Curso.contador_curso
        
    def __str__(self):
        return f"""\nCurso[
        Id: {self.__id_curso}
        Nombre del curso: {self.__nombre_curso} 
        Creditos: " {self.__creditos}
        Horas semanales: " {self.__horas_semanales}
        Programa: " + {self.__programa}
        Nota: " {self.__nota}]"""

    def __del__(self):
        print(f"""Curso: {self.__nombre_curso} {self.__creditos} {self.__horas_semanales}""")

    
    def registrar_curso():
        pass
    
    # define setter and getter methods
    def get_nombre_curso(self):
        return self.__nombre_curso

    def set_nombre_curso(self, nombre_curso):
        self.__nombre_curso = nombre_curso

    def get_creditos(self):
        return self.__creditos

    def set_creditos(self, creditos):
        self.__creditos = creditos

    def get_horas_semanales(self):
        return self.__horas_semanales

    def set_horas_semanales(self, horas_semanales):
        self.__horas_semanales = horas_semanales

    def get_programa(self):
        return self.__programa

    def set_programa(self, programa):
        self.__programa = programa

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
    def show(self):
        print ("Nombre del curso: ", self.nombre_curso)

    #Agregar aula de manera independiente a la orden
    def agregar_aula(self, aula): #Devolvera None
        self.__aulas.append(aula)

    #Ver curso con sus aulas
    def __str__(self) -> str:
        aulas_str = ''
        
        for aula in self.__aulas:
            aulas_str += aula.__str__() + '|'
        return f"Curso: {self.__id_curso}, Aulas: {aulas_str}"
    
    #Crearcurso

    def crear_curso(cls):
        nombre_curso = input("Ingrese nombre de la materia: ")
        creditos = input("Ingrese nombre de la materia: ")
        horas_semanales = input("Ingrese nombre de la materia: ")
        curso = Curso(nombre_curso=nombre_curso, creditos=creditos, horas_semanales= horas_semanales, aulas='')
        return curso
    
  

    def show(self):
        print ("Nombre del curso: ", self.nombre_curso)

    def administrar_Curso(): #Devolvera None
        pass









