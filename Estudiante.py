from Persona import Persona
#from testAnalytics import *
from curso import Curso

class Estudiante(Persona):

    contador_estudiante = 0
    listaEstudiantes = []

    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email, num_carnet):
        Estudiante.contador_estudiante += 1
        
        super().__init__(nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email)
        
        self._num_carnet = num_carnet
        self._obj_matricula = []
        self._id_estudiante = Estudiante.contador_estudiante
        #self._nota= int(nota)
        #self._precio= int(Curso._precio)
        

    # def __str__(self):
    #     return f"""\nEstudiante:[ ID: {self.___id_estudiante}
    #     #Carnet: {self._num_carnet}
    #     #Matricula: {self._obj_matricula}]
    #     \t{super().__str__()}
    #     """

    #Método para registrar un nuevo estudiante
    def registrarEstudiante():
        print('Registro de estudiante\n')
        nombre = input('Ingrese nombre: ')
        apellido = input('Ingrese apellido: ')
        cedula = input('Ingrese cedula: ')
        direccion = input('Ingrese direccion: ')
        telefono = input('Ingrese el telefono: ')
        fecha_nac = input('Ingrese fecha de nacimiento: ')
        email = input('Ingrese email: ')
        num_carnet = input('Ingrese numero de carnet: ')

        objetoEstudiente = Estudiante(nombre, apellido, cedula, direccion, telefono, fecha_nac, email, num_carnet)
        Estudiante.listaEstudiantes.append(objetoEstudiente)

    def mostrar_estudiantes(self):
        for i in Estudiante.listaEstudiantes:
            print(i)

    # def __gt__(self, other):
    #     """Comparamos nota para aplicar descuento o no"""
    #     precio_descuento= 0
    #     if self._nota > 90:
    #         precio_descuento = 0.9* other._precio
    #         return print (f'El precio con descuento es: {precio_descuento}')
            
    # def eliminar_estudiante(self):
    #     print("Eliminar estudiante\n")
    #     borrar = input("Escriba el nombre del estudiante que desea eliminar: ")
    #     bo = Estudiante.listaEstudiantes.pop(borrar)
    #     print("-------------------")
    #     print("------------------------")
    #     print("Se ha eliminado con exito")
    
    # def buscar_estudiante(self):
    #     print("Buscar Estudiante\n")
    #     buscar = input("Escriba el nombre del estudiante que desea encontrar: ")
    #     bu = Estudiante.listaEstudiantes.index(buscar)
    #     print("-------------------")
    #     print("Buscando------------------------")
    #     print(f"El edificio que busca se encuentra en: {bu}")
    
    # def modificar_estudiante(self):
    #     print("Modificar estudiante\n")
    #     numi = int(input("Ingrese el indice que desea modificar: "))
    #     print(Estudiante.listaEstudiantes[: numi])
    #     modi = input("Ingrese la modificacion que desea realizar: ")
    #     Estudiante.listaEstudiantes[:numi] = [modi]
    #     print(Estudiante.listaEstudiantes)

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
        return self._num_carnet

    def set_num_carnet(self, num_carnet):
        self._num_carnet = num_carnet
    #Property
    num_carnet = property(get_num_carnet, set_num_carnet)



#create two objects from Estudiante class.
# objetoEstudiante1 = Estudiante('Estudiante', 'Juan', 'Perez', '123456789', 'Calle 1', '12345678', '12/12/1990', 'asa', '12345', '12345')
# objetoEstudiante2 = Estudiante('Estudiante', 'Pedro', 'Perez', '123456789', 'Calle 1', '12345678', '12/12/1990', 'asa', '12345', '12345')

# #use __gt__ method to compare two objects
# objetoEstudiante1 > objetoEstudiante2

