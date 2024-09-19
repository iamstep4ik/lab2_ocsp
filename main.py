from calc import LoadCalc
print("Введите вес груза")
weight = int(input())
print("Введите этаж на который требуется поднять груз")
floor = int(input())
print("Введите возможно ли поднять груз на заданный этаж T/F")
flag = bool(input())

if weight <= 0:
    print("Вес должен быть больше 0")
if floor <= 1:
    print("Этаж должен быть выше 1")

new_calc  = LoadCalc(weight,floor,flag)