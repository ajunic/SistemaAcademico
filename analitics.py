import statistics as stats

class Analytics():
    def __init__(self, *valores):
        self.__valores = valores
        self.menuAnalytics()


    def calcularMedia(self):
        return f"\nLa media aritmética de los valores: {self.__valores} \n es {stats.mean(self.__valores)}\n"

    # ---------------------------------------------------------------------------------
    def minimoMaximo(self):
        return f"\nEl valor minimo es: {min(self.__valores)}\n El valor máximo es: {max(self.__valores)}\n"

    # ---------------------------------------------------------------------------------
    def calcularMediana(self):
        return f"\nLa mediana de los valores dados es: {stats.median(self.__valores)}\n"

    # ---------------------------------------------------------------------------------
    def calcularModa(self):
        return f"\nLa moda de los valores dados es: {stats.multimode(self.__valores)}\n"

    #---------------------------------------------------------------------------------
    def menuAnalytics(self):
        repetir = True
        while repetir:
            opc = int(input("\033[4;34m" + 'Elija una opción del menu a continuación:\n'
                            '1.Calcular media aritmética\n'
                            '2.Calcular mediana\n'
                            '3.Calcular moda\n'
                            '4.Calcular el valor minimo y maximo de los valores\n'
                            '5.Calcular Todo\n'
                            '0.Salir\n'))
            try:
                if opc == 1:
                    print("\033[4;32m" + self.calcularMedia())
                elif opc == 2:
                    print("\033[4;32m" + self.calcularMediana())
                elif opc == 3:
                    print("\033[4;32m" + self.calcularModa())
                elif opc == 4:
                    print("\033[4;32m" + self.minimoMaximo())
                elif opc == 5:
                    print("\033[4;32m" + self.calcularMedia())
                    print("\033[4;32m" + self.calcularMediana())
                    print("\033[4;32m" + self.calcularModa())
                    print("\033[4;32m" + self.minimoMaximo())
                    repetir = False
                    return
                elif opc == 0:
                    print("\033[4;32m" + "Deteniendo ejecucion...")
                    repetir = False
                    return
                else:
                    raise ValueError
            except ValueError:
                print(
                    "\033[4;31m" + f"Error: Opcion inválida. Vuelva a intentarlo.")
                break

    # ---------------------------------------------------------------------------------


analitica = Analytics(60, 40, 30)










# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------- ESTO ES LO QUE YA ESTABA ANTES -------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# class Analitics:
#     def __init__(self, media, moda, mediana, minimo, maximo):
#         self.__media = media
#         self.__moda= moda
#         self.__mediana = mediana
#         self.__minimo = minimo
#         self.__maximo = maximo
#
#     def __str__(self):
#         return f"""\nAnalitics[
#         Media: {self.__media}
#         Moda: {self.__moda}
#         Mediana: {self.__mediana}
#         Minimo: {self.__minimo}
#         Maximo: {self.__maximo}]"""
#
#     def __del__(self):
#         print(
#             f"""Analitics: {self.__media} {self.__moda}
#             {self.__mediana}""")
#
#     # define getter and setter for media
#     def get_media(self):
#         return self.__media
#
#     def set_media(self, media):
#         self.__media = media
#
#     # define getter and setter for moda
#     def get_moda(self):
#         return self.__moda
#
#     def set_moda(self, moda):
#         self.__moda = moda
#
#     # define getter and setter for mediana
#     def get_mediana(self):
#         return self.__mediana
#
#     def set_mediana(self, mediana):
#         self.__mediana = mediana
#
#     # define getter and setter for minimo
#     def get_minimo(self):
#         return self.__minimo
#
#     def set_minimo(self, minimo):
#         self.__minimo = minimo
#
#     # define getter and setter for maximo
#     def get_maximo(self):
#         return self.__maximo
#
#     def set_maximo(self, maximo):
#         self.__maximo = maximo
#
#     #Proprty definitions for each attribute.
#     media = property(get_media, set_media)
#     moda = property(get_moda, set_moda)
#     mediana = property(get_mediana, set_mediana)
#     minimo = property(get_minimo, set_minimo)
#     maximo = property(get_maximo, set_maximo)
#
#
#     #Mostrar datos
#     def show(self):
#         print("Media: ", self.media)
#         print("Moda: ", self.moda)
#         print("Mediana: ", self.mediana)
#         print("Minimo: ", self.minimo)
#         print("Maximo: ", self.maximo)
#
#     #create a method to calculate the analitics from other class
#     def calculate(self, lista):
#         self.media = sum(lista) / len(lista)
#         self.moda = max(lista, key=lista.count)
#         self.mediana = sorted(lista)[len(lista) // 2]
#         self.minimo = min(lista)
#         self.maximo = max(lista)
        


