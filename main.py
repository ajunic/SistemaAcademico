from mainAdministrar import*
from mainDocente import* 
from mainEstudiante import*
from programa import *



# Programa principal
"""Autores:-    
    -Rodolfo Melendez
    -Ashly Ramos
    -Guillermo Carvajal1

    -Michael Gomez
    -Manuel Caceres 
    -Francisco Blandino
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
        digito = int(input("Elija su opcion para el menu"))   
    except ValueError as err:
        print(err)
        print("Ingrese de nuevo su opcion")
        continue

        # submenu de sercivios docente
        #submenu de sercivios docente
    if digito==1:
        main_Profesor.menu_verificacion() 

        salto_linea()

    #submenu de servicios estudiante
    elif digito==2:
        main_Estudiante.menu_matricula()
    
        salto_linea()        
    #submenu de servicios administrativos        
    elif digito==3:
        main_Administrar_cat.menu_Administracion()

        salto_linea()        
    elif digito==4:
        
        print("Gracias por usar nuestro sistema")
        break


# _______________________________________________________________________________




