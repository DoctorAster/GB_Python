#задача 22
import random
n = int(input("Введите число n: "))
m = int(input("Введите число m: "))

n_numbers = [round(100*random.random()) for i in range(n)]
m_numbers = [round(100*random.random()) for i in range(m)]

print(n_numbers, m_numbers)

n_numbers = set(n_numbers)
m_numbers = set(m_numbers)
pre_result = n_numbers.intersection(m_numbers)
print(pre_result)
result = list(pre_result)
result.sort()

print(result)