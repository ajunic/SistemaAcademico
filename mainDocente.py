from Profesor import*

class main_Profesor:

    def menu_verificacion():
        print("\n")
        print("|****************************|")
        print("|**|         Menu         |**|")
        print("|**|        Docente       |**|")
        print("|****************************|")
        print("") 

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

    def menu_adminDoc():
        numero=0
        while (numero<=2):
            print("\t MENU")
            print("1.MOSTRAR PROFESORES:")
            print("2.ELIMINAR PROFESORES:")
            print("3. SALIR")
            numero=int(input("Ingrese el numero de servicios que desea verificar: "))

            if numero==1:
                Profesor.mostrar_docente()
            elif numero==2:
                Profesor.elimninar_docente()
            elif numero==3:
                break