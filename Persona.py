"""La Universidad de Oxford ubicada en inglaterra lo ha contratado a usted para que 
desarrolle un sistema de control academico estudiantil, para tal tarea se cuenta con la 
siguiente información"""

#Author: Armando Jose Ugarte
#Rodolfo Melendez
#Michael Gomez.
#Guillermo Gómez.
#Francisco Blandino.
#Manuel Cáceres.
#Ashly Ramos.

"""Programar la siguiente jerarquia de clases, con su correspondiente prueba de ejecución
en base a lo aprendido en las sesiones de Object-oriented programming – OOP (Esto es 
Class Factory y el uso del decorador @property para la implementación y/o 
operacionalización de propiedades)."""

class Persona:#superclase
    contador_personas = 0
    listaPersona = []

    def __init__(self, tipo, nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email):
        Persona.contador_personas += 1
        self._tipo = tipo
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._direccion = direccion
        self._telefono = telefono
        self._fecha_nacimiento = fecha_nacimiento
        self._email = email
        self._id_persona = Persona.contador_personas
    
    #def crear_persona(self):
    #    return Persona(self.nombre, self.apellido, self.cedula, self.direccion, self.telefono, self.email, self.fecha_nacimiento)

    def eliminar_persona(self):
        print("Eliminar persona\n")
        borrar = input("Escriba el nombre de la persona que desea eliminar: ")
        bo = Persona.listaPersona.pop(borrar)
        print("-------------------")
        print("------------------------")
        print("Se ha eliminado con exito")
    
    def buscar_persona(self):
        print("Buscar Persona\n")
        buscar = input("Escriba el nombre de la persona que desea encontrar: ")
        bu = Persona.listaPersona.index(buscar)
        print("-------------------")
        print("Buscando------------------------")
        print(f"El edificio que busca se encuentra en: {bu}")
    
    def modificar_persona(self):
        print("Modificar persona\n")
        numi = int(input("Ingrese el indice que desea modificar: "))
        print(Persona.listaPersona[: numi])
        modi = input("Ingrese la modificacion que desea realizar: ")
        Persona.listaPersona[:numi] = [modi]
        print(Persona.listaPersona)

    # define setter and getter methods for nombre
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre

    # define setter and getter methods for apellido
    def get_apellido(self):
        return self._apellido
    
    def set_apellido(self, apellido):
        self._apellido = apellido

    # define setter and getter methods for cedula
    def get_cedula(self):
        return self._cedula
    
    def set_cedula(self, cedula):
        self._cedula = cedula

    # define setter and getter methods for direccion
    def get_direccion(self):
        return self._direccion
    
    def set_direccion(self, direccion):
        self._direccion = direccion

    # define setter and getter methods for telefono
    def get_telefono(self):
        return self._telefono
    
    def set_telefono(self, telefono):
        self._telefono = telefono

    # define setter and getter methods for fecha_nacimiento
    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    # define setter and getter methods for email
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email

    # Property definitions for each attribute.
    nombre = property(get_nombre, set_nombre)
    apellido = property(get_apellido, set_apellido)
    cedula = property(get_cedula, set_cedula)
    direccion = property(get_direccion, set_direccion)
    telefono = property(get_telefono, set_telefono)
    fecha_nacimiento = property(get_fecha_nacimiento, set_fecha_nacimiento)
    email = property(get_email, set_email)

    def display(self):
        print("""nombre:{0} - apellido:{1} - cedula:{2} - direccion:{3} -
                telefono:{4} - fecha_nacimiento:{5} - email:{6} """.format(self._nombre,
                                                                self._apellido,
                                                                self._cedula,
                                                                self._direccion,
                                                                self._telefono,
                                                                self._fecha_nacimiento,
                                                                self._email))

    def mostrar_detalle(self):
        print(f'Persona: {self._tipo} {self._nombre} {self._apellido} {self._cedula}'
              f'{self._direccion}{self._telefono} {self._fecha_nacimiento} {self._email}')

    def __str__(self):
        return f"""\nPersona:[{self._id_persona}
        Nombre: {self._nombre} 
        Apellido: {self._apellido}
        Cedula: {self._cedula}
        Direccion: {self._direccion}
        Telefono: {self._telefono}
        Fecha de Nacimiento: {self._fecha_nacimiento}
        Email: {self._email}]
        """

    def __del__(self):
        print(f'Persona: {self._tipo} {self._nombre} {self._apellido} {self._cedula}'
              f'{self._direccion} {self._telefono} {self._fecha_nacimiento} {self._email}')
