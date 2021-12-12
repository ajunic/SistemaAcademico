class Matricula:
    def __init__(self, fecha_matricula, hora_matricula):
        self.__fecha_matricula = fecha_matricula
        self.__hora_matricula = hora_matricula
        
    
    # fechaMatricula
    def getfecha_matricula(self):
        return self.__fecha_matricula

    def setfecha_matricula(self, fechaM):
        self.__fecha_matricula = fechaM

    # horaMatricula
    def gethora_matricula(self):
        return self.__hora_matricula
    
    def sethora_matricula(self, horaM):
        self.__hora_matricula = horaM

    # --------------------------------------------------
    def agregar_Curso(curso): #Devolvera None
        
        pass

    def agregar_Nota(nota): #Devolvera Int
        pass

    def total_vendido(precio): #Devolvera Float
        pass

    fecha_matricula = property(getfecha_matricula, setfecha_matricula)
    hora_matricula  = property(gethora_matricula, sethora_matricula)