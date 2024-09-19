from calc import LoadCalc

flag = True

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

while True:
    flag_input = input("Введите возможно ли поднять груз на заданный этаж (t/f): ").lower()
    if flag_input == 't':
        flag = True
        break
    elif flag_input == 'f':
        flag = False
        break
    else:
        print("Пожалуйста, введите 't' или 'f'")


new_calc  = LoadCalc(weight,floor,flag)

print(new_calc.price())