class Edificio:
    listEdificio = []

    def __init__(self, nombre_edificio, direccion, cantidad_pisos, cantidad_aulas):
        self.__nombre_edificio = nombre_edificio
        self.__direccion = direccion
        self.__cantidad_pisos = cantidad_pisos
        self.__cantidad_aulas = cantidad_aulas

    def registrar_edificio():
        print("Registrar edificio\n")
        nombre_edificio = input("Ingrese el nombre del edificio: ")
        direccion = input("Introduzca la direccion del edificio: ")
        cantidad_pisos = int(input("Ingrese la cantidad de pisos que contiene: "))
        cantidad_aulas = int(input("Ingrese la cantidad de aulas que contiene: "))
        objEdificio = Edificio(nombre_edificio, direccion, cantidad_pisos, cantidad_aulas)
        Edificio.listEdificio.append(objEdificio)

    def elimninar_edificio():
        print("Eliminar edificio\n")
        borrar = input("Escriba el nombre del edificio que desea eliminar: ")
        bo = Edificio.listEdificio.pop(borrar)
        print("-------------------")
        print("------------------------")
        print("Se ha eliminado con exito")
    
    def buscar_edificio():
        print("Buscar edificio\n")
        buscar = input("Escriba el nombre del edificio que desea encontrar: ")
        bu = Edificio.listEdificio.index(buscar)
        print("-------------------")
        print("Buscando------------------------")
        print(f"El edificio que busca se encuentra en: {bu}")
    
    def modificar_edificio():
        print("Modificar edificio\n")
        numi = int(input("Ingrese el indice que desea modificar: "))
        print(Edificio.listEdificio[: numi])
        modi = input("Ingrese la modificacion que desea realizar: ")
        Edificio.listEdificio[:numi] = [modi]
        print(Edificio.listEdificio)

    #Defining Getters and Setters
    def get_nombre_edificio(self):
        return self.__nombre_edificio
    def set_nombre_edificio(self, nombre_edificio):
        self.__nombre_edificio == nombre_edificio
    def get_direccion(self):
        return self.__direccion
    def set_direccion(self, direccion):
        self.__direccion == direccion
    def get_cantidad_pisos(self):
        return self.__cantidad_pisos
    def set_cantidad_pisos(self, cantidad_pisos):
        self.__cantidad_pisos == cantidad_pisos
    def get_cantidad_aulas(self):
        return self.__cantidad_pisos
    def set_cantidad_aulas(self, cantidad_aulas):
        self.__cantidad_aulas == cantidad_aulas

    #Property definitions for each attribute.

    nombre_edifcio = property(get_nombre_edificio, set_nombre_edificio)
    direccion = property(get_direccion,set_direccion)
    cantidad_pisos = property(get_cantidad_pisos, set_cantidad_pisos)
    cantidad_aulas = property(get_cantidad_aulas, get_cantidad_aulas)

    def administrar_edificio():
        while (numero <= 4):
            print("\t MENU")
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



