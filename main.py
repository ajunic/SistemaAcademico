from curso import *
from programa import *
from Profesor import *
from edificio import *
from Estudiante import *
from aula import *

#Programa principal
"""Autores:-    
    -Rodolfo Melendez
    -Ashly Ramos
    -Guillermo Carvajal
    -Michael Gomez
    -Rodolfo Melendes
    -Blandino
    -Armando Ugarte

"""

def salto_linea():
    print ("\n")
    print("|****************************|")
    print("|**|      siguiente       |**|")
    print("|**|         Menu         |**|")
    print("|****************************|")
    print ("\n")


print("\n")
print("|****************************|")
print("|**|      Bienvenidos     |**|")
print("|**|         Menu         |**|")
print("|****************************|")
print("")

print("Bienvenido al sistema mas mamalon de este curso de python avanzado")
print("Por favor ingrese los datos solicitados")
print("Siga las indicaciones para que el programa funcione correctamente")
print("Sigase las indicaciones para que el programa funcione correctamente ")

#variable de control para menu
#print("""Ingrese 1 para Servicios Docente \n 2 Para Servicios estudiantiles \n 3 Para Servicios administrativos \n 4 Para Salir""")
digito=0

#menu de 4 opciones y sus subramas
while digito<=4:
    print("Ingrese 1 para Verificacion Docente:")
    print("Ingrese 2 para Confirmacion Estudiante:")
    print("Ingrese 3 para Administracion:")
    print("Ingrese 4 para Salir")
    digito=int(input("Ingrese un numero: "))

    #submenu de sercivios docente
    if digito==1:

        numero=0
        #numero=int(input("Ingrese el numero de servicios que desea verificar: "))
        print("Bienvenido a Servicios Docente")
        #Menu de docente.
        while (numero<=3):
            print("\t MENU")
            print("1. Ingresar como docente:")
            print("2. Mostrar cursos a cargo de docente:")
            print("3. Salir")
            numero=int(input("Ingrese el numero de servicios que desea verificar: "))

            if numero==1:
                print("\t Registro de Docente")
                Profesor.registrar_docente()
            elif numero==2:
                print("\t Mostrar cursos a cargo de docente")
                Profesor.mostrar_docente()
            elif numero==3:
                break

        salto_linea()

    #submenu de servicios estudiante
    elif digito==2:
        numero=0
        #numero=int(input("Ingrese el numero de servicios que desea verificar: "))
        print("Bienvenido a Servicios Estudiantiles")
        while (numero<=3):
            print("\t MENU")
            print("1. Matricularse:")
            print("2. Mostrar cursos :")
            print("3. Salir")
            numero=int(input("Ingrese el numero de servicios que desea verificar: "))
            #Submenu de matricula
            if numero==1:
                print("\t MATRICULA")
                while (numero<=3):
                    print("\t MENU")
                    print("1. Pagar:")
                    print("2. Mostrar informacion cursos:")
                    print("3. Salir")
                    numero=int(input("Ingrese el numero de servicios que desea verificar: "))

                    if numero==1:
                        pass #metdo para pagar
                    elif numero==2:
                        pass #metodo para mostrar informacion cursos
                    elif numero==3:
                        break

            elif numero==2:
                print("\t TUS CURSOS:")
                pass #metodo para mostrar cursos

            elif numero==3:
                break

        salto_linea()

    #submenu de servicios administrativos
    elif digito==3:
        numero=0
        #numero=int(input("Ingrese el numero de servicios que desea verificar: "))
        print("Bienvenido a Servicios Administrativos")
        while (numero<=4):
            print("\t MENU")
            print("1. Administrar Profesores:")
            print("2. Administrar Estudiantes:")
            print('3. Administrar Catalogos:')
            print("4. Salir")
            numero=int(input("Ingrese el numero de servicios que desea verificar: "))

            if numero==1:
                print("\t ADMINISTRAR PROFESORES")
                while (numero<=4):
                    print("\t MENU")
                    print("1.REGISTRAR PROFESOR:")
                    print("2.MOSTRAR PROFESOR:")
                    print("3.ELIMINAR PROFESOS:")
                    print("4. SALIR")
                    numero=int(input("Ingrese el numero de servicios que desea verificar: "))

                    if numero == 1:
                        print("\t Registrar nuevo profesor")
                    elif numero == 2:
                        print("\t Mostrar profesor")
                    elif numero == 3:
                        print("\t Eliminar profesor")
                    elif numero == 4:
                        print("\t Saliendo de administrar profesores")
                        break  # salir

            elif numero==2:
                print("\t ADMINISTRAR ESTUDIANTES")
                while (numero<=4):
                        print("\t MENU")
                        print("1. REGISTRAR ESTUDIANTES:")
                        print("2. MOSTRAR ESTUDIANTES:")
                        print("3. ELIMINAR ESTUDIANTES:")
                        print("4. SALIR")
                        numero=int(input("Ingrese el numero de servicios que desea verificar: "))

                        if numero==1:
                            print("\t Registrar nuevo estudiante")
                            #Estudiante.registrarEstudiante()
                        elif numero==2:
                            print("\t Mostrar estudiante")
                            #Estudiante.mostrar_estudiantes()
                        elif numero==3:
                            print("\t Eliminar estudiante")
                        elif numero == 4:
                            print("\t Saliendo de administrar estudiantes")
                            break #salir

            elif numero==3:
                print("\t ADMINISTRAR CATALOGOS")
                while (numero <= 6):
                        print("\t MENU")
                        print("1. Cursos")
                        print("2. Tipos de profesores")
                        print("3. Edificios")
                        print("4. Aulas")
                        print("5. Turno")
                        print("6. Programas")
                        print("7. Salir")
                        numero=int(input("Ingrese el numero del catalogo que desea administrar: "))

                        if numero==1:
                            print("\t ADMINISTRAR CURSOS")
                            while (numero <= 5):
                                    print("\t MENU DE CURSOS")
                                    print("1. Registrar nuevo curso")
                                    print("2. Editar curso")
                                    print("3. Mostrar cursos")
                                    print("4. Eliminar curso")
                                    print("5. Salir")
                                    numero=int(input("Ingrese el numero de servicio que desea verificar: "))

                                    if numero==1:
                                        print("\t Registrar nuevo curso")

                                    elif numero==2:
                                        print("\t Editar curso")

                                    elif numero==3:
                                        print("\t Mostrar curso")

                                    elif numero==4:
                                        print("\t Eliminar curso")

                                    elif numero==5:
                                        print("\t Usted ha salido del catalogo de cursos")
                                        break
                        elif numero==2:
                            print("\t ADMINISTRAR TIPOS DE PROFESORES")
                            while (numero <= 5):
                                    print("\t MENU DE TIPOS DE PROFESORES")
                                    print("1. Registrar nuevo tipo de profesor")
                                    print("2. Editar profesor")
                                    print("3. Mostrar profesores")
                                    print("4. Eliminar profesor")
                                    print("5. Salir")
                                    numero=int(input("Ingrese el numero de servicio que desea verificar: "))

                                    if numero==1:
                                        print("\t Registrar nuevo profesor")

                                    elif numero==2:
                                        print("\t Editar profesor")

                                    elif numero==3:
                                        print("\t Mostrar tipo de profesores")

                                    elif numero==4:
                                        print("\t Eliminar tipo de profesor")

                                    elif numero==5:
                                        print("\t Usted ha salido del catalogo de tipo de profesors")
                                        break
                        elif numero==3:
                            print("\t ADMINISTRAR EDIFICIOS")
                            while (numero <= 4):
                                    print("\t MENU DE EDIFICIOS")
                                    print("1. Registrar nuevos edificios")
                                    print("2. Eliminar edificios")
                                    print("3. Buscar edificios")
                                    print("4. SALIR")
                                    numero=int(input("Ingrese el numero de servicios que desea verificar: "))

                                    if numero==1:
                                        print("\t Registrar edificios")
                                        Edificio.registrar_edificio()

                                    elif numero==2:
                                        print("\t Eliminar edificios")
                                        Edificio.elimninar_edificio()

                                    elif numero==3:
                                        print("\t Buscar edificios")
                                        Edificio.buscar_edificio()

                                    elif numero==4:
                                        break
                        elif numero==4:
                            print("\t ADMINISTRAR AULAS")
                            while (numero <= 4):
                                    print("\t MENU")
                                    print("1. Registrar nuevas aulas")
                                    print("2. Eliminar aulas")
                                    print("3. Buscar aulas")
                                    print("4. SALIR")
                                    numero=int(input("Ingrese el numero de servicios que desea verificar: "))

                                    if numero==1:
                                        print("\t Registrar aulas")
                                        Aula.registrar_aula()

                                    elif numero==2:
                                        print("\t Eliminar aulas")
                                        Aula.elimninar_aula()

                                    elif numero==3:
                                        print("\t Buscar aula")
                                        Aula.buscar_aula()

                                    elif numero==4:
                                        break
                        elif numero==5:
                            print("\t ADMINISTRAR TURNOS")
                            while (numero <= 4):
                                print("\t MENU")
                                print("1. Registrar nuevos turnos")
                                print("2. Eliminar turnos")
                                print("3. Buscar turnos")
                                print("4. SALIR")
                                numero = int(input("Ingrese el numero de servicios que desea verificar: "))

                                if numero == 1:
                                    print("\t Registrar turnos")


                                elif numero == 2:
                                    print("\t Eliminar turnos")


                                elif numero == 3:
                                    print("\t Buscar turno")


                                elif numero == 4:
                                    break
                                
                        elif numero ==6:
                            #Administrar programas que contienen cursos para la clase analitics
                            print("\t ADMINISTRAR TURNOS")
                            while (numero <= 4):
                                print("\t MENU")
                                print("1. Crear programa")
                                print("2. Eliminar programas")
                                print("3. Buscar programas")
                                print("4. SALIR")
                                numero = int(input("Ingrese el numero de servicios que desea verificar: "))

                                if numero == 1:
                                    print("\t Crear programa")
                                    Programa.registrar_programa()



                                elif numero == 2:
                                    print("\t Eliminar programa")


                                elif numero == 3:
                                    print("\t Buscar Programa")


                                elif numero == 4:
                                    break
                        elif numero ==7:
                            print("\t Salir de catalogos")
                            break

            elif numero == 4:
                print("\t SALIENDO DE SERVICIOS ADMINISTRATIVOS")
                break

        salto_linea()

    #salir del menu principal
    elif digito==4:
        print("Gracias por usar nuestro sistema")
        break

#_______________________________________________________________________________








