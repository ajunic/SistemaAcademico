from tipoProfesor import Tipo_profesor


class Turno:
    contador_turno = 0
    lista_turno = []

    def __init__(self, nombreturno, tipo_profesor):
        self._nombreturno = nombreturno
        self._tipo_profesor = tipo_profesor  # Aggregation, usa objeto
        Turno.contador_turno = + 1

    # Definir setter y getter for nombreturno
    def get_nombreturno(self):
        return self._nombreturno

    def set_nombreturno(self, nombreturno):
        self._nombreturno = nombreturno

    # Property
    nombreturno = property(get_nombreturno, set_nombreturno)

    def display(self):
        print("Turno: ", self._nombreturno)
        print("Tipo de Profesor: ", self._tipo_profesor.display())

    def __str__(self):
        return f"""\nTurno[
        Turno: {self._nombreturno}]
        Agregado: {self._tipo_profesor}]"""

    # Metodos para controlar la clase
    """def registrar_turno(self):
        print("Registrar turno\n")
        nombreturno = input("Ingrese el nombre del turno: ")
        objTurno = Turno(nombreturno)
        Turno.lista_turno.append(objTurno)

    def eliminar_turno(self):
        print("Eliminar turno\n")
        borrar = input("Escriba el turno que desea eliminar: ")
        bo = Turno.lista_turno.pop(borrar)
        print("-------------------")
        print("Eliminando----------------------")
        print("Se ha eliminado con exito el turno")

    def buscar_turno(self):
        print("Buscar turno\n")
        buscar = input("Escriba el turno que desea encontrar: ")
        bu = Turno.lista_turno.index(buscar)
        print("-------------------")
        print("Buscando------------------------")
        print(f"El turno que busca se encuentra en: {bu}")

    def modificar_turno(self):
        print("Modificar turno\n")
        numi = int(input("Ingrese el indice de turno que desea modificar: "))
        print(Turno.lista_turno[: numi])
        modi = input("Ingrese la modificacion que desea realizar: ")
        Turno.lista_turno[:numi] = [modi]
        print(Turno.lista_turno)"""

#prueba de la agregacion entre clase turno contiene a tipo_profesor
fff = Tipo_profesor("Horario")
p = Turno("Matutino", fff)
print(p)
