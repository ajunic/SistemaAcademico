
class Analitics:
    def __init__(self,media, moda, mediana, minimo,maximo):
        self._media = media
        self._moda= moda
        self._mediana = mediana
        self._minimo = minimo
        self._maximo = maximo

    def __str__(self):
        return f"""\nAnalitics[
        Media: {self._media}
        Moda: {self._moda}
        Mediana: {self._mediana}
        Minimo: {self._minimo}
        Maximo: {self._maximo}]"""

    def __del__(self):
        print(
            f"""Analitics: {self._media} {self._moda} 
            {self._mediana}""")

    # define getter and setter for media
    def get_media(self):
        return self._media

    def set_media(self, media):
        self._media = media

    # define getter and setter for moda
    def get_moda(self):
        return self._moda

    def set_moda(self, moda):
        self._moda = moda

    # define getter and setter for mediana
    def get_mediana(self):
        return self._mediana

    def set_mediana(self, mediana):
        self._mediana = mediana

    # define getter and setter for minimo
    def get_minimo(self):
        return self._minimo

    def set_minimo(self, minimo):
        self._minimo = minimo

    # define getter and setter for maximo
    def get_maximo(self):
        return self._maximo

    def set_maximo(self, maximo):
        self._maximo = maximo

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
        


