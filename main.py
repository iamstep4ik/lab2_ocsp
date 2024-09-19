from calc import LoadCalc

weight = int(input("Введите вес груза: "))
floor = int(input("Введите этаж на который требуется поднять груз: "))
flag = bool(input("Введите возможно ли поднять груз на заданный этаж T/F: "))

if weight <= 0:
    print("Вес должен быть больше 0")
if floor <= 1:
    print("Этаж должен быть выше 1")

new_calc  = LoadCalc(weight,floor,flag)