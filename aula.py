class Aula:
    def __init__(self, nombre_aula, numero_piso, numero_edificio, capacidad_asientos):
        self.__nombre_aula = nombre_aula
        self.__numero_piso = numero_piso
        self.__numero_edificio = numero_edificio
        self.__capacidad_asientos = capacidad_asientos
        

        
    def administrar_Aula(): #Devolvera None
        pass
    #Define setter and getter methods.    
    def get_nombre_aula(self):
        return self.__nombre_aula
    def set_nombre_aula(self, nombre_aula):
        self.__nombre_aula = nombre_aula
    
    def get_numero_piso(self):
        return self.__numero_piso
    def set_numero_piso(self, numero_piso):
        self.__numero_piso = numero_piso
    
    def get_numero_edificio(self):
        return self.__numero_edificio
    def set_numero_edificio(self, numero_edificio):
        self.__numero_edificio = numero_edificio

    def get_capacidad_asientos(self):
        return self.__capacidad_asientos
    def set_capacidad_asientos(self, capacidad_asientos):
        self.__capacidad_asientos = capacidad_asientos

    #Property definitions for each attribute.
    nombre_aula = property(get_nombre_aula, set_nombre_aula)
    numero_piso = property(get_numero_piso, set_numero_piso)
    numero_edificio = property(get_numero_edificio, set_numero_edificio)
    capacidad_asientos = property(get_capacidad_asientos, set_capacidad_asientos)

    