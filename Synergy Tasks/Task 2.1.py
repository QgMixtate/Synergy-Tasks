# coding=windows-1251
number = 46275

units = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
tenthousands = (number // 10000) % 10

result = (tens ** units) * hundreds * 2 / (tenthousands - thousands)

print(result)
