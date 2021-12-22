from curso import *
from programa import *
from Profesor import *
from edificio import *
from Estudiante import *
from aula import *
from tipoProfesor import *
from turno import *

def admi_estudiante():
    numero = 0
    # numero=int(input("Ingrese el numero de servicios que desea verificar: "))
    print("Bienvenido a Servicios Estudiantiles")
    while (numero <= 3):
        print("\t MENU")
        print("1. Matricularse:")
        print("2. Mostrar cursos :")
        print("3. Salir")
        numero = int(input("Ingrese el numero de servicios que desea verificar: "))
        # Submenu de matricula
        if numero == 1:
            print("\t MATRICULA")
            while (numero <= 3):
                print("\t MENU")
                print("1. Pagar:")
                print("2. Mostrar informacion cursos:")
                print("3. Salir")
                numero = int(input("Ingrese el numero de servicios que desea verificar: "))

                if numero == 1:
                    pass  # metdo para pagar
                elif numero == 2:
                    pass  # metodo para mostrar informacion cursos
                elif numero == 3:
                    break

        elif numero == 2:
            print("\t TUS CURSOS:")
            pass  # metodo para mostrar cursos

        elif numero == 3:
            break
