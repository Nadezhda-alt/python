km_1 = int(input("Сколько вы пробежали в первый день?"))
km = int(input("Введите сколько вы хотите пробежать?"))
day_1 = 1 #первый день
min_km = km_1 #минимальное кол-во км в 1 день
while day_1 < km:
    day_1 += 1
    day = 0.1 * km_1 + km_1 #формулы,трудно не запутаться
    min_km = min_km + day #теперь к минимальному плюсуем
print("Вы достигнете результата на", min_km,"-й день", km, "км")
#явно циклы легкая вещь,но их надо полюбить и понимать. Я так и не понимаю как убрать
#точки после числа в принте.
