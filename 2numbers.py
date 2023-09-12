# Задача 12
import random
import math
x = round(random.random()*1000)
y = round(random.random()*1000)

s = x + y
p = x * y
print ("Задуманы два числа")
print ('Сумма задуманных чисел S = ' + str(s))
print ("произведение задуманных чисел S =" + str(p))

foundX = int((s + math.sqrt(s*s - 4*p))/2)
foundY = int((s - math.sqrt(s*s - 4*p))/2)
print ("Задуманы числа x = " + str(foundX) + " и число y = " + str(foundY))
