try:
    a = int(input("Перше число = "))
    b = int(input("Друге число = "))
    s = 0
    for i in range(a,b+1):
        s=s+1

    print(f"Сума двух чисел = {a+b}")
    print(f"Середнє арифметичне = {s/2} ")



except Exception as e:
    print(e)