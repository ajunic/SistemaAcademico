from Persona import Persona
from testAnalytics import *
from curso import Curso

class Estudiante(Persona):

    contador_estudiante = 0
    listaEstudiantes = []

    def __init__(self, tipo, nombre, apellido, cedula, direccion, telefono,
                 fecha_nacimiento, email, num_carnet, obj_matricula = []):
        Estudiante.contador_estudiante += 1
        super().__init__(tipo, nombre, apellido, cedula, direccion,
                         telefono, fecha_nacimiento, email)
        self.num_carnet = num_carnet
        self.obj_matricula = obj_matricula
        self.__id_estudiante = Estudiante.contador_estudiante

    def __str__(self):
        return f"""\nEstudiante:[ ID: {self.__id_estudiante}
        #Carnet: {self.num_carnet}
        #Matricula: {self.obj_matricula}]
        \t{super().__str__()}
        """

    #Método para registrar un nuevo estudiante
    def registrarEstudiante():
        print('Registro de estudiante\n')
        tipo = input('Ingrese el tipo de estudiante: ')
        nombre = input('Ingrese nombre: ')
        apellido = input('Ingrese apellido: ')
        cedula = input('Ingrese cedula: ')
        direccion = input('Ingrese direccion: ')
        telefono = input('Ingrese el telefono: ')
        fecha_nac = input('Ingrese fecha de nacimiento: ')
        email = input('Ingrese email: ')
        num_carnet = input('Ingrese numero de carnet: ')

        objetoEstudiente = Estudiante(tipo, nombre, apellido, cedula, direccion, telefono, fecha_nac, email, num_carnet)
        Estudiante.listaEstudiantes.append(objetoEstudiente)

    def mostrar_estudiantes():
        for i in Estudiante.listaEstudiantes:
            print(i)

    def elimninar_estudiante():
        print("Eliminar Estudiante\n")
        borrar = input("Escriba el nombre del estudiante que desea eliminar: ")
        bo = Estudiante.listaEstudiantes.pop(borrar)
        print("-------------------")
        print("------------------------")
        print("Se ha eliminado con exito")

    def __gt__(self, other):
        """Comparamos nota para aplicar descuento o no"""
        precio_descuento= 0
        if other.__nota > 90:
            precio_descuento = 0.9* other.__precio
            return print (f'El precio con descuento es: {precio_descuento}')

    # define setter and getter methods for Estudiante attributes
    def get_num_carnet(self):
        return self.__num_carnet

    def set_num_carnet(self, num_carnet):
        self.__num_carnet = num_carnet
    #Property
    num_carnet = property(get_num_carnet, set_num_carnet)