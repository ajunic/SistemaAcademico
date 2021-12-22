from mainAdministrar import*
from mainDocente import* 
from mainEstudiante import*
from programa import *



#Programa principal
"""Autores:-    
    -Rodolfo Melendez
    -Ashly Ramos
    -Guillermo Carvajal
    -Michael Gomez
    -Manuel Caceres 
    -Francisco Blandino
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
#print("Ingrese 1 para Servicios Docente \n 2 Para Servicios estudiantiles \n 3 Para Servicios administrativos \n 4 Para Salir")
#digito=int(input("Ingrese un numero: "))
digito=0

#menu de 4 opciones y sus subramas
while digito<=4:
    print("1 Verificacion Docente:")
    print("2 Confirmacion Estudiante:")
    print("3 Administracion:")
    print("4 Salir")
    digito=int(input("Ingrese un numero: "))
    
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


#_______________________________________________________________________________

 






