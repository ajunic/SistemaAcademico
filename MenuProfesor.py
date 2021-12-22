from curso import *
from programa import *
from Profesor import *
from edificio import *
from Estudiante import *
from aula import *
from tipoProfesor import *
from turno import *

def admi_profesor():
    numero = 0
    # numero=int(input("Ingrese el numero de servicios que desea verificar: "))
    print("Bienvenido a Servicios Docente")
    # Menu de docente.
    while (numero <= 3):
        print("\t MENU")
        print("1. Ingresar como docente:")
        print("2. Mostrar cursos a cargo de docente:")
        print("3. Salir")
        numero = int(input("Ingrese el numero de servicios que desea verificar: "))

        if numero == 1:
            print("\t Registro de Docente")
            Profesor.registrar_docente()
        elif numero == 2:
            print("\t Mostrar cursos a cargo de docente")
            Profesor.mostrar_docente()
        elif numero == 3:
            break
