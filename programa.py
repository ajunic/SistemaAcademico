from curso import Curso
import datetime
lista_programas=[]
descuento=0

class Programa:
    
    def __init__(self,  nombre_programa, fecha_creacion_programa, status_programa, director,duracion ,curso=[]):
        self.__nombre_programa = nombre_programa
        self.__fecha_creacion_programa = fecha_creacion_programa
        self.__status_programa = status_programa #status_programa = 0
        self.__director = director
        self.__duracion = duracion
        self.__curso=[] #agregacion
        

           

    def __str__(self):
        return self.__curso
    
    def agregar_curso(self, curso):
        self.__curso.append(curso)

    def quitar_curso(self, curso):
        self.__curso.remove(curso)

       
    def mostrar_curso(self):
        for curso in self.__curso:
            print(curso)
        return self.__curso

    def limitar_curso(self):
        if len(self.__curso) < 3:
            print("El programa tiene mas de 3 cursos")
        else:
            print("El programa tiene menos de 3 cursos")
    

    #Definir setter y getter
    def get_nombre_programa(self):
        return self.__nombre_programa

    def set_nombre_programa(self, nombre_programa):
        self.__nombre_programa = nombre_programa

    def get_fecha_creacion_programa(self):
        return self.__fecha_creacion_programa

    def set_fecha_creacion_programa(self, fecha_creacion_programa):
        self.__fecha_creacion_programa = fecha_creacion_programa

    def get_status_programa(self):
        return self.__status_programa

    def set_status_programa(self, status_programa):
        self.__status_programa = status_programa

    def get_director(self):
        return self.__director

    def set_director(self, director):
        self.__director = director

    #Definir property
    nombre_programa = property(get_nombre_programa, set_nombre_programa)
    fecha_creacion_programa = property(get_fecha_creacion_programa, set_fecha_creacion_programa)
    status_programa = property(get_status_programa, set_status_programa)
    director = property(get_director, set_director)

    #no se cual es la funcion main ,
    def main():
        pass
    
    def __eq__ (self, other):
        """ Comprobar la duracion y aplicar descuento"""
        
        if self.__duracion == 5:
            precio_descuento= 0.9* other.precio
        
        elif self.__duracion==4:
            precio_descuento=0.95* other.precio
    
        

    def amdministrar_programa(self, op):
        if op == 1:

            print("Crear un programa \n")
            id_programa = int(input("Digite el ID del programa: "))
            nombre_programa = input("Ingrese el nombre del nuevo programa: ").lower()
            fecha_creacion = datetime
            status = input("Digite status si es 'activo' o 'inactivo': ").lower()
            director = input("Digite el nombre del director: ")
            obj_programa = Programa(id_programa, nombre_programa, fecha_creacion, status, director)
            lista_programas.append(obj_programa)
        if op == 2:

            print("Buscar Programa\n")
            id_programa = int(input("Digite el ID del programa: "))
            for obj_programa in lista_programas:
                if id_programa == obj_programa:
                    print("Nombre del programa: ".format(nombre_programa))
                    print("Fecha de creacion: {%c}".format(fecha_creacion))
                    print("Estatus del Programa: ".format(status))
                    print("Nombre del director: ".format(director))

        if op == 3:

            print("Listado de todos los programas \n")
            for obj_programa in lista_programas:
                print(obj_programa)

        if op == 4:
            print("Modifique un programa existente\n")
            id_programa = int(input("Digite el ID del programa: "))
            for obj_programa in lista_programas:
                if id_programa == obj_programa:
                    id_programa = int(input("Digite el nuevo ID del programa: "))
                    nombre_programa = input("Ingrese el nombre del programa: ")
                    fecha_creacion = datetime
                    status = input("Digite status si es 'activo' o 'inactivo': ").lower()
                    director = input("Digite el nombre del director: ")
                    obj_programa = Programa(id_programa, nombre_programa, fecha_creacion, status, director)
                    lista_programas.append(obj_programa)
                    print("Programa modificado exitosamente!")
        else:
            return Programa.main()  #cual es???




ing1 =Programa("ingenieria_Civil", "12/12/12", "activo", "Juan",10, ["Calculo2", "fisica"])
ing2= Programa("Arquitectura", "12/15/16", "activo", "Juan","10")
cur1=Curso("Calculo4", 5, 20,"Ingenieria civil",90)

print(ing1.director)

print(ing2.__dict__)
