try:
    def area_of_rhombus(side, height):

        return side * height


    side = float(input("Введіть довжину сторони ромба: "))

    height = float(input("Введіть висоту ромба: "))

    print("Площа ромба:", area_of_rhombus(side, height))


except Exception as e:
    print(e)