from Estudiante import *

class main_Estudiante:

    def menu_matricula(): 
        print("\n")
        print("|****************************|")
        print("|**|         Menu         |**|")
        print("|**|      Estudiante      |**|")
        print("|****************************|")
        print("") 
        
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

    def menu_adminEstu():
        while (numero<=4):
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
                            Estudiante.elimninar_estudiante()
                        elif numero == 4:
                            break #salir
