from curso import *
from programa import *
from Profesor import *
from edificio import *
from Estudiante import *
from aula import *
from tipoProfesor import *
from turno import *
from MenuEstudiante import *
from MenuProfesor import *
from MenuCatalogo import *

# Programa principal
"""Autores:-    
    -Rodolfo Melendez
    -Ashly Ramos
    -Guillermo Carvajal1

    -Michael Gomez
    -Rodolfo Melendes
    -Blandino
    -Armando Ugarte

"""


def salto_linea():
    print("\n")
    print("|****************************|")
    print("|**|      siguiente       |**|")
    print("|**|         Menu         |**|")
    print("|****************************|")
    print("\n")


print("\n")
print("|****************************|")
print("|**|      Bienvenidos     |**|")
print("|**|         Menu         |**|")
print("|****************************|")
print("")
"""
print("Bienvenido al sistema mas mamalon de este curso de python avanzado")
print("Por favor ingrese los datos solicitados")
print("Siga las indicaciones para que el programa funcione correctamente")
print("Sigase las indicaciones para que el programa funcione correctamente ")"""

# variable de control para menu
# print("""Ingrese 1 para Servicios Docente \n 2 Para Servicios estudiantiles \n 3 Para Servicios administrativos \n 4 Para Salir""")
# digito=0

# menu de 4 opciones y sus subramas
"""
while digito<=4:
    print("Ingrese 1 para Verificacion Docente:")
    print("Ingrese 2 para Confirmacion Estudiante:")
    print("Ingrese 3 para Administracion:")
    print("Ingrese 4 para Salir")
    digito=int(input("Ingrese un numero: "))"""

#Registrando Cursos de prueba
curso = Curso('Matematica I', 4, 4, 150)
Curso.lista_curso.append(curso)

curso = Curso('Estadistica', 4, 3, 150)
Curso.lista_curso.append(curso)

curso = Curso('Bases de dato', 2, 3, 180)
Curso.lista_curso.append(curso)

curso = Curso('Programacion I', 3, 6, 180)
Curso.lista_curso.append(curso)

#Registrando programas de prueba
objetoPrograma = Programa('Ing en Sistemas', datetime.today().strftime('%d-%m-%y'), False, 'Juan Caldera', 1, 2, 4)
Programa.lista_programas.append(objetoPrograma)

objetoPrograma = Programa('Ing en Computacion', datetime.today().strftime('%d-%m-%y'), False, 'Juana Peralta', 1, 2, 4)
Programa.lista_programas.append(objetoPrograma)

Programa.lista_programas[0].set_curso(Curso.lista_curso[0])
Programa.lista_programas[0].set_curso(Curso.lista_curso[1])
Programa.lista_programas[1].set_curso(Curso.lista_curso[2])
Programa.lista_programas[1].set_curso(Curso.lista_curso[3])


while (True):
    print("Sistema de control Academico")
    print("-" * 15)
    print("Menu de opciones.")
    print("-" * 15)
    print("""Ingrese 1 para Servicios Docente 
            \n 2 Para Servicios estudiantiles 
            \n 3 Para Servicios administrativos 
            \n 4 Para Salir""")
    try:
        option = int(input("Elija su opcion para el menu"))
        if option == 1:
            admi_profesor()
            # while (numero <= 3):
            #     print("\t MENU")
            #     print("1. Matricularse:")
            #     print("2. Mostrar cursos :")
            #     print("3. Salir")
            #     numero = int(input("Ingrese el numero de servicios que desea verificar: "))
            #     # Submenu de matricula
            #     if numero == 1:
            #         print("\t MATRICULA")
            #         while (numero <= 3):
            #             print("\t MENU")
            #             print("1. Pagar:")
            #             print("2. Mostrar informacion cursos:")
            #             print("3. Salir")
            #             numero = int(input("Ingrese el numero de servicios que desea verificar: "))

            #             if numero == 1:
            #                 pass  # metdo para pagar
            #             elif numero == 2:
            #                 pass  # metodo para mostrar informacion cursos
            #             elif numero == 3:
            #                 break

            #     elif numero == 2:
            #         print("\t TUS CURSOS:")
            #         pass  # metodo para mostrar cursos

            #     elif numero == 3:
            #         break
            # salto_linea()

            # submenu de servicios estudiante
        elif option == 2:
            admi_estudiante()
            salto_linea()
    

            # submenu de servicios administrativos
        elif option == 3:
            #admi_catalogos()
            salto_linea()
            admi_catalogos()

            # salir del menu principal
        elif option == 4:
            print("Gracias por usar nuestro sistema")
            break
    except ValueError as err:
        print(err)
        print("Ingrese de nuevo su opcion")

        # submenu de sercivios docente


# _______________________________________________________________________________




