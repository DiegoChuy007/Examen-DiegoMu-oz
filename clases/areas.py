import numpy as np
class areas:
    def __init__ (self, base, altura,radio):
        self.base=base 
        self.altura=altura
        self.radio=radio
    def area_rectangulo(self):
        return (self.base*self.altura)
    def area_triangulo(self):
        return ((self.base * self.altura)/2)
    def area_circulo(self):
        return (((self.radio)**2)*np.pi)