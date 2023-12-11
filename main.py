try:
    print("Довжина сторін прямокутника")
    a = float(input("a = "))
    b = float(input("b = "))
    print("Площа: %.2f"% (a*b))

except Exception as e:
    print(e)