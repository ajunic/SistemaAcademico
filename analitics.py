
class Analitics:
    def __init__(self,media, moda, mediana, minimo,maximo):
        self.__media = media
        self.__moda= moda
        self.__mediana = mediana
        self.__minimo = minimo
        self.__maximo = maximo

    def __str__(self):
        return f"""\nAnalitics[
        Media: {self.__media}
        Moda: {self.__moda}
        Mediana: {self.__mediana}
        Minimo: {self.__minimo}
        Maximo: {self.__maximo}]"""

    def __del__(self):
        print(
            f"""Analitics: {self.__media} {self.__moda} 
            {self.__mediana}""")

    # define getter and setter for media
    def get_media(self):
        return self.__media

    def set_media(self, media):
        self.__media = media

    # define getter and setter for moda
    def get_moda(self):
        return self.__moda

    def set_moda(self, moda):
        self.__moda = moda

    # define getter and setter for mediana
    def get_mediana(self):
        return self.__mediana

    def set_mediana(self, mediana):
        self.__mediana = mediana

    # define getter and setter for minimo
    def get_minimo(self):
        return self.__minimo

    def set_minimo(self, minimo):
        self.__minimo = minimo

    # define getter and setter for maximo
    def get_maximo(self):
        return self.__maximo

    def set_maximo(self, maximo):
        self.__maximo = maximo

    #Proprty definitions for each attribute.
    media = property(get_media, set_media)
    moda = property(get_moda, set_moda)
    mediana = property(get_mediana, set_mediana)
    minimo = property(get_minimo, set_minimo)
    maximo = property(get_maximo, set_maximo)


    #Mostrar datos
    def show(self):
        print("Media: ", self.media)
        print("Moda: ", self.moda)
        print("Mediana: ", self.mediana)
        print("Minimo: ", self.minimo)
        print("Maximo: ", self.maximo)

    #create a method to calculate the analitics from other class
    def calculate(self, lista):
        self.media = sum(lista) / len(lista)
        self.moda = max(lista, key=lista.count)
        self.mediana = sorted(lista)[len(lista) // 2]
        self.minimo = min(lista)
        self.maximo = max(lista)
        


