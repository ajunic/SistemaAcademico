from Persona import Persona


class Estudiante(Persona):

    contador_estudiante = 0
    __listaEstudiantes = []

    def __init__(self, tipo, nombre, apellido, cedula, direccion, telefono,
                 fecha_nacimiento, email, num_carnet, obj_matricula):
        Estudiante.contador_estudiante += 1
        super().__init__(tipo, nombre, apellido, cedula, direccion,
                         telefono, fecha_nacimiento, email)
        self.num_carnet = num_carnet
        self.obj_matricula = obj_matricula
        self.__id_estudiante = Estudiante.contador_estudiante

    def __str__(self):
        return f"""\nEstudiante:[ ID: {self.__id_estudiante}
        #Carnet: {self.num_carnet}
        #Matricula: {self.obj_matricula}]
        \t{super().__str__()}
        """

    # define setter and getter methods for Estudiante attributes
    def get_num_carnet(self):
        return self.__num_carnet

    def set_num_carnet(self, num_carnet):
        self.__num_carnet = num_carnet
    #Property
    num_carnet = property(get_num_carnet, set_num_carnet)