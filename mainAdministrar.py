from mainDocente import*
from mainEstudiante import*
from curso import*
from aula import*
from tipoProfesor import*
from turno import*
from edificio import*

class main_Administrar_cat:

    def menu_Administracion():
        print("\n")
        print("|****************************|")
        print("|**|         Menu         |**|")
        print("|**| Administrar catalogos|**|")
        print("|****************************|")
        print("") 

        numero=0
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
                main_Profesor.menu_adminDoc()

            elif numero==2:
                print("\t ADMINISTRAR ESTUDIANTES")
                main_Estudiante.menu_adminEstu()
            
            elif numero==3:
                print("\t ADMINISTRAR CATALOGOS")
                while (numero <= 5):
                        print("\t MENU")
                        print("1. Cursos")
                        print("2. Aulas")
                        print("3. Tipos de profesores")
                        print("4. Edificio")
                        print("5. Turno")
                        print("6. Salir")
                        numero=int(input("Ingrese el numero de servicios que desea verificar: "))

                        if numero==1:
                              print("\t ADMINISTRAR CURSOS")
                              Curso.administrar_Curso()

                        elif numero==2:
                            print("\t ADMINISTRAR AULAS")
   

                        elif numero==3:
                            print("\t ADMINISTRAR TIPO DE PROFESORES")
                            

                        elif numero==4:
                            print("\t ADMINISTRAR EDIFICIOS")
                           
                        
                        elif numero==5:
                            print("\t ADMINISTRAR TURNO")
                            

                        elif numero==6:
                            break
