from curso import *
from programa import *
from Profesor import *
from Estudiante import *

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
print("Ingrese 1 para Servicios Docente \n 2 Para Servicios estudiantiles \n 3 Para Servicios administrativos \n 4 Para Salir")
digito=int(input("Ingrese un numero: "))

#menu de 4 opciones y sus subramas
while digito<=3:
    print("1 Verificacion Docente:")
    print("2 Confirmacion Estudiante:")
    print("3 Administracion:")
    print("4 Salir")
    digito=int(input("Ingrese un numero: "))
    
    #submenu de sercivios docente
    if digito==1:

        numero=0
        numero=int(input("Ingrese el numero de servicios que desea verificar: "))
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
        numero=int(input("Ingrese el numero de servicios que desea verificar: "))
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
                while (numero<=2):
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
        numero=int(input("Ingrese el numero de servicios que desea verificar: "))
        print("Bienvenido a Servicios Administrativos")
        while (numero<=3):
            print("\t MENU")
            print("1. Administrar Profesores:")
            print("2. Administrar Estudiantes:")
            print('3. Administrar Catalogos:')
            print("4. Salir")
            numero=int(input("Ingrese el numero de servicios que desea verificar: "))

            if numero==1:
                print("\t ADMINISTRAR PROFESORES")
                while (numero<=2):
                    print("\t MENU")
                    print("1.MOSTRAR PROFESORES:")
                    print("2.ELIMINAR PROFESORES:")
                    print("3. SALIR")
                    numero=int(input("Ingrese el numero de servicios que desea verificar: "))

                    if numero==1:
                        pass #metodo para mostrar profesores
                    elif numero==2:
                        pass #delete profesores
                    elif numero==3:
                        break

            elif numero==2:
                print("\t ADMINISTRAR ESTUDIANTES")
                while (numero<=2):
                        print("\t MENU")
                        print("1. REGISTRAR ESTUDIANTES:")
                        print("2. MOSTRAR ESTUDIANTES:")
                        print("3. ELIMINAR ESTUDIANTES:")
                        print("4. SALIR")
                        numero=int(input("Ingrese el numero de servicios que desea verificar: "))

                        if numero==1:
                            Estudiante.registrarEstudiante()
                            pass #metodo para registrar estudiantes
                        elif numero==2:
                            Estudiante.mostrar_estudiantes()
                            pass #mostrar estudiantes
                        elif numero==3:
                            pass #eliminar estudiantes
                        elif numero == 4:
                            break #salir

            elif numero==3:
                print("\t ADMINISTRAR CATALOGOS")
                while (numero <= 2):
                        print("\t MENU")
                        print("1. Cursos")
                        print("2. Aulas")
                        print("3. Tipos de profesores")
                        print('4. Edificio')
                        print('5. Turno')
                        numero=int(input("Ingrese el numero de servicios que desea verificar: "))

                        if numero==1:
                            pass #metodo para mostrar profesores
                        elif numero==2:
                            pass #delete profesores
                        elif numero==3:
                            break

            elif numero == 4:
                break

        salto_linea()        
    elif digito==4:
        
        print("Gracias por usar nuestro sistema")
        break


#_______________________________________________________________________________

 






