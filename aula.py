class Aula:
    listaulas = []

    def __init__(self, nombre_aula, numero_piso, numero_edificio, capacidad_asientos):
        self._nombre_aula = nombre_aula
        self._numero_piso = numero_piso
        self._numero_edificio = numero_edificio
        self._capacidad_asientos = capacidad_asientos
        

        
    def administrar_Aula(self): #Devolvera None
        pass

    def registrar_aula(self):
        print("Registrar aula\n")
        nombre_aula = input("Ingrese el nombre del aula: ")
        numero_piso = int(input("Introduzca el numero de piso: "))
        numero_edificio = int(input("Ingrese el numero del edificio: "))
        capacidad_asientos = int(input("Digite la capacidad de asientos: "))
        objAula = Aula(nombre_aula, numero_piso, numero_edificio, capacidad_asientos)
        Aula.listaulas.append(objAula)

    def eliminar_aula(self):
        print("Eliminar aula\n")
        borrar = input("Escriba el nombre del aula que desea eliminar: ")
        bo = Aula.listaulas.pop(borrar)
        print("-------------------")
        print("------------------------")
        print("Se ha eliminado con exito")
    
    def buscar_aula(self):
        print("Buscar aula\n")
        buscar = input("Escriba el nombre del aula que desea encontrar: ")
        bu = Aula.listaulas.index(buscar)
        print("-------------------")
        print("Buscando------------------------")
        print(f"El edificio que busca se encuentra en: {bu}")
    
    def modificar_aula(self):
        print("Modificar aula\n")
        numi = int(input("Ingrese el indice que desea modificar: "))
        print(Aula.listaulas[: numi])
        modi = input("Ingrese la modificacion que desea realizar: ")
        Aula.listaulas[:numi] = [modi]
        print(Aula.listaulas)


    #Define setter and getter methods.    
    def get_nombre_aula(self):
        return self._nombre_aula
    def set_nombre_aula(self, nombre_aula):
        self._nombre_aula = nombre_aula
    
    def get_numero_piso(self):
        return self._numero_piso
    def set_numero_piso(self, numero_piso):
        self._numero_piso = numero_piso
    
    def get_numero_edificio(self):
        return self._numero_edificio
    def set_numero_edificio(self, numero_edificio):
        self._numero_edificio = numero_edificio

    def get_capacidad_asientos(self):
        return self._capacidad_asientos
    def set_capacidad_asientos(self, capacidad_asientos):
        self._capacidad_asientos = capacidad_asientos

    #Property definitions for each attribute.
    nombre_aula = property(get_nombre_aula, set_nombre_aula)
    numero_piso = property(get_numero_piso, set_numero_piso)
    numero_edificio = property(get_numero_edificio, set_numero_edificio)
    capacidad_asientos = property(get_capacidad_asientos, set_capacidad_asientos)

    