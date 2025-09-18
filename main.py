from clases.areas import areas

def main():
    ejemplo=areas(4,8,6)
    print("El área del triángulo es: ", ejemplo.area_triangulo())
    print("El área del rectángulo es: ", ejemplo.area_rectangulo())
    print("El área del círculo es: ", ejemplo.area_circulo())

if __name__ == '__main__':
    main()    
