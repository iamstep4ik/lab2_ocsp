from calc import LoadCalc

while True:
    weight = int(input("Введите вес груза: "))
    if weight <= 0:
        print("Вес должен быть больше 0")
    else:
        break

while True:
    floor = int(input("Введите этаж на который требуется поднять груз: "))
    if floor <= 1:
        print("Этаж должен быть выше 1")
    else:
        break

flag = bool(input("Введите возможно ли поднять груз на заданный этаж T/F: "))

new_calc  = LoadCalc(weight,floor,flag)

print(new_calc.price())