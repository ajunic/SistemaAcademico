from curso import *
from programa import *
from Profesor import *
from edificio import *
from Estudiante import *
from aula import *
from tipoProfesor import *
from turno import *

def admi_catalogos():
    numero = 0
    # numero=int(input("Ingrese el numero de servicios que desea verificar: "))
    print("Bienvenido a Servicios Administrativos")
    while (numero <= 4):
        print("\t MENU")
        print("1. Administrar Profesores:")
        print("2. Administrar Estudiantes:")
        print('3. Administrar Catalogos:')
        print("4. Salir")
        numero = int(input("Ingrese el numero de servicios que desea verificar: "))

        if numero == 1:
            numero = 0
            print("\t ADMINISTRAR PROFESORES")
            while (numero <= 4):
                print("\t MENU")
                print("1.REGISTRAR PROFESOR:")
                print("2.MOSTRAR PROFESOR:")
                print("3.ELIMINAR PROFESOS:")
                print("4. SALIR")
                numero = int(input("Ingrese el numero de servicios que desea verificar: "))

                if numero == 1:
                    Profesor.registrar_docente()
                elif numero == 2:
                    Profesor.elimninar_docente()
                elif numero == 3:
                    break

        elif numero == 2:
            numero = 0
            print("\t ADMINISTRAR ESTUDIANTES")
            while (numero <= 4):
                print("\t MENU")
                print("1. REGISTRAR ESTUDIANTES:")
                print("2. MOSTRAR ESTUDIANTES:")
                print("3. ELIMINAR ESTUDIANTES:")
                print("4. SALIR")
                numero = int(input("Ingrese el numero de servicios que desea verificar: "))

                if numero == 1:
                    print("\t Registrar nuevo estudiante")
                    Estudiante.registrarEstudiante()

                elif numero == 2:
                    print("\t Mostrar estudiante")
                    # Estudiante.mostrar_estudiantes()
                elif numero == 3:
                    Estudiante.elimninar_estudiante()
                elif numero == 4:
                    print("\t Saliendo de administrar estudiantes")
                    break  # salir

        elif numero == 3:
            numero = 0
            print("\t ADMINISTRAR CATALOGOS")
            while (numero <= 5):
                print("\t MENU")
                print("1. Cursos")
                print("2. Aulas")
                print("3. Tipos de profesores")
                print("4. Edificio")
                print("5. Turno")
                print('6. Programas')
                print("7. Salir")
                numero = int(input("Ingrese el numero de servicios que desea verificar: "))

                if numero == 1:
                    print("\t ADMINISTRAR CURSOS")
                    while (numero <= 2):
                        print("\t MENU")
                        print("1. Registrar nuevos cursos")
                        print("2. Eliminar cursos")
                        print("3. Buscar cursos")
                        print("4. SALIR")
                        numero = int(input("Ingrese el numero de servicios que desea verificar: "))

                        if numero == 1:
                            print("\t Registrar cursos")
                            Curso.crear_curso()

                        elif numero == 2:
                            print("\t Eliminar cursos")
                            Curso.eliminar_curso

                        elif numero == 3:
                            print("\t Buscar cursos")
                            Curso.buscar_curso()

                        elif numero == 4:
                            break

                elif numero == 2:
                    numero = 0
                    print("\t ADMINISTRAR AULAS")
                    while (numero <= 4):
                        print("\t MENU")
                        print("1. Registrar nuevas aulas")
                        print("2. Eliminar aulas")
                        print("3. Buscar aulas")
                        print("4. SALIR")
                        numero = int(input("Ingrese el numero de servicios que desea verificar: "))

                        if numero == 1:
                            print("\t Registrar aulas")
                            Aula.registrar_aula()

                        elif numero == 2:
                            print("\t Eliminar aulas")
                            Aula.elimninar_aula()

                        elif numero == 3:
                            print("\t Buscar aula")
                            Aula.buscar_aula()

                        elif numero == 4:
                            break

                elif numero == 3:
                    numero = 0
                    print("\t ADMINISTRAR TIPO DE PROFESORES")
                    while (numero <= 4):
                        print("\t MENU")
                        print("1. Registrar nuevos tipos de profesores")
                        print("2. Eliminar tipo de profesor")
                        print("3. Buscar tipo de profesor")
                        print("4. SALIR")
                        numero = int(input("Ingrese el numero de servicios que desea verificar: "))

                        if numero == 1:
                            print("\t Registrar nuevo tipo de profesor")
                            Tipo_profesor.registrar_tipo_profesor()

                        elif numero == 2:
                            print("\t Eliminar tipo de profesor")
                            Tipo_profesor.elimninar_tipo_profesor()

                        elif numero == 3:
                            print("\t Buscar tipo de profesor")
                            Tipo_profesor.buscar_tipo_profesor()

                        elif numero == 4:
                            break

                elif numero == 4:
                    numero = 0
                    print("\t ADMINISTRAR EDIFICIOS")
                    while (numero <= 4):
                        print("\t MENU")
                        print("1. Registrar nuevos edificios")
                        print("2. Eliminar edificios")
                        print("3. Buscar edificios")
                        print("4. SALIR")
                        numero = int(input("Ingrese el numero de servicios que desea verificar: "))

                        if numero == 1:
                            print("\t Registrar edificios")
                            Edificio.registrar_edificio()

                        elif numero == 2:
                            print("\t Eliminar edificios")
                            Edificio.elimninar_edificio()

                        elif numero == 3:
                            print("\t Buscar edificios")
                            Edificio.buscar_edificio()

                        elif numero == 4:
                            break

                elif numero == 5:
                    numero = 0
                    print("\t ADMINISTRAR TURNO")
                    while (numero <= 4):
                        print("\t MENU")
                        print("1. Registrar nuevos turnos")
                        print("2. Eliminar turnos")
                        print("3. Buscar turnos")
                        print("4. SALIR")
                        numero = int(input("Ingrese el numero de servicios que desea verificar: "))

                        if numero == 1:
                            print("\t Registrar nuevo turno")
                            Turno.registrar_turno()

                        elif numero == 2:
                            print("\t Eliminar turno")
                            Turno.elimninar_turno()

                        elif numero == 3:
                            print("\t Buscar turno")
                            Turno.buscar_turno()

                        elif numero == 4:
                            break

                elif numero == 6:
                    numero = 0
                    print("\t ADMINISTRAR PROGRAMAS")
                    while (numero <= 4):
                        print("\t MENU")
                        print("1. Registrar nuevos programa")
                        print("2. Eliminar programa")
                        print("3. Buscar programa")
                        print('4. Mostrar programas')
                        print("5. SALIR")
                        numero = int(input("Ingrese el numero de servicios que desea verificar: "))

                        if numero == 1:
                            print("\t Registrar nuevo programa")
                            
                        elif numero == 2:
                            print("\t Eliminar programa")
                            
                        elif numero == 3:
                            print("\t Buscar programa")
                            
                        elif numero == 4:
                            print("\t Mostrar programas")
                            Programa.imprimir_cursos()
                            
                        elif numero == 5:
                            break

                elif numero == 7:
                    break

        elif numero == 4:
            print("\t SALIENDO DE SERVICIOS ADMINISTRATIVOS")
            break