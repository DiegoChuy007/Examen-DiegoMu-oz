from clases.areas import areas

def main():
    ejemplo=areas(4,8)
    print("El área del triángulo es: ", ejemplo.area_triangulo())
    print("El área del rectángulo es: ", ejemplo.area_rectangulo())

if __name__ == '__main__':
    main()    
