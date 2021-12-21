import statistics as stats
import csv
import datetime
class Analytics():

    fechaHora = datetime
    results = []
    header = ["Media Aritmetica", "Mediana", "Moda", "Minimo", "Maximo", "Fecha y Hora"]
    #header = []
    def __init__(self, *valores):
        self.__valores = valores
        self.menuAnalytics()


    def calcularMedia(self):
        media = stats.mean(self.__valores)
        Analytics.results.append(media)
        return f"\nLa media aritmética de los valores: {self.__valores} \n es {media}\n"

    # ---------------------------------------------------------------------------------
    def minimoMaximo(self):
        minimo = min(self.__valores)
        maximo = max(self.__valores)
        Analytics.results.append(minimo)
        Analytics.results.append(maximo)
        return f"\nEl valor minimo es: {minimo}\n El valor máximo es: {maximo}\n"

    # ---------------------------------------------------------------------------------
    def calcularMediana(self):
        mediana = stats.median(self.__valores)
        Analytics.results.append(mediana)
        return f"\nLa mediana de los valores dados es: {mediana}\n"

    # ---------------------------------------------------------------------------------
    def calcularModa(self):
        moda = stats.multimode(self.__valores)
        Analytics.results.append(moda)

        return f"\nLa moda de los valores dados es: {moda}\n"


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

                elif opc == 0:

                    with open("calculos.csv", "a+", encoding='utf-8', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(self.header)
                        writer.writerow(Analytics.results)
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
    
    #file = open("Estadisticas del Programa")

analitica = Analytics(60, 40,40,40, 30, 30, 30, 50, 10, 15)









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
        


