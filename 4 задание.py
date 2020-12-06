#s = int(input("Введите положительное число"))
#x = s//100
#c = (s-(x*100))//10
#y = s-(x*100)-(c*10)
#print (x,c,y)
number = int(input("Введите число"))
max_number = number%10 #ищем остаток от деления
while number > 0:
    if number%10 > number:
        max_number = number%10
    number = number//10
print("Максимальное число",max_number)

