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
        self.__tipo = tipo
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__direccion = direccion
        self.__telefono = telefono
        self.__fecha_nacimiento = fecha_nacimiento
        self.__email = email
        self.id_persona = Persona.contador_personas
    
    #def crear_persona(self):
    #    return Persona(self.nombre, self.apellido, self.cedula, self.direccion, self.telefono, self.email, self.fecha_nacimiento)

    # define setter and getter methods for nombre
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # define setter and getter methods for apellido
    def get_apellido(self):
        return self.__apellido
    
    def set_apellido(self, apellido):
        self.__apellido = apellido

    # define setter and getter methods for cedula
    def get_cedula(self):
        return self.__cedula
    
    def set_cedula(self, cedula):
        self.__cedula = cedula

    # define setter and getter methods for direccion
    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self, direccion):
        self.__direccion = direccion

    # define setter and getter methods for telefono
    def get_telefono(self):
        return self.__telefono
    
    def set_telefono(self, telefono):
        self.__telefono = telefono

    # define setter and getter methods for fecha_nacimiento
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    # define setter and getter methods for email
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

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
                telefono:{4} - fecha_nacimiento:{5} - email:{6} """.format(self.__nombre,
                                                                self.__apellido,
                                                                self.__cedula,
                                                                self.__direccion,
                                                                self.__telefono,
                                                                self.__fecha_nacimiento,
                                                                self.__email))

    def mostrar_detalle(self):
        print(f'Persona: {self.__tipo} {self.__nombre} {self.__apellido} {self.__cedula}'
              f'{self.__direccion}{self.__telefono} {self.__fecha_nacimiento} {self.__email}')

    def __str__(self):
        return f"""\nPersona:[{self.id_persona}
        Nombre: {self.nombre} 
        Apellido: {self.apellido}
        Cedula: {self.cedula}
        Direccion: {self.direccion}
        Telefono: {self.telefono}
        Fecha de Nacimiento: {self.fecha_nacimiento}
        Email: {self.email}]
        """

    def __del__(self):
        print(f'Persona: {self.__tipo} {self.__nombre} {self.__apellido} {self.__cedula}'
              f'{self.__direccion} {self.__telefono} {self.__fecha_nacimiento} {self.__email}')
