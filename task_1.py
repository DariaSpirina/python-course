#Задача 2: Найдите сумму цифр трехзначного числа.
#n = int(input("Введите трехзначное число  "))
#a = n//100
#b = (n%100)//10
#c = n%10
#sum = a+b+c
#print("Сумма всех цифр данного числа равна", sum)


#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
#они сделали S журавликов. Сколько журавликов сделал каждый
#ребенок, если известно, что Петя и Сережа сделали одинаковое
#количество журавликов, а Катя сделала в два раза больше журавликов,
#чем Петя и Сережа вместе?

#s = int(input("Введите число кратное 6 "))
#n = (s/6)
#m= (n*4)
#print("Петя и Сережа сделали",n, "журавликов, а Катя -", m)



#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
#расплачивались за проезд и получали билет с номером. Счастливым
#билетом называют такой билет с шестизначным номером, где сумма
#первых трех цифр равна сумме последних трех. Т.е. билет с номером
#385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
#программу, которая проверяет счастливость билета.

#n = int(input("Введите шестизначное число  "))
#a = n//100000
#b = (n%100000)//10000
#c = (n%10000)//1000
#d = (n%1000)//100
#e = (n%100)//10
#f = n%10
#sum1 = a+b+c
#sum2 = d+e+f
#if sum1 == sum2:
 #   print("Этот билет счастливый!")
#else:
 #   print("Этот билет несчастливый!")



#Задача 8: Требуется определить, можно ли от шоколадки размером n
#× m долек отломить k долек, если разрешается сделать один разлом по
#прямой между дольками (то есть разломить шоколадку на два
#прямоугольника).

#n = int(input("Введите ширину шоколадки "))
#m = int(input("Введите длину шоколадки "))
#k = int(input("Введите количество отломленных долек "))
#if (k%n ==0 or k%m ==0):
 #   print("Можно")
#else:
 #   print("Нельзя") 
