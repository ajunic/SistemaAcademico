from Estudiante import Estudiante
from Profesor import Profesor


class Factoria:
    def factory (type):
        class Estudiante():
            def display(self):
                print("This is new Estudiante")

        class Profesor():
            def display(self):
                print("This is new Profesor")

        if(type == "Estudiante"):
            return Estudiante()
        elif (type == "Profesor"):
            return Profesor()

    def crear_persona(self, nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email):
        if (nombre is 'E'):
            return Estudiante(nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email)
        elif (nombre is 'P'):
            return Profesor(nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email)

