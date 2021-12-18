from curso import Curso
import datetime

class Programa:
    contador_programa = 0
    lista_programas=[]

    def __init__(self,  nombre_programa, fecha_creacion, status_programa, director, mini, maxi, duracion):
        Programa.contador_programa += 1
        self.__nombre_programa = nombre_programa
        self.__fecha_creacion_programa = fecha_creacion
        self.__status_programa = status_programa #status_programa = 0
        self.__director = director
        self.__curso=[] #agregacion
        self.__maxi = maxi
        self.__mini = mini
        self.__duracion = duracion
        self.__id = Programa.contador_programa
        
    def __str__(self):
        return self._curso
    
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

    def set_curso(self, curso):
        self.__curso.append(curso)

    def get_curso(self):
        return self.__curso

    #Definir property
    nombre_programa = property(get_nombre_programa, set_nombre_programa)
    fecha_creacion_programa = property(get_fecha_creacion_programa, set_fecha_creacion_programa)
    status_programa = property(get_status_programa, set_status_programa)
    director = property(get_director, set_director)
    curso = property(get_curso, set_curso)

    def registrar_programa():
        nombre_programa = input('Ingrese el nombre del programa: ')
        fecha = datetime.today().strftime('%d-%m-%y')
        status_programa = input('Ingrese estado del programa: ')
        director = input('Ingrese nombre del director: ')
        mini = int(input('Ingrese el minimo de cursos: '))
        maxi = int(input('Ingrese el maximo de cursos: '))
        duracion = input('Ingrese la duracion:')
        objetoPrograma = Programa(nombre_programa, fecha, status_programa, director, mini, maxi, duracion)
        Programa.lista_programas.append(objetoPrograma)

    def imprimir_cursos():
        for i in Programa.lista_programas:
            print(f'{i.__nombre_programa}')
            for j in i.__curso:
                print(f'{j.nombre_curso}')
    
    def agregar_curso():
        id_prog = 0
        print('Eliga el programa')
        for i in Programa.lista_programas:
            print(f'{i.__id}. {i.__nombre_programa}')
        id_prog = int(input())

        for i in Programa.lista_programas:
            if id_prog == i.__id:
                id = None
                while id != 0:
                    print('Seleciona el curso que desea agregar (Presione 0 para salir)')
                    for j in Curso.lista_curso:
                        print(f'{j.id_curso}. {j.nombre_curso}')
                    
                    id = int(input())

                    if id == 0 and len(i.__curso) < i.__mini: 
                        print('No ha seleccionado el minimo de cursos')
                        id = None
                        continue
                    
                    elif len(i.__curso) >= i.__maxi:
                        print('Ya ha completado el numero maximo de cursos')
                        break

                    for j in Curso.lista_curso:
                        if j.id_curso == id:
                            i.__curso.append(j)

    def buscar_curso():
        print("Buscar Programa\n")
        id_programa = int(input("Digite el ID del programa: "))
        for obj_programa in lista_programas:
            if id_programa == obj_programa:
                print("Nombre del programa: ".format(nombre_programa))
                print("Fecha de creacion: {%c}".format(fecha_creacion))
                print("Estatus del Programa: ".format(status))
                print("Nombre del director: ".format(director))

    #no se cual es la funcion main ,
    def main():
        pass
    
    def descuento(self ):
        """ Comprobar la duracion y aplicar descuento"""
        
        if self._duracion == 5:
            return self._obj_precio_curso() * 0.1

        elif self._duracion==4:
            return self._obj_precio_curso() * 0.15

    def listar_programa(self):
        print("Listado de todos los programas \n")
            for obj_programa in lista_programas:
                print(obj_programa)
    
    def modificar_programa():
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
        
    def eliminar_programa():
        print("Eliminar programa\n")
        borrar = input("Escriba el nombre del programa que desea eliminar: ")
        bo = lista_programas.pop(borrar)
        print("-------------------")
        print("------------------------")
        print("Se ha eliminado con exito")

curso1=Curso(1,"Python","Curso de Python","10/10/2019",10,10)
ingenieria=Programa("Ingenieria","12 50","Activo", "Juan", 5,5 ,["Python","Java","C++"])
print(ingenieria.descuento())

Curso.crear_curso()
Curso.crear_curso()
# Curso.nombre_id()
Programa.registrar_programa()
Programa.registrar_programa()
Programa.agregar_curso()
Programa.imprimir_cursos()

#Programa.imprimir_cursos()